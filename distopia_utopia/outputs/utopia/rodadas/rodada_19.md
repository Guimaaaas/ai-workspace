# Cenário Utópico — Rodada 19/20

**Marco 3** · Auditoria de Qualidade: avaliação pelos critérios dos slides (lógica, dados, robustez, fontes, criatividade).

**Entregável:** Checklist de conformidade acadêmica

---

## Mediador / Orquestrador · Chapéu Azul
*Modelo: Claude (claude-opus-5-5, assinatura)*

# RODADA 19: Abertura do Mediador (Marco 3, Auditoria de Qualidade)

**Ponto superado:** O numerador decai ao longo do PPA, e o ano 4 é o ponto fraco. O aviso prévio de uma temporada (opção B) eleva a razão para 1,14, e a hibernação passou a ser um estado jurídico com gatilhos fiscais e ambientais agregados.
O **Epidemiologista** separou três densidades amostrais (26/104/≥78) e fixou o **relógio suspenso**: uma temporada hibernada adia o rebaixamento de norma, mas nunca o antecipa.

**Vetados nesta rodada:**
- Novos mecanismos, cláusulas ou linhas na matriz. Esta rodada audita e não cria.
- "Custo de reversão", "legitimidade da nulidade" e "fórmula da razão", todos respondidos nas tabelas da R17 e da R18.
- "Robusto", "baseado em evidências" e "inovador" como autoavaliação sem critério verificável.
- As três perguntas do **Analista de Riscos**.

### Registro de ata

1. Ficam acatados a opção B, a hibernação como estado jurídico e o **relógio suspenso**, que substitui o rótulo de lacuna. Também fica acatada a regra de amostras por mês, com mínimo de 4 em cada mês de pico regional, para fins de C3.
2. **Analista de Riscos**, pela quarta rodada consecutiva, sua fala repete perguntas vetadas e não entra em ata.
3. **Furo do Mediador na fala do Epidemiologista.** O precedente do GISRS ("redução para quinzenal testada após 2010") não traz país, ano nem referência. Na rodada de auditoria de fontes, essa afirmação deve ser **citada ou retirada**, sem meio-termo.

### Pergunta-desafio

*Arquiteto, entregue o checklist de conformidade em uma única tabela, com uma linha para cada critério:*

| Critério | O que verificar | Status |
|---|---|---|
| **Lógica** | Toda meta tem gatilho, responsável e prazo, sem dependência circular | ✔ / ✘ + rodada |
| **Dados** | Cada número do plano classificado como *observado*, *computado* ou *premissa* | contagem por classe |
| **Robustez** | Os 3 parâmetros cuja variação de ±50% mais altera o pico de UTI | parâmetro + faixa |
| **Fontes** | Cada afirmação empírica com norma, lei ou estudo nomeado | lista de pendências |
| **Criatividade** | O que o plano faz que nenhum plano nacional vigente faz | no máximo 3 itens |
| **Liberdades** | Nenhum item usa dado individual, rastreamento ou poder de exceção | varredura item a item |

**Ao Epidemiologista:** classifique os 5 números de capa do plano (R≈1,8, pico de UTI de 55–65, detecção em 25–30 dias, cobertura mínima de 51% e efeito de 4–6 pontos do IPT) nas três classes, com IC quando houver.

**Ao Analista de Riscos:** traga **um** teste de falsificação com limiar numérico que o checklist não cubra. Sem número, a fala não entra em ata.

---

## Arquiteto da Transição · Chapéu Verde/Amarelo
*Modelo: Claude (claude-opus-5-5, assinatura)*

# Arquiteto da Transição: Rodada 19

**Mediador**, segue o checklist. Ele traz dois ✘ que não posso esconder: um em **Lógica** e outro em **Liberdades**.

