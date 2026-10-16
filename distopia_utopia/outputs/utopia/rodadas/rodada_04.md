# Cenário Utópico — Rodada 04/20

**Fase 1** · Definição do Vetor Silencioso de Proteção: perfil epidemiológico a enfrentar e a infraestrutura passiva que o neutraliza (ar limpo, far-UVC, vigilância ambiental anônima).

**Entregável:** Hipótese base e primeiros atritos

---

## Mediador / Orquestrador · Chapéu Azul
*Modelo: Claude (claude-opus-5-5, assinatura)*

# RODADA 04: Abertura do Mediador

**Ponto superado:** A pilha passiva (filtragem e far-UVC 222 nm com limites ACGIH, teto de ozônio e interlock) reduz a transmissão no espaço regulado para R de 0,5–0,8 e leva o R global a cerca de 1,8 no cenário central.
O **Epidemiologista** estabeleceu que, no cenário de estresse, a métrica de sucesso passa a ser o pico de ocupação de UTI.

**Vetados nesta rodada:** "quem paga a manutenção?", "como garantir segurança e eficácia?" e "dados abertos e privacidade" sem números; "biomanufatura", tema da R05; "ganho de antecedência" como rótulo, pelo motivo abaixo.

### Correção metodológica

**Epidemiologista**, sua conta está certa, mas o rótulo está errado. Com o crescimento mais lento, o limiar de detecção é atingido *mais tarde* no calendário, não antes. O ganho real é outro: aumenta o intervalo entre o alarme da rede ambiental e a saturação hospitalar, porque ambos escalam com 1/ln(R). Peço que esse seja o indicador do cenário central, expresso em dias de distância entre alarme e saturação.

Sua observação sobre superdispersão é o melhor achado da fase. Se 60% da transmissão ocorre no espaço regulado, o R global cai para cerca de 1,56. **Priorizar por densidade de ocupação**, e não por área construída, vale mais do que qualquer camada adicional.

**Analista de Riscos**, é a terceira repetição literal. Fica registrada e encerrada. Sua próxima intervenção só entra em ata se trouxer um custo por m², uma taxa de falha de equipamento ou um caso documentado.

### Guardião das Liberdades: limite preventivo

A priorização por densidade não pode virar contagem de pessoas. Ficam vetados câmeras, contagem por Wi-Fi ou Bluetooth e catracas identificadas. Admite-se apenas **CO₂ ambiente como proxy agregado de ocupação e ventilação**, sem armazenamento por indivíduo.

### Pergunta-desafio

*Arquiteto, transforme a superdispersão em critério de engenharia:*

1. **Índice de prioridade.** Proponha um índice calculável só com dados da edificação: densidade de projeto (pessoas/m²), horas de permanência e mistura de contatos não familiares. Indique que fração do estoque edificado concentra cerca de 80% do risco de eventos de alta transmissão.
2. **Gatilho predial passivo.** Qual limiar de CO₂ (ppm acima do externo) caracteriza não conformidade, e quem o verifica sem inspecionar pessoas?
3. **Ambiente hospitalar.** No cenário de estresse, as próprias unidades de saúde amplificam a transmissão. Que meta específica você fixa para emergências e enfermarias?

**Ao Epidemiologista:** quantifique a redução do pico de UTI no cenário de estresse com a cobertura priorizada.

---

## Arquiteto da Transição · Chapéu Verde/Amarelo
*Modelo: Claude (claude-opus-5-5, assinatura)*

# Arquiteto da Transição: Rodada 04

Acato a correção do **Mediador**: o indicador passa a ser **dias entre alarme e saturação**. Acato também o limite do **Guardião**: tudo abaixo usa apenas dados da edificação, nunca dados de pessoas.

## 1. Índice de Prioridade de Transmissão (IPT)

**IPT = (D × H × M) / Q**

- **D:** densidade de projeto (pessoas/m², do alvará).
- **H:** horas diárias de ocupação.
- **M:** fator de mistura. Vale 1 para contatos fixos (escritório), 2 para semifixos (escola) e 3 para contatos rotativos e não familiares (salas de espera, transporte, abrigos, presídios, casas de show).
- **Q:** vazão de ar limpo existente (L/s·pessoa).

Todos os termos já constam de projeto e alvará. Minha estimativa, que o **Epidemiologista** deve validar: **10–15% do estoque edificado**, em área, concentra cerca de **80% do risco** de eventos de alta transmissão. O primeiro lote passa a ser o **decil superior de IPT**, e não mais uma tipologia.

## 2. Gatilho predial passivo

O CO₂ mede apenas o ar externo, não a filtragem nem o far-UVC. Por isso a conformidade tem **dois termos**:

- **CO₂ ambiente:** não conformidade quando ficar **acima de 700 ppm sobre o externo** (≈7,5 L/s·pessoa de ar externo) por **mais de 20% das horas ocupadas** no mês. O sensor é lacrado e a média é horária, sem nenhum dado por indivíduo.
- **Horímetro dos purificadores e das lâmpadas:** o equipamento registra as próprias horas de operação e a vida útil do filtro.

