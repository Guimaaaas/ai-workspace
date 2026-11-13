"""Chão Público: chat com agentes que documentam imóveis ociosos e a função social deles.

streamlit run app.py
"""

import json
import logging
from datetime import datetime

import anthropic
import pandas as pd
import streamlit as st

import agentes
import exportar
import fontes
import historico

logging.getLogger("fontTools").setLevel(logging.ERROR)  # avisos de fonte do PDF, sem efeito no resultado
st.set_page_config(page_title="Chão Público", page_icon="🏚️", layout="wide")

ETAPAS = {
    "pesquisador": "🔎 Pesquisador: consultando bases públicas",
    "redator": "✍️ Redator: escrevendo o laudo",
    "revisor": "🧐 Revisor: conferindo cada número",
    "correcao": "✍️ Redator: corrigindo o que o revisor apontou",
    "conservador": "✍️ Redator: retirando o que não pôde ser confirmado",
    "lai": "📨 Escrevendo os pedidos de acesso à informação",
}
ROTULOS_FERRAMENTA = {
    "web_search": "busca na web", "web_fetch": "lendo página", "ler_pagina": "lendo página (leitura própria)",
    "geocodificar_endereco": "geocodificando", "suscetibilidade_inundacao": "cartas de inundação (SGB)",
    "contratos_federais": "contratos federais (Compras.gov.br)", "ckan_buscar": "dados abertos (CKAN)",
    "ckan_ler_recurso": "lendo dados abertos", "iptu_recife": "IPTU do Recife",
    "iptu_recife_proximos": "IPTU do Recife (lotes próximos)", "consultar_cnpj": "CNPJ", "municipio_ibge": "IBGE",
    "portal_transparencia": "Portal da Transparência", "registrar_evidencia": "evidência registrada",
    "imoveis_uniao_proximos": "cadastro da SPU", "dados_gov_buscar": "catálogo dados.gov.br",
    "dados_gov_conjunto": "conjunto dados.gov.br",
}

ss = st.session_state
ss.setdefault("conversa", [])   # [{papel, texto, resultado?}]
ss.setdefault("dossie", [])
ss.setdefault("documento", None)
ss.setdefault("custo_total", 0.0)
ss.setdefault("chave_ok", None)
ss.setdefault("id_laudo", None)      # laudo desta consulta no histórico (ajustes atualizam o mesmo)
ss.setdefault("coordenadas", None)
ENV = fontes.ler_env()  # chaves locais de quem roda o app (chao_publico/.env, fora do Git)
DEV = ENV.get("MODO_DESENVOLVEDOR") == "1"  # mostra revisões e notas internas; a população não vê

# ---------------------------------------------------------------- barra lateral
with st.sidebar:
    st.header("🏚️ Chão Público")
    st.caption("Imóvel ocioso vira prova: quanto o abandono custa, se a lei está sendo aplicada e se o imóvel "
               "pode cumprir função social.")
    laudados = historico.listar()
    tela = st.radio("Tela", ["consulta", "laudados"], horizontal=True, label_visibility="collapsed",
                    format_func={"consulta": "Consulta", "laudados": f"Imóveis laudados ({len(laudados)})"}.get)

    # o modo assinatura só existe com MODO_ASSINATURA=1 no .env local: um app publicado nunca o mostra
    usar_assinatura = ENV.get("MODO_ASSINATURA") == "1" and st.radio(
        "Como rodar os agentes", ["assinatura", "chave"], horizontal=True,
        format_func={"assinatura": "Minha assinatura (testes)", "chave": "Chave da API"}.get) == "assinatura"
    chave = None
    if usar_assinatura:
        st.info("Usando o login do seu Claude Code. Não gasta crédito de API, mas consome o limite da assinatura.")
    else:
        chave = st.text_input("Sua chave da API da Anthropic", type="password", placeholder="sk-ant-…",
                              help="Fica só na memória desta sessão do navegador. Não é gravada em disco nem "
                                   "enviada a nenhum outro serviço. Crie uma em platform.claude.com.")
        if chave and ss.get("chave_validada") != chave:
            with st.spinner("conferindo a chave…"):
                ok, msg = agentes.validar_chave(chave)
            ss.chave_validada, ss.chave_ok, ss.chave_msg = chave, ok, msg
        if chave and ss.chave_ok is not None:
            (st.success if ss.chave_ok else st.error)(ss.chave_msg)
    pronto = usar_assinatura or bool(chave and ss.chave_ok)

    with st.expander("Chaves das bases públicas (opcionais)", expanded=False):
        chave_dados_gov = st.text_input("Token do dados.gov.br", type="password", value=ENV.get("DADOS_GOV_TOKEN", ""),
                                        help="dados.gov.br > Entrar com gov.br (perfil Consumidor) > Minha Conta.")
        chave_transp = st.text_input("Chave do Portal da Transparência", type="password",
                                     value=ENV.get("PORTAL_TRANSPARENCIA_CHAVE", ""),
                                     help="Gratuita: portaldatransparencia.gov.br/api-de-dados/cadastrar-email.")
        if fontes.ARQUIVO_SPU.exists():
            st.caption("✅ Cadastro georreferenciado da SPU carregado.")
        else:
            st.caption(f"⚠️ Sem o cadastro da SPU. [Baixe no navegador]({fontes.URL_SPU}) e salve como "
                       "`chao_publico/dados/spu_pontos.geojson`.")
        st.caption("Sem essas chaves, o agente usa as outras bases.")
    modelo = st.selectbox("Modelo", list(agentes.MODELOS), format_func=agentes.MODELOS.get)
    esforco = st.select_slider("Profundidade", ["low", "medium", "high"], value="medium",
                               format_func={"low": "rápida", "medium": "padrão", "high": "minuciosa"}.get,
                               help="Mais profundidade = mais buscas e mais custo.")
    # para a população a revisão é sempre interna e com correção; só quem desenvolve pode desligar
    corrigir = st.toggle("[dev] Corrigir automaticamente após a revisão", value=True) if DEV else True

    st.divider()
    st.metric("Custo equivalente na API (não cobrado)" if usar_assinatura else "Custo estimado nesta sessão",
              f"US$ {ss.custo_total:.2f}")
    st.caption(f"{len(ss.dossie)} evidências no dossiê")
    if st.button("🧹 Nova consulta (limpa tudo)", width="stretch"):
        for k in ("conversa", "dossie", "documento", "id_laudo", "coordenadas"):
            ss.pop(k)
        ss.custo_total = 0.0
        st.rerun()
    st.caption("Protótipo acadêmico. O documento gerado é ponto de partida: confira cada fonte antes de protocolar.")


