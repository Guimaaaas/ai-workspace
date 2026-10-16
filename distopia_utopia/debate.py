"""Experimento Distopia / Utopia — debate multiagente em loop de 20 rodadas.

Uso:
    python debate.py --session distopia          # Sessão 1
    python debate.py --session utopia            # Sessão 2
    python debate.py --session ambas             # as duas, em sequência
    python debate.py --session distopia --resume # continua de onde parou
    python debate.py --session ambas --mock      # teste offline, sem API nem Ollama
"""

import argparse
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path

import prompts as P
from llm import ClaudeBackend, ClaudeCodeBackend, ModelRefusal, MockBackend, OllamaBackend

BASE_DIR = Path(__file__).parent
OUTPUT_DIR = BASE_DIR / "outputs"
ENV_FILE = BASE_DIR / ".env"

# Llama local tem janela de contexto curta: limita o histórico enviado a ele.
LOCAL_DIGEST_ROUNDS = 4
LOCAL_TURN_CHARS = 1500
DIGEST_CHARS = 700


class Agent:
    def __init__(self, key, name, hat, backend, system_prompt, frame=None):
        self.key = key
        self.name = name
        self.hat = hat
        self.backend = backend
        self.system = f"{system_prompt}\n\n{frame or P.COMMON_FRAMES['distopia']}"

    @property
    def is_local(self):
        return self.backend.kind == "local"


def build_agents(session, mock=False):
    if mock:
        remote = lambda n: MockBackend(n, "remoto")
        local = MockBackend("Llama", "local")
    else:
        claude = ClaudeBackend() if os.getenv("CLAUDE_BACKEND") == "api" else ClaudeCodeBackend()
        remote = lambda n: claude
        local = OllamaBackend()
    frame = P.COMMON_FRAMES[session]
    return [
        Agent("orchestrator", "Mediador / Orquestrador", "Chapéu Azul",
              remote("Orchestrator"), P.ORCHESTRATOR_PROMPTS[session], frame),
        Agent("architect", "Arquiteto da Transição", "Chapéu Verde/Amarelo",
              remote("Architect"), P.ARCHITECT_PROMPTS[session], frame),
        Agent("risk", "Analista de Riscos & Atrito", "Chapéu Preto",
              local, P.RISK_ANALYST_PROMPTS[session], frame),
        Agent("scientist", "Cientista de Fatos & Epidemiologista", "Chapéu Branco/Vermelho",
              remote("DataScientist"), P.DATA_SCIENTIST_PROMPTS[session], frame),
    ]


# ---------------- Montagem de contexto ----------------
def _clip(text, limit):
    return text if len(text) <= limit else text[:limit].rstrip() + " […]"


def _format_turns(turns, limit=None):
    return "\n\n".join(
        f"### {t['name']} ({t['model']})\n{_clip(t['content'], limit) if limit else t['content']}"
        for t in turns
    )


def build_context(session, transcript, round_no, current_turns, agent):
    cfg = P.SESSIONS[session]
    agenda = P.agenda_for(round_no, session)
    rounds = transcript["rounds"]
    parts = [
        f"# SESSÃO: {cfg['label']}",
        f"**Pergunta central:** {cfg['question']}",
        f"**Foco dos agentes:** {cfg['focus']}",
    ]
    # Memória: abertura do Mediador de cada rodada anterior (resumo + pergunta-desafio).
    past = rounds[-LOCAL_DIGEST_ROUNDS:] if agent.is_local else rounds
    if past:
        digest = "\n".join(
            f"- **R{r['round']:02d}** ({r['agenda']['phase']}): "
            f"{_clip(r['turns'][0]['content'], DIGEST_CHARS).replace(chr(10), ' ')}"
            for r in past
        )
        parts.append(f"## MEMÓRIA DO DEBATE (aberturas do Mediador)\n{digest}")

    if rounds:
        prev = rounds[-1]
        limit = LOCAL_TURN_CHARS if agent.is_local else None
        parts.append(f"## RODADA ANTERIOR ({prev['round']:02d}) — íntegra\n{_format_turns(prev['turns'], limit)}")

    parts.append(
        f"## RODADA {round_no:02d} de {P.TOTAL_ROUNDS}\n"
        f"**Bloco:** {agenda['phase']}\n**Objetivo temático:** {agenda['goal']}\n"
        f"**Entregável intermediário:** {agenda['deliverable']}"
    )
    if current_turns:
        parts.append(f"### Falas desta rodada até agora\n{_format_turns(current_turns)}")
    else:
        parts.append("_(Você abre a rodada.)_")

    parts.append(f"---\nAgora é a sua vez, como **{agent.name}** ({agent.hat}). Escreva apenas a sua fala.")
    return "\n\n".join(parts)