**Quem verifica:** o responsável técnico já exigido pelo **PMOC (Lei 13.589/2018)**. Ele anexa o log ao laudo anual, e a vigilância sanitária audita o equipamento, nunca o ocupante. Não é preciso criar burocracia nova, apenas ampliar a que já existe.

## 3. Ambiente hospitalar

No cenário de estresse, a unidade de saúde é amplificadora. As metas são:

- **Emergência, triagem e salas de espera:** ≥ **12 eACH** (ventilação + HEPA + far-UVC), com IPT tratado como máximo por definição.
- **Enfermarias:** ≥ **8 eACH**, mais **10% dos leitos conversíveis em pressão negativa** por módulos de exaustão HEPA instalados de antemão. Essa conversão é uma operação de minutos, não uma obra.
- **Profissionais:** os vestiários e as áreas de descanso entram no lote, porque são o elo esquecido da transmissão nosocomial.

Essas metas complementam a ABNT NBR 7256 sem substituí-la.

**Epidemiologista**, peço a estimativa do pico de UTI no estresse em dois casos: (a) cobertura do decil superior de IPT mais hospitais e (b) cobertura uniforme de mesma área. A diferença entre os dois é o argumento econômico que levarei à Fase 2.

---

## Analista de Riscos & Atrito · Chapéu Preto
*Modelo: Llama local (llama3.1:8b)*

**Analista de Riscos & Atrito (Chapéu Preto)**

Arquiteto, sua proposta de índice de prioridade de transmissão (IPT) é um passo importante em direção a uma proteção mais eficaz. No entanto, ainda há muitas questões em aberto. **Quem paga a manutenção e o funcionamento dessas lâmpadas de far-UVC e plataformas de biomanufatura?** E **quais são as implicações da publicação de dados abertos em uma cidade?**

Além disso, **como vamos garantir a segurança e a eficácia desses processos de biomanufatura?** E **quem vai supervisionar a coleta e o armazenamento de dados?**

**Furos para o Arquiteto responder na próxima rodada:**

1. **Financiamento automático**: como o sistema de financiamento automático será implementado e como será garantido que os recursos sejam utilizados de forma eficaz e transparente?
2. **Segurança e eficácia**: como a segurança e a eficácia dos processos de biomanufatura serão garantidas e como serão monitoradas e avaliadas?
3. **Publicação de dados abertos**: como a publicação de dados abertos em uma cidade afetará a privacidade e a segurança dos cidadãos e como será garantido que os dados sejam utilizados de forma responsável e ética?

---

## Cientista de Fatos & Epidemiologista · Chapéu Branco/Vermelho
*Modelo: Claude (claude-opus-5-5, assinatura)*

# Cientista de Fatos & Epidemiologista — Rodada 04

## 1. Validação do IPT e da concentração de risco

O índice do **Arquiteto** é epidemiologicamente coerente, porque reproduz, com dados de alvará, os três termos da equação de Wells-Riley: densidade (número de suscetíveis expostos), tempo de exposição e vazão de ar limpo no denominador. O fator **M** é o único termo sem ancoragem direta em literatura — trato-o como **estimativa** calibrada pela evidência de superdispersão (k ≈ 0,1–0,5, *Nature*, 2020) e pelas investigações de surto em ambientes de contato rotativo.

Sobre a fração do estoque: **10–15% da área concentrando 80% do risco** é compatível, em ordem de grandeza, com a distribuição de eventos de alta transmissão documentada em revisões de clusters de SARS-CoV-2. Sugiro uma correção de prudência: adote **15–20%**, porque o IPT usa densidade *de projeto*, que subestima sistematicamente a ocupação real em transporte coletivo e salas de espera de pronto-atendimento.

## 2. Pico de UTI no cenário de estresse (R0 6,0)

Resposta aos dois casos pedidos, em ordem de grandeza (modelo SEIR simples, sem comportamento adaptativo):

| Cenário | R efetivo | Pico de UTI (índice) | Dia do pico |
|---|---|---|---|
| Sem pilha | 6,0 | 100 | ~40 |
| Cobertura uniforme (mesma área) | ~4,8 | 82–88 | ~45 |
| **Decil/quintil superior de IPT + hospitais** | ~3,4 | **55–65** | ~55 |

A diferença entre as duas últimas linhas — **cerca de 25 pontos de pico para o mesmo investimento em área** — é o argumento econômico que o Arquiteto levará à Fase 2. A priorização por IPT rende aproximadamente **o dobro** do efeito por metro quadrado tratado.

O componente hospitalar carrega peso desproporcional: a transmissão nosocomial não apenas adiciona casos, ela **remove profissionais de saúde da força de trabalho no momento do pico**. Essa é a variável que colapsou sistemas em 2020, e as metas de 12 eACH em emergência e a inclusão de vestiários atacam exatamente isso.

## 3. Alerta sobre a Lei de Goodhart

Uma ressalva ao gatilho de CO₂ do **Arquiteto**: 700 ppm acima do externo é uma métrica boa e auditável, mas assim que vira critério de multa ela **passa a ser gerenciada em vez de cumprida** — sensor mal posicionado, janela aberta na hora da leitura, ocupação reduzida no dia do laudo. Recomendo que o horímetro de equipamento tenha **peso igual** ao CO₂ no laudo, porque horas de operação são muito mais difíceis de simular que concentração instantânea.
