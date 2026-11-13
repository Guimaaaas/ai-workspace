"""Histórico de imóveis laudados: um arquivo JSON por laudo em chao_publico/dados/laudos/ (fora do Git).

É o começo do "mapear" da ideia: cada laudo vira um ponto no mapa e fica disponível para reabrir.
Para um app publicado com várias pessoas, isto precisa virar um banco de dados compartilhado.
"""

import json
import re
from datetime import datetime
from pathlib import Path

PASTA = Path(__file__).parent / "dados" / "laudos"


def _titulo(documento):
    m = re.search(r"^#\s*(?:Laudo Chão Público:\s*)?(.+)$", documento or "", flags=re.M)
    return m.group(1).strip() if m else "imóvel sem título"


def salvar(resultado, pedido, coordenadas, modelo, pedidos_lai=None, id_existente=None):
    """Grava (ou atualiza) um laudo. Devolve o id."""
    PASTA.mkdir(parents=True, exist_ok=True)
    agora = datetime.now()
    lid = id_existente or agora.strftime("%Y%m%d-%H%M%S")
    registro = {"id": lid, "titulo": _titulo(resultado["documento"]), "data": agora.strftime("%Y-%m-%d %H:%M"),
                "pedido": pedido, "modelo": modelo, "status": resultado.get("status"),
                "lat": coordenadas[0] if coordenadas else None, "lon": coordenadas[1] if coordenadas else None,
                "documento": resultado["documento"], "dossie": resultado.get("dossie", []),
                "pedidos_lai": pedidos_lai}
    (PASTA / f"{lid}.json").write_text(json.dumps(registro, ensure_ascii=False, indent=1), encoding="utf-8")
    return lid


def anexar_pedidos_lai(lid, texto):
    arq = PASTA / f"{lid}.json"
    if arq.exists():
        reg = json.loads(arq.read_text(encoding="utf-8"))
        reg["pedidos_lai"] = texto
        arq.write_text(json.dumps(reg, ensure_ascii=False, indent=1), encoding="utf-8")


def listar():
    """Laudos salvos, do mais recente ao mais antigo."""
    if not PASTA.exists():
        return []
    regs = []
    for arq in PASTA.glob("*.json"):
        try:
            regs.append(json.loads(arq.read_text(encoding="utf-8")))
        except (json.JSONDecodeError, OSError):
            continue
    return sorted(regs, key=lambda r: r.get("id", ""), reverse=True)