# ---------------------------------------------------------------- utilidades
def novo_cliente():
    return agentes.assinatura.Assinatura() if usar_assinatura else anthropic.Anthropic(api_key=chave, max_retries=4)


def com_tratamento(acao, atual):
    """Roda `acao()` mostrando erros de forma legível. Devolve o resultado ou None."""
    def falhou(msg):
        if atual.get("status"):
            atual["status"].update(state="error")
        st.error(msg)
    try:
        return acao()
    except agentes.Recusa as e:
        falhou(f"O modelo recusou esta tarefa: {e}")
    except anthropic.RateLimitError:
        falhou("Limite de uso da sua chave atingido. Espere um pouco ou use um modelo mais barato.")
    except anthropic.APIStatusError as e:
        falhou(f"Erro da API da Anthropic ({e.status_code}): {e.message}")
    except anthropic.APIConnectionError:
        falhou("Sem conexão com a API da Anthropic.")
    except Exception as e:  # modo assinatura: limite atingido, login vencido, Claude Code ausente…
        if not usar_assinatura:
            raise
        falhou(f"Falha no modo assinatura: {e}\n\nSe for login, rode `claude` no terminal e entre de novo.")
    return None


def painel_de_etapas():
    """Cria (atual, ao_etapa, ao_evento) para mostrar o trabalho dos agentes em tempo real."""
    atual = {"status": None}

    def ao_etapa(nome):
        if atual["status"]:
            atual["status"].update(state="complete", expanded=False)
        atual["status"] = st.status(ETAPAS[nome], expanded=True)

    def ao_evento(tipo, nome, dados):
        box = atual["status"]
        rot = ROTULOS_FERRAMENTA.get(nome, nome)
        if tipo in ("web", "ferramenta"):
            if nome == "registrar_evidencia":
                box.write(f"📌 {dados.get('afirmacao', '')}" + (f" — **{dados['valor']}**" if dados.get("valor") else ""))
            else:
                detalhe = dados.get("query") or dados.get("url") or dados.get("endereco") or dados.get("termo") or ""
                if not detalhe and nome == "contratos_federais":
                    detalhe = ", ".join(dados.get("palavras_chave") or [])
                box.write(f"· {rot}: `{str(detalhe)[:120]}`" if detalhe else f"· {rot}")
        elif tipo == "resultado" and dados["erro"]:
            box.write(f"  ⚠️ {rot} falhou: {dados['resumo'][:160]}")
        elif tipo == "aviso":
            box.warning(f"{nome}: {dados}")
        elif tipo == "fim":
            box.write(f"**{dados['novas_evidencias']} evidências novas no dossiê.**")

    return atual, ao_etapa, ao_evento


@st.cache_data(show_spinner=False, max_entries=50)
def pdf_de(texto_md):
    return exportar.laudo_pdf(texto_md)


