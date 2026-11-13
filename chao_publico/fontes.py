"""Ferramentas do agente pesquisador: consultas a bases públicas brasileiras.

Cada ferramenta tem um esquema (enviado ao modelo) e uma função Python (executada aqui, no
computador de quem roda o app). Todas são só leitura (GET). Respostas longas são cortadas.
"""

import json
import math
import re
import time
from datetime import datetime
from pathlib import Path

import requests

UA = "ChaoPublico/0.1 (prototipo academico; dados publicos)"
TIMEOUT = 40
LIMITE_CARACTERES = 12000
PASTA_DADOS = Path(__file__).parent / "dados"
ARQUIVO_SPU = PASTA_DADOS / "spu_pontos.geojson"
URL_SPU = "https://drive.spu.gestao.gov.br/index.php/s/xbmeGFJpNDigXEm/download"

_http = requests.Session()
_http.headers["User-Agent"] = UA
_ultimo_nominatim = [0.0]
_cache_spu = {}


class Contexto:
    """Estado compartilhado de uma consulta: o dossiê de evidências e as chaves opcionais."""

    def __init__(self, chave_transparencia=None, dossie=None, chave_dados_gov=None):
        self.chave_transparencia = (chave_transparencia or "").strip() or None
        self.chave_dados_gov = (chave_dados_gov or "").strip() or None
        self.dossie = dossie if dossie is not None else []
        self.coordenadas = None  # (lat, lon) do imóvel, para o mapa de imóveis laudados


def _corta(obj):
    texto = obj if isinstance(obj, str) else json.dumps(obj, ensure_ascii=False, default=str)
    if len(texto) > LIMITE_CARACTERES:
        texto = texto[:LIMITE_CARACTERES] + f"\n…[cortado: {len(texto)} caracteres no total]"
    return texto


def _get(url, params=None, headers=None):
    r = _http.get(url, params=params, headers=headers, timeout=TIMEOUT)
    return r


# ---------------------------------------------------------------- funções

def geocodificar_endereco(endereco):
    espera = 1.1 - (time.time() - _ultimo_nominatim[0])  # política do Nominatim: 1 req/s
    if espera > 0:
        time.sleep(espera)
    _ultimo_nominatim[0] = time.time()
    r = _get("https://nominatim.openstreetmap.org/search",
             {"q": endereco, "format": "json", "countrycodes": "br", "limit": 5, "addressdetails": 1})
    r.raise_for_status()
    itens = [{"nome": i.get("display_name"), "lat": float(i["lat"]), "lon": float(i["lon"]),
              "tipo": f"{i.get('class')}/{i.get('type')}", "osm": f"https://www.openstreetmap.org/{i['osm_type']}/{i['osm_id']}"}
             for i in r.json()]
    return {"fonte": "OpenStreetMap / Nominatim", "url": r.url, "resultados": itens}


def suscetibilidade_inundacao(lat, lon, raio_m=100):
    raio_m = max(20, min(float(raio_m), 2000))
    dlat = raio_m / 111320
    dlon = raio_m / (111320 * max(math.cos(math.radians(lat)), 0.01))
    bbox = f"{lon - dlon},{lat - dlat},{lon + dlon},{lat + dlat}"
    saida = {"fonte": "Serviço Geológico do Brasil (SGB/CPRM), GeoServer gestao-territorial",
             "aviso": (f"Camadas que intersectam um quadrado de {2 * raio_m:.0f} m de lado em torno do ponto. "
                       "Suscetibilidade é modelagem regional (escala de carta), não laudo do lote: "
                       "serve para triagem e precisa de vistoria."),
             "camadas": {}}
    for camada in ("suscet_inundacao", "risco_geologico"):
        r = _get("https://geoservicos.sgb.gov.br/geoserver/ows",
                 {"service": "WFS", "version": "1.0.0", "request": "GetFeature",
                  "typeName": f"gestao-territorial:{camada}", "outputFormat": "application/json",
                  "maxFeatures": 20, "bbox": bbox})
        r.raise_for_status()
        feats = r.json().get("features", [])
        saida["camadas"][camada] = {"url": r.url, "n": len(feats),
                                    "feicoes": [f.get("properties", {}) for f in feats]}
    return saida