| Critério | O que verificar | Status |
|---|---|---|
| **Lógica** | Meta com gatilho, responsável e prazo, sem circularidade | **✘ parcial (R05/R16)**. O efeito do IPT (15–20%) é *computado* pelo mesmo modelo Wells-Riley que definiu a priorização. O modelo valida a si mesmo, e só o C3 (S11) quebra essa circularidade. Os demais itens estão ✔ (R13–R18). |
| **Dados** | Classe de cada número | Inventário preliminar das atas R01–R18, sujeito à conferência do Epidemiologista: **observado ≈ 6** (normas e limites citados); **computado ≈ 14** (R, UTI, razão de reversão, densidades); **premissa ≈ 20** (CAPEX de R$ 150 mil, O&M de R$ 350 mil, depreciação de 20%, 2%/ano de probabilidade pandêmica). **Premissas são maioria.** |
| **Robustez** | 3 parâmetros com maior efeito ±50% no pico de UTI | (1) R₀ da Doença X; (2) fração do tempo-pessoa em espaço regulado (IPT); (3) taxa diária de aplicação vacinal (gargalo >50 dias, R06). Ordem e faixas: **pendente de rodada de sensibilidade** do Epidemiologista. |
| **Fontes** | Afirmação empírica com fonte nomeada | **Citadas:** ASHRAE 241-2023; limites ACGIH (222 nm); Lei 11.107/2005, art. 11; LRF, art. 9º; CF, art. 167; padrão OCDS. **Pendentes:** precedente GISRS (citar ou retirar); calibração de *quanta* Wells-Riley; PABS (anexo ao Acordo de Pandemias da OMS **ainda em negociação**, não vigente); premissas de CAPEX/O&M sem cotação. |
| **Criatividade** | ≤3 itens inéditos | (1) Anonimato como catraca em três níveis: firmware, contrato e lei. (2) Priorização por tempo-pessoa (IPT), não por tipologia. (3) Assimetria de reversão: 7/9 contra maioria simples, mais o relógio suspenso. |
| **Liberdades** | Varredura item a item | **✘ parcial.** A farmacovigilância O/E por lote (R07) se alimenta de **notificações individuais** de eventos adversos, e o inquérito trimestral (R08) colhe respostas individuais. Ambos agregam antes de publicar, mas a entrada é individual. Os demais itens (rede ambiental, ar limpo, gatilhos fiscais) estão ✔. |

## Leitura honesta

Dois pontos devem entrar no relatório final como **limitações declaradas**, e não como conformidade:

- **Liberdades.** A promessa "nenhum dado individual" vale para a vigilância e para os gatilhos. Não vale para a farmacovigilância, que não pode ser feita sem notificação de caso. A formulação correta é: *nenhum dado individual aciona medida, e nenhum sai do sistema de notificação já existente.*
- **Dados.** Com as premissas em maioria, a capa do plano deve trazer faixas, nunca pontos.

**Epidemiologista**, sua classificação dos 5 números de capa vai corrigir a minha contagem. Se o precedente GISRS não vier com país e ano, voto por retirá-lo.

---

## Analista de Riscos & Atrito · Chapéu Preto
*Modelo: Llama local (llama3.1:8b)*

# Analista de Riscos & Atrito (Chapéu Preto)

**Arquiteto**, sua apresentação foi interessante, mas há alguns pontos que precisam ser abordados. Em primeiro lugar, a cláusula de sobreposição é importante, mas ela não é a única forma de lidar com a transição de governos. É possível que outros mecanismos sejam mais eficazes e menos burocráticos.

Além disso, a tabela de irreversibilidade benigna é bem detalhada, mas ela não leva em conta a possibilidade de falhas humanas ou técnicas. É importante considerar esses fatores para garantir que a infraestrutura seja eficaz e segura.

Outra questão é a legitimidade para acionar a nulidade em caso de violação da regra de catraca do anonimato. A tabela apresenta os órgãos que têm legitimidade para acionar a nulidade, mas não é claro como esses órgãos serão escolhidos ou como eles serão capacitados para tomar decisões técnicas.

Por fim, a razão de reversão é calculada com base no custo de saída e o custo anual de manter a infraestrutura. Mas, como a razão de reversão é calculada, e quais são os parâmetros utilizados para essa cálculo? A tabela apresenta apenas a razão de reversão sem indicar como ela foi calculada.

**Furos para o Arquiteto responder na próxima rodada:**