def botoes_download(texto_md, nome, chave_widget, rotulo="laudo"):
    data = datetime.now().strftime("%Y%m%d-%H%M")
    c1, c2 = st.columns(2)
    try:
        c1.download_button(f"⬇️ Baixar {rotulo} (PDF)", pdf_de(texto_md), f"{nome}-{data}.pdf", "application/pdf",
                           key=f"pdf_{chave_widget}", width="stretch", type="primary")
    except Exception as e:  # o PDF nunca pode derrubar a tela; o .md continua disponível
        c1.caption(f"Não foi possível gerar o PDF ({type(e).__name__}). Use o .md.")
    c2.download_button(f"⬇️ Baixar {rotulo} (.md)", texto_md, f"{nome}-{data}.md", "text/markdown",
                       key=f"md_{chave_widget}", width="stretch")


def secao_pedidos_lai(res, chave_widget):
    """Pedidos de LAI do laudo: mostra se já existem, ou oferece gerar."""
    if res.get("pedidos_lai"):
        with st.expander("📨 Pedidos de acesso à informação (LAI), prontos para protocolar", expanded=False):
            st.markdown(res["pedidos_lai"])
            botoes_download(res["pedidos_lai"], "pedidos-lai-chao-publico", f"lai_{chave_widget}", "pedidos")
        return
    if not pronto:
        return
    if st.button("📨 Gerar os pedidos de LAI que fecham as lacunas do laudo", key=f"gerar_lai_{chave_widget}"):
        atual, ao_etapa, ao_evento = painel_de_etapas()
        ctx = fontes.Contexto(chave_transp, list(res.get("dossie") or []), chave_dados_gov)

        def gerar():
            ao_etapa("lai")
            return agentes.gerar_pedidos_lai(novo_cliente(), modelo, res["documento"], ctx, ao_evento, esforco)
        saida = com_tratamento(gerar, atual)
        if saida:
            res["pedidos_lai"], custo = saida
            ss.custo_total += custo
            if res.get("id_historico"):
                historico.anexar_pedidos_lai(res["id_historico"], res["pedidos_lai"])
            st.rerun()


def mostrar_resultado(res, chave_widget):
    status = res.get("status", "aprovado" if res.get("veredito") == "APROVADO" else "pendente")
    if DEV and res.get("revisoes") is not None:  # quem desenvolve vê o veredito cru e todas as revisões
        rotulo = {"aprovado": "aprovado", "conservador": "pendente → versão conservadora", "pendente": "pendente"}
        st.info(f"[dev] veredito: **{rotulo.get(status, status)}** · rodadas de correção: "
                f"{res.get('rodadas_correcao', '?')}")
    elif status == "aprovado":
        st.caption("✅ Laudo revisado: cada número foi conferido com a fonte citada.")
    elif status == "conservador":
        st.caption("✅ Laudo revisado. Pontos que não puderam ser confirmados nas fontes foram retirados.")
    else:
        st.caption("⚠️ Revisão incompleta: confira as fontes antes de usar o laudo.")
    st.markdown(res["documento"])
    botoes_download(res["documento"], "laudo-chao-publico", chave_widget)
    secao_pedidos_lai(res, chave_widget)
    dossie = res.get("dossie") or []
    with st.expander(f"Dossiê: {len(dossie)} evidências"):
        if dossie:
            st.dataframe(pd.DataFrame(dossie).reindex(columns=["id", "afirmacao", "valor", "periodo", "fonte",
                                                                "tipo", "url"]),
                         hide_index=True, width="stretch", column_config={"url": st.column_config.LinkColumn("url")})
            st.download_button("⬇️ Baixar dossiê (.json)", json.dumps(dossie, ensure_ascii=False, indent=2),
                               "dossie-chao-publico.json", "application/json", key=f"dos_{chave_widget}")
    if DEV:
        for i, rev in enumerate(res.get("revisoes") or [], 1):
            with st.expander(f"[dev] Revisão {i}" + (" (última)" if i == len(res["revisoes"]) > 1 else "")):
                st.markdown(rev)
        if res.get("resumo_pesquisa"):
            with st.expander("[dev] Notas do pesquisador"):
                st.markdown(res["resumo_pesquisa"])
    if res.get("tokens"):
        t = res["tokens"]
        st.caption(f"Custo estimado: US$ {res['custo_usd']:.2f} · "
                   f"{t['entrada'] + t['cache_lido'] + t['cache_gravado']:,} tokens de entrada · "
                   f"{t['saida']:,} de saída · {t['buscas_web']} buscas na web")