def contratos_federais(data_inicio, data_fim, codigo_orgao=None, codigo_unidade_gestora=None,
                       palavras_chave=None, max_paginas=3):
    if not (codigo_orgao or codigo_unidade_gestora):
        raise ValueError("informe codigo_orgao ou codigo_unidade_gestora")
    params = {"tamanhoPagina": 500, "dataVigenciaInicialMin": data_inicio,
              "dataVigenciaInicialMax": data_fim}
    if codigo_orgao:
        params["codigoOrgao"] = codigo_orgao
    if codigo_unidade_gestora:
        params["codigoUnidadeGestora"] = codigo_unidade_gestora
    chaves = [p.lower() for p in (palavras_chave or []) if p.strip()]
    url_base = "https://dadosabertos.compras.gov.br/modulo-contratos/1_consultarContratos"
    achados, total, urls = [], 0, []
    for pagina in range(1, int(max(1, min(max_paginas, 10))) + 1):
        r = _get(url_base, {**params, "pagina": pagina})
        urls.append(r.url)
        if r.status_code == 404:  # a API devolve 404 quando não há registro
            break
        r.raise_for_status()
        dados = r.json()
        total = dados.get("totalRegistros", total)
        for c in dados.get("resultado", []):
            texto = f"{c.get('objeto') or ''} {c.get('informacoesComplementares') or ''}".lower()
            if chaves and not any(k in texto for k in chaves):
                continue
            achados.append({k: c.get(k) for k in (
                "numeroContrato", "nomeUnidadeGestora", "codigoUnidadeGestora", "nomeRazaoSocialFornecedor",
                "niFornecedor", "objeto", "dataVigenciaInicial", "dataVigenciaFinal", "valorGlobal",
                "valorParcela", "numeroParcelas", "processo", "numeroControlePncpCompra")})
        if not dados.get("paginasRestantes"):
            break
    return {"fonte": "Compras.gov.br — Dados Abertos, módulo contratos", "urls_consultadas": urls,
            "total_registros_no_periodo": total, "filtro_palavras": chaves,
            "n_achados": len(achados), "contratos": achados[:60]}


_PORTAL_CKAN = re.compile(r"^https://dados\.[a-z0-9.-]+\.gov\.br$")


def _portal(portal):
    portal = portal.strip().rstrip("/")
    if not portal.startswith("http"):
        portal = "https://" + portal
    portal = portal.replace(":443", "")
    if not _PORTAL_CKAN.match(portal):
        raise ValueError("portal precisa ser um CKAN público no formato https://dados.<ente>.gov.br")
    return portal


def ckan_buscar(portal, termo, linhas=8):
    portal = _portal(portal)
    r = _get(f"{portal}/api/3/action/package_search", {"q": termo, "rows": int(min(linhas, 20))})
    r.raise_for_status()
    res = r.json()["result"]
    return {"fonte": f"CKAN {portal}", "url": r.url, "total": res["count"], "conjuntos": [
        {"titulo": p.get("title"), "pagina": f"{portal}/dataset/{p.get('name')}",
         "atualizado": p.get("metadata_modified"), "orgao": (p.get("organization") or {}).get("title"),
         "recursos": [{"id": rc["id"], "nome": rc.get("name"), "formato": rc.get("format"),
                       "url": rc.get("url"), "consultavel": bool(rc.get("datastore_active"))}
                      for rc in p.get("resources", [])]}
        for p in res["results"]]}


def ckan_ler_recurso(portal, recurso_id, filtro=None, limite=30):
    portal = _portal(portal)
    params = {"resource_id": recurso_id, "limit": int(min(limite, 100))}
    if filtro:
        params["q"] = filtro
    r = _get(f"{portal}/api/3/action/datastore_search", params)
    if r.status_code != 200:
        raise RuntimeError(f"datastore indisponível para este recurso (HTTP {r.status_code}); "
                           "use web_fetch na URL de download do recurso")
    res = r.json()["result"]
    return {"fonte": f"CKAN {portal} (datastore)", "url": r.url, "total": res.get("total"),
            "campos": [f["id"] for f in res.get("fields", [])], "registros": res.get("records", [])}


_RECIFE = "https://dados.recife.pe.gov.br"
_cache_iptu = {}


def _num(v):
    try:
        return float(str(v).replace(".", "").replace(",", ".")) if isinstance(v, str) else float(v)
    except (TypeError, ValueError):
        return None


def _recursos_iptu():
    """Mapa ano -> id do recurso de IPTU no CKAN do Recife (um CSV por ano)."""
    if "recursos" not in _cache_iptu:
        r = _get(f"{_RECIFE}/api/3/action/package_show", {"id": "imposto-predial-e-territorial-urbano-iptu"})
        r.raise_for_status()
        _cache_iptu["recursos"] = {int(m.group()): rc["id"] for rc in r.json()["result"]["resources"]
                                   if rc.get("datastore_active") and (m := re.search(r"20\d\d", rc.get("name", "")))}
    return _cache_iptu["recursos"]