# ---------------- Persistência ----------------
def session_dir(session):
    d = OUTPUT_DIR / session
    (d / "rodadas").mkdir(parents=True, exist_ok=True)
    return d


def render_round_md(session, rnd):
    a = rnd["agenda"]
    head = (f"# {P.SESSIONS[session]['label']} — Rodada {rnd['round']:02d}/{P.TOTAL_ROUNDS}\n\n"
            f"**{a['phase']}** · {a['goal']}\n\n**Entregável:** {a['deliverable']}\n\n---\n\n")
    body = "\n\n---\n\n".join(
        f"## {t['name']} · {t['hat']}\n*Modelo: {t['model']}*\n\n{t['content']}" for t in rnd["turns"]
    )
    return head + body + "\n"


def save(session, transcript):
    d = session_dir(session)
    (d / "transcript.json").write_text(json.dumps(transcript, ensure_ascii=False, indent=2), encoding="utf-8")
    for rnd in transcript["rounds"]:
        (d / "rodadas" / f"rodada_{rnd['round']:02d}.md").write_text(render_round_md(session, rnd), encoding="utf-8")


def loop_diagram(agents):
    by_key = {a.key: a for a in agents}
    return f"""```mermaid
flowchart LR
    subgraph Remoto["Modelo remoto — Anthropic API"]
        O["Mediador<br/>{by_key['orchestrator'].backend.label}"]
        A["Arquiteto<br/>{by_key['architect'].backend.label}"]
        S["Cientista<br/>{by_key['scientist'].backend.label}"]
    end
    subgraph Local["Modelo local — Ollama"]
        R["Analista de Riscos<br/>{by_key['risk'].backend.label}"]
    end
    O -->|pergunta-desafio| A -->|proposta| R -->|furos| S -->|evidências| O
    O -.->|"20 rodadas · marcos R1, R5, R20"| F[("Plano final .md")]
```"""


def models_table(agents):
    rows = "\n".join(
        f"| {a.name} | {a.hat} | {a.backend.label} | {a.backend.kind} |" for a in agents
    )
    return "| Persona | Chapéu | Modelo | Execução |\n|---|---|---|---|\n" + rows


def write_milestones(session, transcript, agents):
    """Gera marcos.md (rodadas 1, 5, 20 na íntegra) e slides.md (seção 7 do prompt.md)."""
    d = session_dir(session)
    cfg = P.SESSIONS[session]
    by_round = {r["round"]: r for r in transcript["rounds"]}

    marcos = [f"# Marcos do debate — {cfg['label']}\n"]
    for n in P.MILESTONES:
        if n in by_round:
            slide = transcript["slides"].get(str(n), "")
            marcos.append(f"\n{slide}\n\n<details><summary>Rodada {n:02d} na íntegra</summary>\n\n"
                          f"{render_round_md(session, by_round[n])}\n</details>\n")
    (d / "marcos.md").write_text("\n".join(marcos), encoding="utf-8")

    final = transcript.get("final_doc") or ""
    m = re.search(r"##\s*6\.[^\n]*\n(.*?)(?=\n##\s*7\.|\Z)", final, re.S)
    diferencial = m.group(1).strip() if m else "_(disponível após a Rodada 20)_"
    slides = [
        f"# Slides — {cfg['label']}\n",
        "## Diagrama do Loop\n", loop_diagram(agents),
        "\n## Quadro de Modelos e Papéis\n", models_table(agents),
        "\n## Os Três Marcos da Evolução\n",
        *[transcript["slides"].get(str(n), f"_Rodada {n} ainda não executada._") + "\n" for n in P.MILESTONES],
        "\n## O Diferencial Criativo\n", diferencial, "",
    ]
    (d / "slides.md").write_text("\n".join(slides), encoding="utf-8")


# ---------------- Execução ----------------
def banner(text):
    line = "=" * 78
    print(f"\n{line}\n{text}\n{line}", flush=True)


