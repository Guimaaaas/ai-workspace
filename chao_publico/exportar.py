"""Exporta o laudo (Markdown) para PDF, com tabelas, links, cabeçalho e numeração de páginas."""

import os
import re
from datetime import datetime

import markdown
from fpdf import FPDF

# fontes TrueType com acentos e símbolos (≈, ÷, −). A primeira que existir é usada.
_FONTES = [
    {"": r"C:\Windows\Fonts\arial.ttf", "B": r"C:\Windows\Fonts\arialbd.ttf",
     "I": r"C:\Windows\Fonts\ariali.ttf", "BI": r"C:\Windows\Fonts\arialbi.ttf"},
    {"": "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", "B": "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
     "I": "/usr/share/fonts/truetype/dejavu/DejaVuSans-Oblique.ttf",
     "BI": "/usr/share/fonts/truetype/dejavu/DejaVuSans-BoldOblique.ttf"},
    {"": "/System/Library/Fonts/Supplemental/Arial.ttf", "B": "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
     "I": "/System/Library/Fonts/Supplemental/Arial Italic.ttf",
     "BI": "/System/Library/Fonts/Supplemental/Arial Bold Italic.ttf"},
]
_SIMBOLOS = [r"C:\Windows\Fonts\seguisym.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"]


class _PDF(FPDF):
    rodape = ""

    def header(self):
        if self.page_no() > 1:
            self.set_font(self.font_family, "I", 8)
            self.set_text_color(110)
            self.cell(0, 6, "Chão Público · laudo de imóvel ocioso", align="L")
            self.ln(8)
            self.set_text_color(0)

    def footer(self):
        self.set_y(-12)
        self.set_font(self.font_family, "I", 8)
        self.set_text_color(110)
        self.cell(0, 6, f"{self.rodape}   ·   página {self.page_no()}/{{nb}}", align="C")
        self.set_text_color(0)


def _limpa(md):
    md = re.sub(r"[\U0001F000-\U0001FFFF\u2600-\u27BF\uFE0F]", "", md)  # emojis não cabem na fonte do PDF
    # o Markdown exige linha em branco antes de tabela e de lista; o modelo às vezes esquece
    md = re.sub(r"([^\n|])\n(\|)", r"\1\n\n\2", md)
    md = re.sub(r"([^\n])\n(\s*[-*] |\s*\d+\. )", r"\1\n\n\2", md)
    return md


def _larguras(tabela):
    """Põe width (%) no cabeçalho, proporcional ao texto de cada coluna (colunas curtas ficam estreitas)."""
    linhas = re.findall(r"<tr>(.*?)</tr>", tabela, flags=re.S)
    celulas = [re.findall(r"<t[dh](?:\s[^>]*)?>(.*?)</t[dh]>", ln, flags=re.S) for ln in linhas]
    n = max((len(c) for c in celulas), default=0)
    if n < 2:
        return tabela
    peso = []
    for j in range(n):
        tams = sorted(len(re.sub(r"<[^>]+>", "", c[j])) for c in celulas if j < len(c))
        media = sum(tams) / len(tams)
        peso.append(max(media, 6) ** 0.75)  # amortece: coluna longa ganha mais, sem esmagar as outras
    total = sum(peso)
    pct = [max(8, round(100 * p / total)) for p in peso]
    pct[pct.index(max(pct))] += 100 - sum(pct)
    it = iter(pct)
    cab = re.sub(r"<th(\s[^>]*)?>", lambda m: f'<th width="{next(it, 10)}%">', linhas[0])
    return tabela.replace(linhas[0], cab, 1)


def laudo_pdf(texto_md, titulo_rodape=None):
    """Devolve os bytes do PDF."""
    html = markdown.markdown(_limpa(texto_md), extensions=["tables", "sane_lists"])
    html = re.sub(r"<table>", '<table width="100%" border="1" cellpadding="3">', html)
    # o fpdf2 não aceita tags dentro de célula: fica só o texto (links viram texto com a URL)
    html = re.sub(r"<(td|th)(\s[^>]*)?>(.*?)</\1>",
                  lambda m: f"<{m[1]}{m[2] or ''}>{re.sub(r'<[^>]+>', '', m[3])}</{m[1]}>", html, flags=re.S)
    html = re.sub(r"<table.*?</table>", lambda m: _larguras(m[0]), html, flags=re.S)
    html = re.sub(r"<blockquote>\s*<p>(.*?)</p>\s*</blockquote>", r"<p><i>\1</i></p>", html, flags=re.S)

    pdf = _PDF(format="A4")
    pdf.set_margins(16, 14, 16)
    pdf.set_auto_page_break(True, margin=16)
    fonte = next((f for f in _FONTES if all(os.path.exists(p) for p in f.values())), None)
    if fonte:
        for estilo, caminho in fonte.items():
            pdf.add_font("Corpo", estilo, caminho)
        familia = "Corpo"
        simb = next((p for p in _SIMBOLOS if os.path.exists(p)), None)
        if simb:
            pdf.add_font("Simbolos", "", simb)
            pdf.set_fallback_fonts(["Simbolos"])
    else:  # sem TTF: fonte padrão (só Latin-1)
        familia = "helvetica"
        html = html.encode("latin-1", "replace").decode("latin-1")
    pdf.set_font(familia, size=9.5)
    pdf.rodape = titulo_rodape or f"gerado em {datetime.now():%d/%m/%Y %H:%M}"
    pdf.add_page()
    pdf.write_html(html, font_family=familia, table_line_separators=True,
                   tag_styles=None)
    return bytes(pdf.output())