def iptu_recife(logradouro, numero=None, anos=None):
    """Lançamentos de IPTU do Recife por endereço, ano a ano (dados abertos da prefeitura)."""
    disponiveis = sorted(_recursos_iptu(), reverse=True)
    anos = sorted({int(a) for a in anos}, reverse=True) if anos else disponiveis[:6]
    termo = re.sub(r"^(av|avenida|r|rua|pc|praca|praça|tv|travessa)\.?\s+", "", logradouro.strip(), flags=re.I)
    numero = str(numero).strip() if numero not in (None, "") else None
    saida = {"fonte": "Prefeitura do Recife — dados abertos, Imposto Predial e Territorial Urbano (IPTU)",
             "pagina": f"{_RECIFE}/dataset/imposto-predial-e-territorial-urbano-iptu",
             "anos_disponiveis": disponiveis,
             "aviso": ("alíquota efetiva = valor cobrado / valor total estimado. Alíquota que sobe ano a ano no mesmo "
                       "imóvel é indício de IPTU progressivo no tempo; estável é indício de que não é aplicado. "
                       "Este cadastro NÃO mostra dívida ativa nem se o imposto foi pago. CPF/CNPJ vêm mascarados. "
                       "O campo 'pavimentos' não é confiável (em vários lotes vem 1 com área construída maior que o "
                       "terreno): não tire conclusão dele nem aponte a inconsistência como achado; diga só que o "
                       "número de pavimentos precisa ser verificado."),
             "anos": {}}
    for ano in anos:
        rid = _cache_iptu["recursos"].get(ano)
        if not rid:
            saida["anos"][ano] = "sem dados abertos para este ano"
            continue
        r = _get(f"{_RECIFE}/api/3/action/datastore_search",
                 {"resource_id": rid, "q": f"{termo} {numero or ''}".strip(), "limit": 300})
        r.raise_for_status()
        regs = [x for x in r.json()["result"]["records"]
                if termo.lower() in str(x.get("logradouro", "")).lower()
                and (numero is None or str(x.get("numero")) == numero)]
        unidades = []
        for x in regs:
            cobrado, venal = _num(x.get("valor cobrado de IPTU")), _num(x.get("valor total do imóvel estimado"))
            unidades.append({"endereco": f"{x.get('logradouro')}, {x.get('numero')} {x.get('complemento') or ''}".strip(),
                             "uso": x.get("tipo de uso do imóvel"), "construcao": x.get("Tipo de Construção"),
                             "area_terreno": x.get("AREA TERRENO"), "area_construida": x.get("AREA CONSTRUIDA"),
                             "pavimentos": x.get("quantidade de pavimentos"), "ano_construcao": x.get("ano da construção corrigido"),
                             "tipo_contribuinte": x.get("tipo de contribuinte"), "valor_venal": venal, "iptu_cobrado": cobrado,
                             "aliquota_efetiva_%": round(100 * cobrado / venal, 3) if cobrado and venal else None,
                             "regime_iptu": x.get("Regime de Tributação do iptu"),
                             "lat": x.get("latitude"), "lon": x.get("longitude")})
        aliq = [u["aliquota_efetiva_%"] for u in unidades if u["aliquota_efetiva_%"] is not None]
        resumo = {"consulta": r.url, "n_unidades": len(unidades),
                  "iptu_total_cobrado": round(sum(u["iptu_cobrado"] or 0 for u in unidades), 2),
                  "valor_venal_total": round(sum(u["valor_venal"] or 0 for u in unidades), 2),
                  "aliquota_efetiva_min_max_%": [min(aliq), max(aliq)] if aliq else None,
                  "regimes": sorted({str(u["regime_iptu"]) for u in unidades})}
        if ano == anos[0]:  # unidade por unidade só no ano mais recente, para caber
            resumo["unidades"] = unidades[:12]
        saida["anos"][ano] = resumo
    return saida


