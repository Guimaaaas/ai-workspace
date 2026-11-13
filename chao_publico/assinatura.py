"""Modo assinatura: roda os agentes pelo Claude Agent SDK, com o login do Claude Code de quem roda o app.

Só para testes locais. A assinatura é pessoal: um app publicado precisa que cada pessoa use a própria chave.
As ferramentas de fontes.py entram como um servidor MCP dentro do próprio processo; a busca e a leitura na
web são as do Claude Code (WebSearch, WebFetch).
"""

import asyncio
import os
import tempfile

from claude_agent_sdk import (AssistantMessage, ClaudeAgentOptions, ResultMessage, TextBlock, ToolUseBlock,
                              create_sdk_mcp_server, query, tool)

import fontes

SERVIDOR = "fontes"
WEB = {"web_search": "WebSearch", "web_fetch": "WebFetch"}
_pasta = tempfile.mkdtemp(prefix="chao_publico_")


class Assinatura:
    """Marcador passado no lugar do cliente da API."""


def _servidor(proprias, ctx, ao_evento):
    ferramentas = []
    for f in proprias:
        def fazer(nome):
            async def rodar(args):
                saida, erro = fontes.executar(nome, args, ctx)
                ao_evento("resultado", nome, {"erro": erro, "resumo": saida[:300]})
                return {"content": [{"type": "text", "text": saida}], "is_error": erro}
            return rodar
        ferramentas.append(tool(f["name"], f["description"], f["input_schema"])(fazer(f["name"])))
    return create_sdk_mcp_server(SERVIDOR, tools=ferramentas)


async def _rodar(modelo, agente, mensagem, ctx, uso, ao_evento, esforco, max_turnos):
    web = [WEB[t["name"]] for t in agente.ferramentas if t.get("name") in WEB]
    proprias = [t for t in agente.ferramentas if "input_schema" in t]  # só as ferramentas deste agente
    mcp = {SERVIDOR: _servidor(proprias, ctx, ao_evento)} if proprias else {}
    permitidas = web + [f"mcp__{SERVIDOR}__{t['name']}" for t in proprias]
    opcoes = ClaudeAgentOptions(
        system_prompt=agente.system, model=modelo, effort=esforco, max_turns=max_turnos,
        tools=web,                      # nenhuma ferramenta embutida além da web (sem Bash, sem arquivos)
        allowed_tools=permitidas, permission_mode="dontAsk", mcp_servers=mcp, strict_mcp_config=True,
        setting_sources=[],             # não carrega CLAUDE.md nem configurações de quem roda
        cwd=_pasta, env={"ANTHROPIC_API_KEY": ""})

    texto, resultado = "", None
    async for msg in query(prompt=mensagem, options=opcoes):
        if isinstance(msg, AssistantMessage):
            for b in msg.content:
                if isinstance(b, TextBlock) and b.text.strip():
                    texto = b.text
                elif isinstance(b, ToolUseBlock) or type(b).__name__ == "ServerToolUseBlock":
                    nome = b.name.removeprefix(f"mcp__{SERVIDOR}__")
                    nome = {"WebSearch": "web_search", "WebFetch": "web_fetch"}.get(nome, nome)
                    ao_evento("web" if nome in WEB else "ferramenta", nome, b.input or {})
        elif isinstance(msg, ResultMessage):
            resultado = msg
    if resultado is None:
        raise RuntimeError("o Claude Code terminou sem resposta")
    uso.custo_equivalente += resultado.total_cost_usd or 0
    u = resultado.usage or {}
    uso.entrada += u.get("input_tokens", 0)
    uso.saida += u.get("output_tokens", 0)
    uso.cache_lido += u.get("cache_read_input_tokens", 0)
    uso.cache_gravado += u.get("cache_creation_input_tokens", 0)
    if resultado.is_error:
        detalhe = resultado.result or "; ".join(map(str, resultado.errors or [])) or resultado.subtype
        if resultado.subtype == "error_max_turns":
            ao_evento("aviso", "limite de passos", f"o agente parou após {max_turnos} passos")
            return texto
        raise RuntimeError(f"Claude Code: {detalhe}")
    return resultado.result or texto


def rodar_agente(modelo, agente, mensagem, ctx, uso, ao_evento, esforco=None, max_turnos=40):
    return asyncio.run(_rodar(modelo, agente, mensagem, ctx, uso, ao_evento, esforco or agente.esforco, max_turnos))