def run_session(session, mock=False, resume=False, rounds=P.TOTAL_ROUNDS):
    cfg = P.SESSIONS[session]
    agents = build_agents(session, mock)
    orchestrator = agents[0]
    path = session_dir(session) / "transcript.json"

    if resume and path.exists():
        transcript = json.loads(path.read_text(encoding="utf-8"))
        print(f"Retomando {session} a partir da rodada {len(transcript['rounds']) + 1}.")
    else:
        transcript = {
            "session": session, "label": cfg["label"], "question": cfg["question"],
            "started_at": datetime.now().isoformat(timespec="seconds"),
            "models": {a.key: {"name": a.name, "hat": a.hat, "model": a.backend.label,
                               "kind": a.backend.kind} for a in agents},
            "rounds": [], "slides": {}, "final_doc": None,
        }

    banner(f"SESSÃO {cfg['label'].upper()}\n{cfg['question']}")
    for round_no in range(len(transcript["rounds"]) + 1, rounds + 1):
        agenda = P.agenda_for(round_no, session)
        print(f"\n--- Rodada {round_no:02d}/{rounds} · {agenda['phase']} ---", flush=True)
        turns = []
        for agent in agents:
            print(f"  · {agent.name} [{agent.backend.label}] pensando...", flush=True)
            try:
                content = agent.backend.chat(
                    agent.system, build_context(session, transcript, round_no, turns, agent))
            except ModelRefusal as e:
                # Falso positivo dos filtros sobre tarefa de saúde pública: registra e segue.
                print(f"    ! fala sinalizada pelos filtros do modelo ({e}); seguindo sem ela", flush=True)
                content = (f"_[Fala não gerada: os filtros de segurança do modelo sinalizaram esta rodada "
                           f"({e}). O debate segue sem esta contribuição.]_")
            turns.append({"agent": agent.key, "name": agent.name, "hat": agent.hat,
                          "model": agent.backend.label, "content": content})
        transcript["rounds"].append({"round": round_no, "agenda": agenda, "turns": turns})

        if round_no in P.MILESTONES:
            banner(f"MARCO · RODADA {round_no:02d} ({cfg['label']})")
            print(render_round_md(session, transcript["rounds"][-1]))
            full = _format_turns(turns)
            prompt = P.SLIDE_SUMMARY_PROMPT.format(
                round_no=round_no, session_label=cfg["label"], slide_role=P.SLIDE_ROLES[round_no])
            previous = "\n\n".join(transcript["slides"].values())
            transcript["slides"][str(round_no)] = orchestrator.backend.chat(
                orchestrator.system,
                f"## Marcos anteriores\n{previous or '(nenhum)'}\n\n## Rodada {round_no} na íntegra\n{full}\n\n{prompt}",
            )
            print(f"\n>>> Resumo para slide:\n{transcript['slides'][str(round_no)]}")

        # O nome exato do modelo remoto só é conhecido depois da primeira chamada.
        for a in agents:
            transcript["models"][a.key]["model"] = a.backend.label
        save(session, transcript)
        write_milestones(session, transcript, agents)

    if rounds == P.TOTAL_ROUNDS and not transcript.get("final_doc"):
        transcript["final_doc"] = compile_final_doc(session, transcript, agents)
        transcript["finished_at"] = datetime.now().isoformat(timespec="seconds")
        save(session, transcript)
        write_milestones(session, transcript, agents)
        (session_dir(session) / cfg["output_file"]).write_text(transcript["final_doc"], encoding="utf-8")

    banner(f"FIM — arquivos em {session_dir(session)}")