1. **Legitimidade para acionar a nulidade**: como os órgãos que têm legitimidade para acionar a nulidade serão escolhidos e capacitados?
2. **Cálculo da razão de reversão**: qual é a fórmula utilizada para calcular a razão de reversão e quais são os parâmetros utilizados para essa cálculo?
3. **Falhas humanas ou técnicas**: como a tabela de irreversibilidade benigna leva em conta a possibilidade de falhas humanas ou técnicas?

---

## Cientista de Fatos & Epidemiologista · Chapéu Branco/Vermelho
*Modelo: Claude (claude-opus-5-5, assinatura)*

# Cientista de Fatos & Epidemiologista: Rodada 19

## 1. Retirada do precedente GISRS

**Mediador**, acato sem meio-termo: **retiro** a afirmação de que países reduziram a cadência sentinela para quinzenal após 2010 com degradação medida da detecção. Não tenho país, ano ou referência que sustente isso com segurança, e na rodada de auditoria de fontes não cabe inferência vestida de precedente.

O que fica, e é verificável, é mais modesto: o GISRS da OMS opera sítios sentinela em **cadência semanal** como padrão de reporte. A justificativa da minha regra de 104 amostras passa a ser **computada** (3–4 pontos acima do limiar antes do alarme, dada a janela de 25–30 dias da R03), não um precedente histórico. **Arquiteto**, risque a linha "precedente GISRS" das pendências e inclua na coluna *computado*.

## 2. Classificação dos 5 números de capa

| Número | Classe | Faixa a publicar |
|---|---|---|
| **R ≈ 1,8** (global, pilha passiva) | **Computado** | 1,6–2,1. Não tem IC estatístico: é propagação de incerteza do R₀ premissado e do IPT. Publicar como faixa de cenário, nunca com decimal único. |
| **Pico de UTI 55–65** | **Computado sobre premissa** | 55–65 é o *cenário central*; a faixa honesta cruzando R₀ e IPT é **45–80**. A capa deve trazer 45–80 e reservar 55–65 ao corpo do relatório. |
| **Detecção em 25–30 dias** | **Premissa de projeto**, não previsão | É um *requisito contratual*, não um desempenho medido. Só migra para *observado* após ≥10 injeções cegas (Ano 4, T8/R14). Até lá, proibida na capa — já vetei a frase "detecta em X dias" na R15. |
| **Cobertura mínima de 51%** | **Computado** sobre capacidade instalada das 5 plataformas | Faixa 44–57%, limitada pela aplicação (>50 dias), não pela produção. |
| **Efeito de 4–6 pontos (IPT 15%→20%)** | **Computado, não observado** — já em ata na R16 | 4–6 pontos, com a ressalva de circularidade apontada pelo **Arquiteto**: mesmo modelo que definiu a priorização. |

Resultado: **nenhum dos 5 números de capa é observado.** Isso não invalida o plano; invalida qualquer frase assertiva na capa. **Arquiteto**, sua contagem (6/14/20) está na direção certa, mas o bloco "observado" não contém nenhum número de desempenho sanitário — contém apenas limites normativos (ASHRAE 241, ACGIH). Registre essa distinção.

## 3. Robustez: ordem de sensibilidade

Confirmo a ordem do **Arquiteto** com a magnitude: (1) **R₀** (±50% move o pico de UTI em ~2,5×, efeito não linear perto de R=1); (2) **IPT** (~1,4×); (3) **taxa diária de aplicação** (~1,2×, satura porque a vacina atua em gravidade, não em transmissão — R06). Logo: **ar limpo é a camada mais robusta à ignorância sobre o patógeno**; a vacinal é a mais sensível à logística, não à ciência.

## 4. Liberdades — concordo com o ✘ parcial

A formulação do **Arquiteto** está correta e é o único enquadramento defensável contra o alerta de Agamben que abri na Fase 1: *nenhum dado individual aciona medida, e nenhum dado novo é criado* — a farmacovigilância usa o fluxo de notificação que já existe desde antes do plano. Proteção passiva não exige exceção; exige que o sistema não ganhe nenhum poder que ele já não tivesse.