def iptu_recife_proximos(lat, lon, bairro, raio_m=200, ano=None, limite=20):
    """Lotes do cadastro de IPTU do Recife perto de uma coordenada, agrupados por endereço."""
    recursos = _recursos_iptu()
    ano = int(ano or max(recursos))
    rid = recursos.get(ano)
    if not rid:
        raise ValueError(f"sem dados de IPTU para {ano}")
    chave = (rid, bairro.strip().lower())
    if chave not in _cache_iptu:
        regs, total = [], None
        while len(regs) < 30000:  # bairros muito grandes ficam cortados: o agente é avisado
            r = _get(f"{_RECIFE}/api/3/action/datastore_search",
                     {"resource_id": rid, "filters": json.dumps({"bairro": bairro.strip()}), "limit": 1000,
                      "offset": len(regs)})
            r.raise_for_status()
            res = r.json()["result"]
            total = res.get("total", 0)
            regs += res["records"]  # o portal devolve no máximo 500 por página, qualquer que seja o limit
            if not res["records"] or len(regs) >= total:
                break
        _cache_iptu[chave] = regs
    regs = _cache_iptu[chave]
    if not regs:
        raise ValueError(f"nenhum registro no bairro '{bairro}'; use o nome exato do bairro como no cadastro "
                         "(ex.: 'Recife' para o Bairro do Recife, 'Santo Antonio', 'Boa Vista')")
    lotes = {}
    for x in regs:
        k = (x.get("logradouro"), x.get("numero"))
        lt = lotes.setdefault(k, {"endereco": f"{k[0]}, {k[1]}", "lat": x.get("latitude"), "lon": x.get("longitude"),
                                  "area_terreno": x.get("AREA TERRENO"), "area_construida_total": 0.0,
                                  "n_unidades": 0, "iptu_total": 0.0, "valor_venal_total": 0.0,
                                  "regimes": set(), "tipos": set(), "usos": set()})
        lt["lat"] = lt["lat"] or x.get("latitude")
        lt["lon"] = lt["lon"] or x.get("longitude")
        lt["n_unidades"] += 1
        lt["area_construida_total"] += _num(x.get("AREA CONSTRUIDA")) or 0
        lt["iptu_total"] += _num(x.get("valor cobrado de IPTU")) or 0
        lt["valor_venal_total"] += _num(x.get("valor total do imóvel estimado")) or 0
        lt["regimes"].add(str(x.get("Regime de Tributação do iptu")))
        lt["tipos"].add(str(x.get("Tipo de Construção")))
        lt["usos"].add(str(x.get("tipo de uso do imóvel")))
    perto, sem_coord = [], []
    for lt in lotes.values():
        for c in ("regimes", "tipos", "usos"):
            lt[c] = sorted(lt[c])
        lt["iptu_total"], lt["valor_venal_total"] = round(lt["iptu_total"], 2), round(lt["valor_venal_total"], 2)
        lt["area_construida_total"] = round(lt["area_construida_total"], 1)
        if lt["lat"] and lt["lon"]:
            d = _distancia_m(lat, lon, lt["lat"], lt["lon"])
            if d <= raio_m:
                perto.append({"distancia_m": round(d), **lt})
        else:
            sem_coord.append(lt)
    perto.sort(key=lambda x: x["distancia_m"])
    sem_coord.sort(key=lambda x: -(_num(x["area_terreno"]) or 0))
    return {"fonte": "Prefeitura do Recife — dados abertos, IPTU", "ano": ano,
            "pagina": f"{_RECIFE}/dataset/imposto-predial-e-territorial-urbano-iptu",
            "consulta": f"{_RECIFE}/api/3/action/datastore_search?resource_id={rid}&filters="
                        + requests.utils.quote(json.dumps({"bairro": bairro.strip()})),
            "aviso": ("lotes = unidades agrupadas por logradouro e número; a coordenada é a do cadastro. "
                      "Confirme o lote pelo endereço e pela área. 'Imune Executivo União' = União; "
                      "'Imunidade Recíproca'/'Imune Executivo' = ente público; 'Hasta Publica' = arrematado em leilão."),
            "registros_no_bairro": len(regs), "cortado": len(regs) >= 30000,
            "lotes_no_raio": perto[:int(min(limite, 40))],
            "maiores_lotes_sem_coordenada": sem_coord[:8]}


def consultar_cnpj(cnpj):
    cnpj = re.sub(r"\D", "", cnpj)
    r = _get(f"https://brasilapi.com.br/api/cnpj/v1/{cnpj}")
    r.raise_for_status()
    d = r.json()
    campos = ("cnpj", "razao_social", "nome_fantasia", "natureza_juridica", "descricao_situacao_cadastral",
              "logradouro", "numero", "bairro", "municipio", "uf", "cep", "cnae_fiscal_descricao")
    return {"fonte": "BrasilAPI (Receita Federal)", "url": r.url, **{k: d.get(k) for k in campos}}


def municipio_ibge(nome, uf):
    r = _get(f"https://servicodados.ibge.gov.br/api/v1/localidades/estados/{uf.strip().upper()}/municipios")
    r.raise_for_status()
    alvo = nome.strip().lower()
    achados = [{"codigo_ibge": m["id"], "nome": m["nome"]} for m in r.json() if alvo in m["nome"].lower()]
    return {"fonte": "IBGE — API de localidades", "url": r.url, "municipios": achados}


def portal_transparencia(endpoint, parametros, ctx):
    if not ctx.chave_transparencia:
        raise RuntimeError("sem chave do Portal da Transparência: quem usa o app pode cadastrar uma em "
                           "https://portaldatransparencia.gov.br/api-de-dados/cadastrar-email e colar na barra lateral")
    endpoint = endpoint.strip().strip("/")
    if not re.fullmatch(r"[a-z0-9\-/]+", endpoint):
        raise ValueError("endpoint inválido")
    r = _get(f"https://api.portaldatransparencia.gov.br/api-de-dados/{endpoint}", parametros or {},
             headers={"chave-api-dados": ctx.chave_transparencia, "Accept": "application/json"})
    if r.status_code >= 400:
        raise RuntimeError(f"HTTP {r.status_code}: {r.text[:500]}")
    # a URL vai sem a chave (a chave viaja no cabeçalho)
    return {"fonte": "Portal da Transparência (CGU)", "url": r.url, "dados": r.json()}


def _dados_gov(caminho, params, ctx):
    if not ctx.chave_dados_gov:
        raise RuntimeError("sem token do dados.gov.br: gere em dados.gov.br > Entrar (perfil Consumidor) > "
                           "Minha Conta e cole na barra lateral")
    r = _get(f"https://dados.gov.br/dados/api/publico/{caminho}", params,
             headers={"chave-api-dados-abertos": ctx.chave_dados_gov})
    if r.status_code >= 400:
        raise RuntimeError(f"HTTP {r.status_code} (token inválido ou expirado?)")
    return r


