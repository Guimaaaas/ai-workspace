"""Backends de modelo: Claude (remoto, Anthropic API) e Llama (local, Ollama)."""

import json
import os
import random
import shutil
import subprocess
import tempfile


class ModelRefusal(Exception):
    """Os filtros de segurança do modelo sinalizaram esta fala. Não deve ser repetida nem reformulada."""


class ClaudeCodeBackend:
    """Modelo remoto via Claude Code (`claude -p`), usando a assinatura logada — sem chave de API.

    Roda sem ferramentas, sem MCP e numa pasta temporária, para que o agente apenas converse.
    """

    kind = "remoto"

    def __init__(self, model=None, effort=None):
        self.exe = shutil.which("claude") or os.path.expanduser("~/.local/bin/claude.exe")
        self.model = model or os.getenv("CLAUDE_MODEL", "opus")
        self.effort = effort or os.getenv("CLAUDE_EFFORT", "medium")
        self.workdir = tempfile.mkdtemp(prefix="debate_claude_")
        # Sem ANTHROPIC_API_KEY no ambiente o Claude Code usa o login da assinatura.
        self.env = {k: v for k, v in os.environ.items() if k != "ANTHROPIC_API_KEY"}
        self.resolved_model = None

    @property
    def label(self):
        return f"Claude ({self.resolved_model or self.model}, assinatura)"

    def chat(self, system, user, max_tokens=None, retries=2):
        sp_file = os.path.join(self.workdir, "system_prompt.txt")
        with open(sp_file, "w", encoding="utf-8") as f:
            f.write(system)
        cmd = [self.exe, "-p", "--system-prompt-file", sp_file, "--tools", "", "--model", self.model,
               "--effort", self.effort, "--output-format", "json", "--no-session-persistence",
               "--strict-mcp-config"]
        for attempt in range(retries + 1):
            proc = subprocess.run(cmd, input=user, capture_output=True, text=True, encoding="utf-8",
                                  cwd=self.workdir, env=self.env, timeout=900)
            try:
                data = json.loads(proc.stdout)
            except json.JSONDecodeError:
                data = {"is_error": True, "result": (proc.stderr or proc.stdout).strip()[:500]}
            result = data.get("result") or ""
            # Fala sinalizada pelos filtros: não insistir nem reformular — registrar e seguir.
            if "safeguards flagged" in result or "Details: `[" in result:
                raise ModelRefusal(result.split("Details: ")[-1].strip().strip("`") or "sinalizada")
            if not data.get("is_error") and result:
                models = [m for m in data.get("modelUsage", {}) if "haiku" not in m]
                if models:
                    self.resolved_model = models[0]
                if data.get("stop_reason") == "refusal":
                    return "_[O modelo recusou esta fala. O debate segue com os demais agentes.]_"
                return data["result"].strip()
            if attempt == retries:
                raise RuntimeError(f"Claude Code falhou: {data.get('result')}")


class ClaudeBackend:
    """Modelo remoto via Anthropic SDK (cobrança da API, separada da assinatura).
    Use com CLAUDE_BACKEND=api e ANTHROPIC_API_KEY."""

    kind = "remoto"

    def __init__(self, model=None, effort=None):
        import anthropic

        self._anthropic = anthropic
        self.client = anthropic.Anthropic(max_retries=4)
        self.model = model or os.getenv("CLAUDE_MODEL", "claude-opus-5")
        self.effort = effort or os.getenv("CLAUDE_EFFORT", "medium")

    @property
    def label(self):
        return f"Claude ({self.model})"

    def chat(self, system, user, max_tokens=8000):
        response = self.client.beta.messages.create(
            model=self.model,
            max_tokens=max_tokens,
            system=system,
            messages=[{"role": "user", "content": user}],
            thinking={"type": "adaptive"},
            output_config={"effort": self.effort},
            # Se o classificador de segurança recusar, a API reexecuta no modelo de fallback recomendado.
            betas=["server-side-fallback-2026-07-01"],
            fallbacks="default",
        )
        if response.stop_reason == "refusal":
            return "_[O modelo recusou esta fala. O debate segue com os demais agentes.]_"
        text = "".join(b.text for b in response.content if b.type == "text").strip()
        if response.stop_reason == "max_tokens":
            text += "\n\n_[fala truncada por limite de tokens]_"
        return text


class OllamaBackend:
    """Modelo local (Meta Llama 3 por padrão) servido pelo Ollama em localhost:11434."""

    kind = "local"

    def __init__(self, model=None, host=None, num_ctx=None):
        import ollama

        self.model = model or os.getenv("LLAMA_MODEL", "llama3.1:8b")
        self.client = ollama.Client(host=host or os.getenv("OLLAMA_HOST", "http://localhost:11434"))
        self.num_ctx = int(num_ctx or os.getenv("LLAMA_NUM_CTX", "8192"))

    @property
    def label(self):
        return f"Llama local ({self.model})"

    def chat(self, system, user, max_tokens=1200):
        response = self.client.chat(
            model=self.model,
            messages=[{"role": "system", "content": system}, {"role": "user", "content": user}],
            options={"num_ctx": self.num_ctx, "num_predict": max_tokens, "temperature": 0.7},
        )
        return response["message"]["content"].strip()


class MockBackend:
    """Backend offline para testar o pipeline sem chave de API nem Ollama (`--mock`)."""

    def __init__(self, name, kind):
        self.name = name
        self.kind = kind
        self.model = f"mock-{name}"

    @property
    def label(self):
        return f"Mock ({self.name})"

    def chat(self, system, user, max_tokens=1000):
        first_line = next((l for l in user.splitlines() if l.startswith("## RODADA")), "## RODADA ?")
        ideas = ["sensores de esgoto", "nuvem de saúde", "identidade digital", "seguro vinculado",
                 "filtragem de ar", "biomanufatura aberta", "auditoria pública"]
        return (f"[{self.name}] {first_line.removeprefix('## ')}: proposta sobre "
                f"{random.choice(ideas)} e {random.choice(ideas)}.\n\n- ponto A\n- ponto B")