# ---------------------------------------------------------------- tela: imóveis laudados
if tela == "laudados":
    st.title("Imóveis laudados")
    if not laudados:
        st.info("Nenhum laudo salvo ainda. Cada consulta concluída aparece aqui e no mapa.")
        st.stop()
    pontos = pd.DataFrame([{"lat": r["lat"], "lon": r["lon"]} for r in laudados if r.get("lat") and r.get("lon")])
    if not pontos.empty:
        st.map(pontos, latitude="lat", longitude="lon", size=40, zoom=12)
    st.caption(f"{len(laudados)} laudos · {len(pontos)} no mapa. Ficam salvos neste computador "
               "(`chao_publico/dados/laudos/`).")
    for r in laudados:
        with st.expander(f"**{r['titulo']}** · {r['data']}" + (" · 📨 com pedidos de LAI" if r.get("pedidos_lai") else "")):
            st.markdown(r["documento"])
            botoes_download(r["documento"], "laudo-chao-publico", f"h_{r['id']}")
            if r.get("pedidos_lai"):
                st.divider()
                st.markdown(r["pedidos_lai"])
                botoes_download(r["pedidos_lai"], "pedidos-lai-chao-publico", f"hl_{r['id']}", "pedidos")
            if st.button("Abrir na consulta (para ajustar ou gerar pedidos de LAI)", key=f"abrir_{r['id']}"):
                res = {"documento": r["documento"], "dossie": r.get("dossie") or [], "status": r.get("status"),
                       "pedidos_lai": r.get("pedidos_lai"), "id_historico": r["id"]}
                ss.conversa = [{"papel": "user", "texto": r.get("pedido") or r["titulo"]},
                               {"papel": "assistant", "texto": r["documento"], "resultado": res}]
                ss.dossie, ss.documento, ss.id_laudo = list(res["dossie"]), r["documento"], r["id"]
                ss.coordenadas = (r["lat"], r["lon"]) if r.get("lat") else None
                st.info("Laudo aberto. Volte para a tela **Consulta** na barra lateral.")
    st.stop()

# ---------------------------------------------------------------- tela: consulta
if not ss.conversa:
    st.title("Chão Público")
    st.markdown(
        "Diga qual **imóvel ocioso** você quer documentar: prédio ou terreno **público** sem uso, ou imóvel "
        "**privado** abandonado. Três agentes trabalham em sequência:\n\n"
        "1. **Pesquisador** consulta bases públicas (cadastro da SPU, IPTU municipal, cartas de inundação do Serviço "
        "Geológico do Brasil, contratos federais, dados abertos, Portal da Transparência, Diário Oficial, TCU, "
        "imprensa) e registra cada fato com a fonte;\n"
        "2. **Redator** escreve o laudo: quanto o abandono custa ao poder público, a situação fiscal (dívida de "
        "IPTU, IPTU progressivo e demais instrumentos da função social) e a aptidão do imóvel para uma função "
        "social. O uso (moradia, abrigo, creche…) fica a cargo do órgão responsável;\n"
        "3. **Revisor** confere cada número contra a fonte e devolve para correção se precisar.\n\n"
        "No fim, você baixa o laudo em PDF e pode gerar os **pedidos de acesso à informação (LAI)** prontos "
        "para protocolar.\n\n"
        "Exemplos: *Prédio do antigo INSS na Av. Dantas Barreto, Santo Antônio, Recife (PE), vazio há anos.* · "
        "*Prédio privado abandonado na Rua da Concórdia, São José, Recife (PE): o IPTU progressivo está sendo cobrado?*"
    )

for i, m in enumerate(ss.conversa):
    with st.chat_message(m["papel"]):
        if m.get("resultado"):
            mostrar_resultado(m["resultado"], i)
        else:
            st.markdown(m["texto"])

pedido = st.chat_input("Descreva o imóvel (endereço, nome do prédio, dono…) ou peça um ajuste no laudo",
                       disabled=not pronto)
if not pronto and not ss.conversa:
    st.info("Cole sua chave da API da Anthropic na barra lateral para começar.")

if pedido:
    ss.conversa.append({"papel": "user", "texto": pedido})
    with st.chat_message("user"):
        st.markdown(pedido)

    with st.chat_message("assistant"):
        ctx = fontes.Contexto(chave_transp, ss.dossie, chave_dados_gov)
        atual, ao_etapa, ao_evento = painel_de_etapas()
        res = com_tratamento(lambda: agentes.executar_consulta(
            novo_cliente(), modelo, pedido, ctx, ao_etapa, ao_evento, documento_anterior=ss.documento,
            corrigir=corrigir, esforco=esforco), atual)
        if res:
            atual["status"].update(state="complete", expanded=False)
            res["dossie"] = list(ss.dossie)
            ss.coordenadas = ctx.coordenadas or ss.coordenadas
            ss.id_laudo = historico.salvar(res, pedido, ss.coordenadas, modelo, id_existente=ss.id_laudo)
            res["id_historico"] = ss.id_laudo
            ss.documento = res["documento"]
            ss.custo_total += res["custo_usd"]
            ss.conversa.append({"papel": "assistant", "texto": res["documento"], "resultado": res})
            mostrar_resultado(res, len(ss.conversa) - 1)