def dados_gov_buscar(termo, ctx, pagina=1):
    r = _dados_gov("conjuntos-dados", {"nomeConjuntoDados": termo, "pagina": pagina}, ctx)
    return {"fonte": "Portal Brasileiro de Dados Abertos (dados.gov.br)", "busca": termo, "conjuntos": [
        {"id": c.get("id"), "titulo": c.get("title"), "organizacao": c.get("nomeOrganizacao"),
         "pagina": f"https://dados.gov.br/dados/conjuntos-dados/{c.get('nome')}",
         "dados_atualizados_em": c.get("ultimaAtualizacaoDados")} for c in r.json()]}


def dados_gov_conjunto(id_conjunto, ctx):
    d = _dados_gov(f"conjuntos-dados/{id_conjunto}", None, ctx).json()
    return {"fonte": "dados.gov.br", "titulo": d.get("titulo"), "descricao": (d.get("descricao") or "")[:1500],
            "organizacao": (d.get("organizacao") or {}).get("titulo") if isinstance(d.get("organizacao"), dict)
            else d.get("organizacao"), "periodicidade": d.get("periodicidade"),
            "pagina": f"https://dados.gov.br/dados/conjuntos-dados/{d.get('nome')}",
            "recursos": [{"titulo": r.get("titulo"), "tipo": r.get("tipo"), "formato": r.get("formato"),
                          "link": r.get("link"), "descricao": (r.get("descricao") or "")[:300],
                          "atualizado_em": r.get("dataUltimaAtualizacaoArquivo")} for r in d.get("recursos", [])]}


def _pontos(geom):
    """Todas as coordenadas (lon, lat) de uma geometria GeoJSON."""
    if not geom:
        return []
    if geom["type"] == "GeometryCollection":
        return [p for g in geom["geometries"] for p in _pontos(g)]
    pilha, saida = [geom.get("coordinates")], []
    while pilha:
        c = pilha.pop()
        if isinstance(c, (list, tuple)) and c and isinstance(c[0], (int, float)):
            saida.append((c[0], c[1]))
        elif isinstance(c, (list, tuple)):
            pilha.extend(c)
    return saida


def _distancia_m(lat1, lon1, lat2, lon2):
    r = 6371000
    p1, p2 = math.radians(lat1), math.radians(lat2)
    a = (math.sin((p2 - p1) / 2) ** 2
         + math.cos(p1) * math.cos(p2) * math.sin(math.radians(lon2 - lon1) / 2) ** 2)
    return 2 * r * math.asin(math.sqrt(a))


def imoveis_uniao_proximos(lat, lon, raio_m=300, limite=15):
    if not ARQUIVO_SPU.exists():
        raise RuntimeError(f"arquivo da SPU não encontrado em {ARQUIVO_SPU}. Ele precisa ser baixado no navegador "
                           f"(o site bloqueia download automático): {URL_SPU}")
    mtime = ARQUIVO_SPU.stat().st_mtime
    if _cache_spu.get("mtime") != mtime:
        with open(ARQUIVO_SPU, encoding="utf-8") as f:
            feats = json.load(f).get("features", [])
        _cache_spu.update(mtime=mtime, feicoes=[(f.get("properties") or {}, _pontos(f.get("geometry")))
                                                  for f in feats])
    raio_m = max(10, min(float(raio_m), 5000))
    achados = []
    for props, pts in _cache_spu["feicoes"]:
        if not pts:
            continue
        d = min(_distancia_m(lat, lon, la, lo) for lo, la in pts)
        if d <= raio_m:
            achados.append({"distancia_m": round(d), **props})
    achados.sort(key=lambda x: x["distancia_m"])
    return {"fonte": "SPU/MGI — Imóveis da União, pontos georreferenciados (dados.gov.br)", "url": URL_SPU,
            "arquivo_baixado_em": datetime.fromtimestamp(mtime).strftime("%Y-%m-%d"),
            "aviso": "o ponto da SPU pode não coincidir com o prédio exato; confirme pelo endereço e pelo RIP",
            "n": len(achados), "imoveis": achados[:int(min(limite, 50))]}


def _url_publica(url):
    """Só http(s) para endereço público: a ferramenta roda no computador de quem usa o app."""
    import ipaddress
    import socket
    from urllib.parse import urlparse
    u = urlparse(url)
    if u.scheme not in ("http", "https") or not u.hostname:
        raise ValueError("só URLs http(s)")
    for info in socket.getaddrinfo(u.hostname, None):
        ip = ipaddress.ip_address(info[4][0])
        if ip.is_private or ip.is_loopback or ip.is_link_local or ip.is_reserved:
            raise ValueError("endereço de rede interna não permitido")


def _wayback(url):
    """URL da cópia arquivada mais recente no Wayback Machine (versão crua, sem a barra do arquivo)."""
    r = _get("https://archive.org/wayback/available", {"url": url})
    snap = (r.json().get("archived_snapshots") or {}).get("closest") if r.ok else None
    if not snap or not snap.get("available"):
        return None, None
    ts = snap["timestamp"]
    return f"https://web.archive.org/web/{ts}id_/{url}", f"{ts[6:8]}/{ts[4:6]}/{ts[:4]}"


