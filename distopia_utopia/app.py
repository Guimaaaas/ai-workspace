"""Visualizador do debate: streamlit run app.py"""

import json
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

import prompts as P

BASE_DIR = Path(__file__).parent

st.set_page_config(page_title="Distopia / Utopia — Debate Multiagente", layout="wide")
st.title("Experimento Distopia / Utopia")
st.caption('Eixo: "Como salvar o mundo da próxima pandemia da forma mais silenciosa?" — '
           "4 agentes, 20 rodadas, Claude (remoto) + Llama (local via Ollama).")

source = st.sidebar.radio("Execução", ["outputs", "outputs_mock"],
                          format_func=lambda s: "Real" if s == "outputs" else "Mock (teste)")
available = [s for s in P.SESSIONS if (BASE_DIR / source / s / "transcript.json").exists()] or ["utopia"]
session = (available[0] if len(available) == 1 else
           st.sidebar.radio("Sessão", available, format_func=lambda s: P.SESSIONS[s]["label"]))
path = BASE_DIR / source / session / "transcript.json"

if not path.exists():
    st.info(f"Nenhuma execução encontrada em `{path.relative_to(BASE_DIR)}`.\n\n"
            f"Rode: `python debate.py --session {session}`")
    st.stop()

data = json.loads(path.read_text(encoding="utf-8"))
rounds = {r["round"]: r for r in data["rounds"]}
st.subheader(data["label"])
st.markdown(f"**Pergunta central:** {data['question']}")
st.progress(len(rounds) / P.TOTAL_ROUNDS, text=f"{len(rounds)}/{P.TOTAL_ROUNDS} rodadas concluídas")

HAT_COLORS = {"orchestrator": "#2f6fdf", "architect": "#2e9e5b", "risk": "#444444", "scientist": "#c0392b"}


def mermaid(code, height=320):
    components.html(
        f"""<pre class="mermaid">{code}</pre>
        <script type="module">
          import mermaid from "https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs";
          mermaid.initialize({{ startOnLoad: true }});
        </script>""",
        height=height,
    )


def show_round(n):
    rnd = rounds.get(n)
    if not rnd:
        st.warning(f"A Rodada {n} ainda não foi executada.")
        return
    a = rnd["agenda"]
    st.markdown(f"**{a['phase']}** · {a['goal']}  \n*Entregável:* {a['deliverable']}")
    slide = data["slides"].get(str(n))
    if slide:
        with st.container(border=True):
            st.markdown("**Resumo para slide**")
            st.markdown(slide)
    for t in rnd["turns"]:
        color = HAT_COLORS.get(t["agent"], "#888")
        st.markdown(f"<h4 style='border-left:6px solid {color};padding-left:8px'>{t['name']} "
                    f"<small style='color:gray'>· {t['hat']} · {t['model']}</small></h4>",
                    unsafe_allow_html=True)
        st.markdown(t["content"])


tabs = st.tabs(["Arquitetura", "Rodada 1", "Rodada 5", "Rodada 20", "Todas as rodadas", "Plano final"])

with tabs[0]:
    m = data["models"]
    mermaid(f"""flowchart LR
    subgraph Remoto["Modelo remoto — Anthropic API"]
        O["Mediador<br/>{m['orchestrator']['model']}"]
        A["Arquiteto<br/>{m['architect']['model']}"]
        S["Cientista<br/>{m['scientist']['model']}"]
    end
    subgraph Local["Modelo local — Ollama"]
        R["Analista de Riscos<br/>{m['risk']['model']}"]
    end
    O -->|pergunta-desafio| A -->|proposta| R -->|furos| S -->|evidências| O""")
    st.table([{"Persona": v["name"], "Chapéu": v["hat"], "Modelo": v["model"], "Execução": v["kind"]}
              for v in m.values()])
    st.markdown("**Fases:** R1–5 concepção · R6–12 fricção · R13–18 roadmap · R19–20 auditoria e síntese")

for tab, n in zip(tabs[1:4], P.MILESTONES):
    with tab:
        show_round(n)

with tabs[4]:
    if rounds:
        n = st.select_slider("Rodada", options=sorted(rounds), value=max(rounds))
        show_round(n)

with tabs[5]:
    if data.get("final_doc"):
        st.download_button("Baixar plano (.md)", data["final_doc"],
                           file_name=P.SESSIONS[session]["output_file"], mime="text/markdown")
        st.markdown(data["final_doc"])
    else:
        st.info("O documento final é gerado ao fim da Rodada 20.")