def compile_final_doc(session, transcript, agents):
    """Compila o documento final em blocos: uma resposta única excede o limite de saída do modelo."""
    cfg = P.SESSIONS[session]
    by_key = {a.key: a for a in agents}
    orchestrator = by_key["orchestrator"]
    history = "\n\n".join(render_round_md(session, r) for r in transcript["rounds"])
    titles = {"utopia": "A Arquitetura Silenciosa da Imunidade Planetária",
              "distopia": "A Arquitetura Silenciosa da Próxima Pandemia"}
    # Usa os modelos registrados na transcrição: são os que realmente debateram.
    recorded = transcript.get("models", {})
    parts = [P.FINAL_DOC_HEADER.format(
        title=titles[session], session_label=cfg["label"],
        remote_model=recorded.get("architect", {}).get("model") or by_key["architect"].backend.label,
        local_model=recorded.get("risk", {}).get("model") or by_key["risk"].backend.label,
        date=datetime.now().strftime("%d/%m/%Y"))]

    blocks = P.FINAL_DOC_SECTIONS[session]
    for i, (template, max_words) in enumerate(blocks, 1):
        print(f"  · Mediador compilando o documento final ({i}/{len(blocks)})...", flush=True)
        spec = template.format(criteria=P.EVALUATION_CRITERIA[session])
        written = "\n\n".join(parts[1:])
        prompt = (f"# TRANSCRIÇÃO COMPLETA DO DEBATE\n\n{history}\n\n---\n\n{P.FINAL_DOC_INTRO}"
                  f"## Blocos já escritos do documento (não repita este conteúdo)\n"
                  f"{written or '(nenhum — este é o primeiro bloco)'}\n\n---\n\n"
                  f"## BLOCO A ESCREVER AGORA (no máximo {max_words} palavras, siga o template)\n\n{spec}")
        try:
            parts.append(orchestrator.backend.chat(orchestrator.system, prompt).strip())
        except ModelRefusal as e:
            print(f"    ! bloco sinalizado pelos filtros ({e}); seguindo", flush=True)
            parts.append(f"_[Bloco não gerado: os filtros de segurança do modelo o sinalizaram ({e}).]_")
    return "\n\n".join(parts) + "\n"


def load_env():
    """Lê variáveis de distopia_utopia/.env (ex.: ANTHROPIC_API_KEY=sk-ant-...) sem sobrescrever o ambiente."""
    if not ENV_FILE.exists():
        return
    for line in ENV_FILE.read_text(encoding="utf-8").splitlines():
        key, sep, value = line.strip().partition("=")
        if sep and not key.startswith("#"):
            os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def preflight():
    """Confere o acesso ao Claude e o Ollama/modelo local antes de começar; retorna a lista de problemas."""
    problems = []
    if os.getenv("CLAUDE_BACKEND") == "api":
        if not os.getenv("ANTHROPIC_API_KEY", "").startswith("sk-ant-"):
            problems.append(f"CLAUDE_BACKEND=api exige ANTHROPIC_API_KEY=sk-ant-... em {ENV_FILE}")
    elif not ClaudeCodeBackend().exe or not os.path.exists(ClaudeCodeBackend().exe):
        problems.append("Claude Code (comando `claude`) não encontrado. Instale e faça login com sua assinatura.")
    model = os.getenv("LLAMA_MODEL", "llama3.1:8b")
    try:
        import ollama
        host = os.getenv("OLLAMA_HOST", "http://localhost:11434")
        installed = [m.model for m in ollama.Client(host=host).list().models]
        if not any(name == model or name == f"{model}:latest" for name in installed):
            problems.append(f"Modelo local '{model}' não encontrado no Ollama. Rode:  ollama pull {model}")
    except Exception:
        problems.append("Ollama não está respondendo em localhost:11434. Abra o app do Ollama e tente de novo.")
    return problems


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    load_env()
    parser = argparse.ArgumentParser(description="Debate multiagente Distopia / Utopia (20 rodadas).")
    parser.add_argument("--session", choices=["distopia", "utopia", "ambas"], default="ambas")
    parser.add_argument("--rounds", type=int, default=P.TOTAL_ROUNDS,
                        help="Número de rodadas (padrão 20; menos que isso não gera o documento final).")
    parser.add_argument("--resume", action="store_true", help="Continua uma sessão interrompida.")
    parser.add_argument("--mock", action="store_true", help="Backends falsos para testar sem API/Ollama.")
    args = parser.parse_args()

    if not 1 <= args.rounds <= P.TOTAL_ROUNDS:
        parser.error(f"--rounds deve estar entre 1 e {P.TOTAL_ROUNDS}")
    if args.mock:
        global OUTPUT_DIR
        OUTPUT_DIR = BASE_DIR / "outputs_mock"
    else:
        problems = preflight()
        if problems:
            print("Não dá para começar ainda:\n" + "\n".join(f"  - {p}" for p in problems))
            sys.exit(1)
    sessions = ["distopia", "utopia"] if args.session == "ambas" else [args.session]
    for s in sessions:
        run_session(s, mock=args.mock, resume=args.resume, rounds=args.rounds)


if __name__ == "__main__":
    main()