def ler_pagina(url, buscar=None, pagina_pdf_inicial=1):
    """Lê uma página web ou PDF e devolve o texto (ou os trechos em torno de `buscar`).

    Se a página falhar, tiver saído do ar ou vier vazia (site em JavaScript), tenta a cópia do Wayback Machine.
    """
    try:
        _url_publica(url)
        saida = _ler(url, buscar, pagina_pdf_inicial)
        if saida.pop("_caracteres") >= 300:
            return saida
        motivo = "a página veio sem texto (provavelmente montada por JavaScript)"
    except OSError as e:  # domínio que saiu do ar (DNS) ou falha de conexão
        motivo = f"a página não abriu ({e})"
    except RuntimeError as e:  # HTTP 4xx/5xx
        motivo = f"a página não abriu ({e})"
    arquivo, data = _wayback(url)
    if not arquivo:
        raise RuntimeError(f"{motivo}, e não há cópia no Wayback Machine")
    saida = _ler(arquivo, buscar, pagina_pdf_inicial)
    saida.pop("_caracteres")
    saida.update(fonte=f"cópia arquivada no Wayback Machine em {data}", url_original=url,
                 aviso_arquivo=f"{motivo}; o texto é da cópia de {data}. Cite a URL do arquivo como fonte.")
    return saida


def _ler(url, buscar, pagina_pdf_inicial):
    r = _http.get(url, timeout=60, allow_redirects=True)
    if r.status_code >= 400:
        raise RuntimeError(f"HTTP {r.status_code}")
    _url_publica(r.url)  # o redirecionamento também precisa ser público
    tipo = r.headers.get("content-type", "").lower()
    if "pdf" in tipo or r.content[:5] == b"%PDF-":
        import io
        from pypdf import PdfReader
        pdf = PdfReader(io.BytesIO(r.content))
        ini = max(1, int(pagina_pdf_inicial))
        paginas = range(ini - 1, min(len(pdf.pages), ini - 1 + 25))
        texto = "\n".join(f"[pág. {i + 1}] {pdf.pages[i].extract_text() or ''}" for i in paginas)
        formato = f"PDF, {len(pdf.pages)} páginas (lidas {ini}–{paginas[-1] + 1 if paginas else ini})"
    else:
        from bs4 import BeautifulSoup
        sopa = BeautifulSoup(r.content, "html.parser")
        for t in sopa(["script", "style", "nav", "footer", "header", "aside", "form", "noscript"]):
            t.decompose()
        corpo = sopa.find("article") or sopa.find("main") or sopa.body or sopa
        texto = re.sub(r"\n\s*\n+", "\n\n", corpo.get_text("\n", strip=True))
        formato = "HTML"
        titulo = sopa.title.get_text(strip=True) if sopa.title else None
    saida = {"fonte": "leitura direta da página", "url": r.url, "formato": formato,
             "titulo": None if formato.startswith("PDF") else titulo, "_caracteres": len(texto.strip())}
    if buscar:
        trechos = []
        for m in re.finditer(re.escape(buscar), texto, flags=re.I):
            trechos.append(texto[max(0, m.start() - 600):m.end() + 600])
            if len(trechos) == 6:
                break
        saida["buscar"] = buscar
        saida["trechos"] = trechos or "termo não encontrado no texto"
    else:
        saida["texto"] = texto[:11000]
        if len(texto) > 11000:
            saida["aviso"] = f"texto cortado ({len(texto)} caracteres): use `buscar` para achar um trecho"
    return saida


def registrar_evidencia(afirmacao, fonte, url, trecho, tipo, ctx, valor=None, periodo=None):
    eid = f"E{len(ctx.dossie) + 1}"
    ctx.dossie.append({"id": eid, "afirmacao": afirmacao, "valor": valor, "periodo": periodo,
                       "fonte": fonte, "url": url, "trecho": trecho, "tipo": tipo,
                       "consultado_em": datetime.now().strftime("%Y-%m-%d %H:%M")})
    return {"id": eid, "ok": True, "total_no_dossie": len(ctx.dossie)}


# ---------------------------------------------------------------- esquemas

def _obj(props, req):
    return {"type": "object", "properties": props, "required": req, "additionalProperties": False}


FERRAMENTAS = [
    {"name": "geocodificar_endereco",
     "description": "Converte endereço ou nome de prédio em coordenadas (OpenStreetMap). Use antes de suscetibilidade_inundacao.",
     "input_schema": _obj({"endereco": {"type": "string", "description": "endereço completo com cidade e UF"}}, ["endereco"])},
    {"name": "suscetibilidade_inundacao",
     "description": ("Consulta as cartas oficiais do Serviço Geológico do Brasil (suscetibilidade a inundação e "
                     "setores de risco geológico) em torno de uma coordenada. Base da ficha de aptidão."),
     "input_schema": _obj({"lat": {"type": "number"}, "lon": {"type": "number"},
                           "raio_m": {"type": "number", "description": "raio em metros (padrão 100)"}}, ["lat", "lon"])},
    {"name": "contratos_federais",
     "description": ("Contratos de órgãos federais (Compras.gov.br) num período, filtrados por palavras do objeto "
                     "(ex.: vigilância, segurança patrimonial, manutenção predial, condomínio, IPTU, energia). "
                     "Use para achar quanto o órgão gasta com o imóvel vazio. Datas AAAA-MM-DD; prefira janelas de até 12 meses. "
                     "codigo_orgao é o código SIAFI do órgão; codigo_unidade_gestora é a UASG."),
     "input_schema": _obj({"data_inicio": {"type": "string"}, "data_fim": {"type": "string"},
                           "codigo_orgao": {"type": "string"}, "codigo_unidade_gestora": {"type": "string"},
                           "palavras_chave": {"type": "array", "items": {"type": "string"}},
                           "max_paginas": {"type": "integer"}}, ["data_inicio", "data_fim"])},
    {"name": "ckan_buscar",
     "description": ("Busca conjuntos de dados em portais CKAN públicos (ex.: https://dados.recife.pe.gov.br, que tem "
                     "'Imóveis da Administração Pública Municipal' e 'Próprios municipais'). Devolve ids dos recursos."),
     "input_schema": _obj({"portal": {"type": "string"}, "termo": {"type": "string"},
                           "linhas": {"type": "integer"}}, ["portal", "termo"])},
    {"name": "ckan_ler_recurso",
     "description": "Lê registros de um recurso CKAN com datastore ativo, com busca textual opcional (ex.: nome da rua).",
     "input_schema": _obj({"portal": {"type": "string"}, "recurso_id": {"type": "string"},
                           "filtro": {"type": "string"}, "limite": {"type": "integer"}}, ["portal", "recurso_id"])},
    {"name": "iptu_recife",
     "description": ("IPTU lançado pela Prefeitura do Recife para um endereço, ano a ano: valor venal, IPTU cobrado, "
                     "alíquota efetiva, regime, uso, área, pavimentos. Serve para ver se o IPTU progressivo está sendo "
                     "aplicado a um imóvel ocioso privado. Use o nome do logradouro sem o tipo (ex.: 'DANTAS BARRETO') "
                     "e o número. Só para o Recife; em outras cidades use ckan_buscar e web_search."),
     "input_schema": _obj({"logradouro": {"type": "string"}, "numero": {"type": "string"},
                           "anos": {"type": "array", "items": {"type": "integer"},
                                    "description": "padrão: os 6 anos mais recentes"}}, ["logradouro"])},
    {"name": "iptu_recife_proximos",
     "description": ("Lotes do cadastro de IPTU do Recife perto de uma coordenada, dentro de um bairro, com área do "
                     "terreno, área construída, IPTU total, regime (normal, imune da União, imunidade recíproca, hasta "
                     "pública, isenções) e tipo de construção. Use quando a busca por endereço (iptu_recife) não achar "
                     "o imóvel: muitos imóveis estão cadastrados com outro logradouro. 'bairro' é o nome do cadastro "
                     "(ex.: 'Recife' para o Bairro do Recife). Depois confirme o lote com iptu_recife."),
     "input_schema": _obj({"lat": {"type": "number"}, "lon": {"type": "number"}, "bairro": {"type": "string"},
                           "raio_m": {"type": "number", "description": "padrão 200"},
                           "ano": {"type": "integer"}, "limite": {"type": "integer"}}, ["lat", "lon", "bairro"])},
    {"name": "consultar_cnpj",
     "description": "Dados cadastrais de um CNPJ (órgão dono, fornecedor de vigilância etc.).",
     "input_schema": _obj({"cnpj": {"type": "string"}}, ["cnpj"])},
    {"name": "municipio_ibge",
     "description": "Código IBGE de um município (exigido por algumas APIs).",
     "input_schema": _obj({"nome": {"type": "string"}, "uf": {"type": "string"}}, ["nome", "uf"])},
    {"name": "portal_transparencia",
     "description": ("GET na API do Portal da Transparência (https://api.portaldatransparencia.gov.br/swagger-ui/index.html). "
                     "endpoint sem barra inicial, ex.: 'contratos', 'despesas/documentos'. Só funciona se o usuário informou a chave."),
     "input_schema": _obj({"endpoint": {"type": "string"},
                           "parametros": {"type": "object", "additionalProperties": {"type": "string"}}},
                          ["endpoint", "parametros"])},
    {"name": "imoveis_uniao_proximos",
     "description": ("Imóveis da União cadastrados pela SPU num raio em torno de uma coordenada (arquivo oficial de "
                     "pontos georreferenciados). Use logo após geocodificar: diz se o prédio é da União, o RIP, "
                     "a situação e a destinação cadastradas."),
     "input_schema": _obj({"lat": {"type": "number"}, "lon": {"type": "number"},
                           "raio_m": {"type": "number", "description": "padrão 300"},
                           "limite": {"type": "integer"}}, ["lat", "lon"])},
    {"name": "dados_gov_buscar",
     "description": ("Busca conjuntos de dados no catálogo federal dados.gov.br pelo nome (ex.: 'imóveis da união', "
                     "'imóveis funcionais', 'defesa civil'). Devolve ids para dados_gov_conjunto."),
     "input_schema": _obj({"termo": {"type": "string"}, "pagina": {"type": "integer"}}, ["termo"])},
    {"name": "dados_gov_conjunto",
     "description": "Detalhes de um conjunto do dados.gov.br, com os links dos arquivos (que você pode abrir com web_fetch).",
     "input_schema": _obj({"id_conjunto": {"type": "string"}}, ["id_conjunto"])},
    {"name": "ler_pagina",
     "description": ("Lê o texto integral de uma página web ou de um PDF (pareceres, diários oficiais, leis, "
                     "reportagens). Use quando web_fetch falhar ou para ler um PDF: muitos sites de governo bloqueiam "
                     "o web_fetch mas abrem aqui. 'buscar' devolve só os trechos em torno de um termo, útil em textos "
                     "longos. Para PDF grande, 'pagina_pdf_inicial' escolhe de onde começar (lê 25 páginas)."),
     "input_schema": _obj({"url": {"type": "string"}, "buscar": {"type": "string"},
                           "pagina_pdf_inicial": {"type": "integer"}}, ["url"])},
    {"name": "registrar_evidencia",
     "description": ("Registra no dossiê UMA evidência que sustenta uma afirmação do laudo. Devolve o id (E1, E2…) que o "
                     "redator vai citar. Registre só o que você leu na fonte; copie o trecho literal que prova."),
     "input_schema": _obj({
         "afirmacao": {"type": "string", "description": "o fato, em uma frase"},
         "valor": {"type": "string", "description": "número com unidade, se houver (ex.: 'R$ 1.234.567,00', '3 pavimentos')"},
         "periodo": {"type": "string", "description": "período a que o valor se refere, se houver"},
         "fonte": {"type": "string", "description": "nome da base ou do documento"},
         "url": {"type": "string"},
         "trecho": {"type": "string", "description": "trecho literal ou campo/valor exato que prova a afirmação"},
         "tipo": {"type": "string", "enum": ["oficial", "imprensa", "academico", "movimento_social", "outro"]}},
         ["afirmacao", "fonte", "url", "trecho", "tipo"])},
]

def _anota_geocodificacao(res, ctx):
    if ctx.coordenadas is None and res.get("resultados"):
        ctx.coordenadas = (res["resultados"][0]["lat"], res["resultados"][0]["lon"])
    return res


_FUNCOES = {
    "geocodificar_endereco": lambda i, c: _anota_geocodificacao(geocodificar_endereco(**i), c),
    # o pesquisador consulta as cartas já no ponto do imóvel: essa é a melhor coordenada para o mapa
    "suscetibilidade_inundacao": lambda i, c: (setattr(c, "coordenadas", (i["lat"], i["lon"])),
                                               suscetibilidade_inundacao(**i))[1],
    "contratos_federais": lambda i, c: contratos_federais(**i),
    "ckan_buscar": lambda i, c: ckan_buscar(**i),
    "ckan_ler_recurso": lambda i, c: ckan_ler_recurso(**i),
    "iptu_recife": lambda i, c: iptu_recife(**i),
    "iptu_recife_proximos": lambda i, c: iptu_recife_proximos(**i),
    "consultar_cnpj": lambda i, c: consultar_cnpj(**i),
    "municipio_ibge": lambda i, c: municipio_ibge(**i),
    "portal_transparencia": lambda i, c: portal_transparencia(i["endpoint"], i.get("parametros"), c),
    "imoveis_uniao_proximos": lambda i, c: imoveis_uniao_proximos(**i),
    "dados_gov_buscar": lambda i, c: dados_gov_buscar(ctx=c, **i),
    "dados_gov_conjunto": lambda i, c: dados_gov_conjunto(i["id_conjunto"], c),
    "ler_pagina": lambda i, c: ler_pagina(**i),
    "registrar_evidencia": lambda i, c: registrar_evidencia(ctx=c, **i),
}


def ler_env():
    """Lê chao_publico/.env (CHAVE=valor por linha). O arquivo fica fora do Git."""
    env = {}
    arq = Path(__file__).parent / ".env"
    if arq.exists():
        for linha in arq.read_text(encoding="utf-8").splitlines():
            if "=" in linha and not linha.lstrip().startswith("#"):
                k, v = linha.split("=", 1)
                env[k.strip()] = v.strip().strip('"').strip("'")
    return env


def executar(nome, entrada, ctx):
    """Executa uma ferramenta. Devolve (texto, erro?)."""
    if nome not in _FUNCOES:
        return f"ferramenta desconhecida: {nome}", True
    try:
        return _corta(_FUNCOES[nome](dict(entrada or {}), ctx)), False
    except requests.RequestException as e:
        return f"falha de rede ao consultar a base: {e}", True
    except Exception as e:  # erro de parâmetro ou da base: o agente lê e tenta outro caminho
        return f"erro: {e}", True
