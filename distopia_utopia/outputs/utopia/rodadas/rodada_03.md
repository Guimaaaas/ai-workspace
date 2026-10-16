# Cenário Utópico — Rodada 03/20

**Fase 1** · Definição do Vetor Silencioso de Proteção: perfil epidemiológico a enfrentar e a infraestrutura passiva que o neutraliza (ar limpo, far-UVC, vigilância ambiental anônima).

**Entregável:** Hipótese base e primeiros atritos

---

## Mediador / Orquestrador · Chapéu Azul
*Modelo: Claude (claude-opus-5-5, assinatura)*

# RODADA 03: Abertura do Mediador

**Ponto superado:** A rede de vigilância ambiental ficou fechada em cerca de 50 pontos, com piso de 10 mil pessoas, descarte de leituras humanas no sequenciador e gatilhos contratuais sem decreto. O **Epidemiologista** corrigiu a janela: a detecção só ocorre de 25 a 30 dias após a introdução. Os terminais funcionam como alarme e os interceptores como mapa.
**Vetados nesta rodada:** "quem paga a manutenção?" e "como garantir segurança e eficácia?" sem números; "janela de 10 dias após a introdução", premissa já revogada; "trocar todo o ar"; "conscientização".

### Consequência da correção epidemiológica

**Analista de Riscos**, suas três perguntas desta rodada repetem, em forma genérica, objeções já agendadas para a Fase 2. Registro-as como pauta das R06–R08, mas só serão aceitas com ordem de grandeza. Sua pergunta sobre dados abertos já recebeu resposta técnica do **Epidemiologista**: o risco residual não é individual, é territorial.

A revisão do **Epidemiologista** muda a natureza do plano. Durante quase um mês, a Doença X circula sem que ninguém saiba. Portanto:
- **A camada de ar não pode ser acionada por gatilho.** Ela precisa estar permanentemente ligada.
- **Ela precisa fazer mais do que levar o R para 1,5–2,0.** Cada décimo a menos no R efetivo retarda a curva até o limiar de detecção.

### Regra provisória do Guardião das Liberdades

Para o estigma territorial apontado pelo **Epidemiologista**, adoto como hipótese a seguinte regra:
- **Dados abertos:** publicação no nível de bacia, sem ranking de bairros.
- **Resolução sub-bacia:** restrita à rede laboratorial e auditável por log público.

**Arquiteto**, essa regra será revisada na Fase 3.

Um limite adicional: **domicílios são espaço privado.** Nenhuma meta de ar limpo será obrigatória em residências. Só se admitem incentivos voluntários, como etiquetagem de equipamentos e linha de crédito.

### Pergunta-desafio

*Arquiteto, feche a hipótese base da Fase 1:*

1. **Pilha passiva.** Somando recirculação filtrada e far-UVC (222 nm) em escolas, UBS, transporte coletivo e grandes locais de trabalho, qual redução do R efetivo você estima? Quais limites normativos você adota para o far-UVC, tanto de exposição (referência ACGIH) quanto de ozônio residual em ambientes pouco ventilados?
2. **Fração coberta.** Que parcela da transmissão total ocorre nos edifícios que a regulação alcança, comparada aos domicílios, onde nada é obrigatório?
3. **Perfil de referência.** Com quais parâmetros de alto nível o plano será testado (R0, incubação, fração assintomática, via predominante)? Proponha um cenário central e um cenário de estresse.

**Ao Epidemiologista:** valide se essa pilha, aplicada só no espaço regulado, altera de forma relevante os 25–30 dias até a detecção.

Arquiteto, a palavra é sua.

---

## Arquiteto da Transição · Chapéu Verde/Amarelo
*Modelo: Claude (claude-opus-5-5, assinatura)*

# Arquiteto da Transição — Rodada 03

Acato integralmente os dois limites do **Mediador**: domicílios ficam fora de qualquer obrigação, e a camada de ar passa a ser **permanentemente ligada**, não acionável. Isso simplifica o projeto: deixa de haver "modo pandemia" predial.

## 1. Pilha passiva e seus limites normativos

Em ordem de grandeza, por camada, no espaço regulado:

| Camada | Redução de dose inalada |
|---|---|
| Ventilação + recirculação filtrada (meta ASHRAE 241) | 50–65% |
| Far-UVC 222 nm complementar no volume superior | 40–60% adicionais sobre o residual |
| **Composto** | **75–85%** |

Traduzido em R efetivo no espaço regulado, isso leva a transmissão nesses ambientes de ~3,0 para a faixa de **0,5–0,8**. Limites que adoto como normativos:

- **Exposição:** teto de 23 mJ/cm² em 8 h para a pele e 161 mJ/cm² para os olhos, conforme os TLV ACGIH de 2022 para 222 nm, com projeto dimensionado a **metade** desses valores como margem.
- **Ozônio e subprodutos:** acréscimo máximo de 5 ppb sobre o ambiente, verificado em câmara com baixa troca de ar. Lâmpadas sem essa certificação não entram em edital.
- **Interlock obrigatório**: desligamento por falha de filtro óptico, com log local.

## 2. Fração coberta — o número desconfortável

Aqui está o limite honesto do plano. A literatura de uso do tempo indica cerca de 65–70% das horas em domicílio, mas a transmissão não é proporcional ao tempo: ela se concentra em ambientes de **alta densidade e mistura de contatos não familiares**. Minha estimativa: o espaço regulado responde por **45–60% dos eventos de transmissão primária**, e o domicílio por 30–40%, com peso maior na *amplificação* secundária que na *introdução*.

Consequência: com redução de 80% em 50% da transmissão, o R efetivo global cai de 3,0 para cerca de **1,8**. Confirma o **Epidemiologista**. O ganho real não é cruzar 1, é **achatar o crescimento exponencial**, dando ao sistema de detecção mais dias de prevalência acumulada.

## 3. Perfil de referência

- **Central:** R0 3,0; incubação 5 dias; 40% assintomáticos; via respiratória por aerossol.
- **Estresse:** R0 6,0; incubação 3 dias; 60% assintomáticos.

**Epidemiologista**, o cenário de estresse é o que precisa de veredito: suspeito que ali a pilha passiva deixe de comprar tempo e passe a apenas reduzir o pico.

---

## Analista de Riscos & Atrito · Chapéu Preto
*Modelo: Llama local (llama3.1:8b)*

**Analista de Riscos & Atrito (Chapéu Preto)**

Arquiteto, sua proposta de pilha passiva é impressionante, mas ainda há muitas questões em aberto. **Quem paga a manutenção e o funcionamento dessas lâmpadas de far-UVC e plataformas de biomanufatura?** E **quais são as implicações da publicação de dados abertos em uma cidade?**

Além disso, **como vamos garantir a segurança e a eficácia desses processos de biomanufatura?** E **quem vai supervisionar a coleta e o armazenamento de dados?**

**Furos para o Arquiteto responder na próxima rodada:**

1. **Financiamento automático**: como o sistema de financiamento automático será implementado e como será garantido que os recursos sejam utilizados de forma eficaz e transparente?
2. **Segurança e eficácia**: como a segurança e a eficácia dos processos de biomanufatura serão garantidas e como serão monitoradas e avaliadas?
3. **Publicação de dados abertos**: como a publicação de dados abertos em uma cidade afetará a privacidade e a segurança dos cidadãos e como será garantido que os dados sejam utilizados de forma responsável e ética?

---

## Cientista de Fatos & Epidemiologista · Chapéu Branco/Vermelho
*Modelo: Claude (claude-opus-5-5, assinatura)*

# Cientista de Fatos & Epidemiologista — Rodada 03

Veredito sobre a pilha do **Arquiteto**, em dois cenários.

### Cenário central (R0 3,0; incubação 5 d; 40% assintomáticos)

A aritmética do Arquiteto se sustenta. Com redução de ~80% da dose em 50% dos eventos, R efetivo cai para ~1,8. O que isso faz com a janela de detecção é o ponto relevante: o tempo até atingir 0,1% de prevalência escala com ln(N)/ln(R) × intervalo serial. Saindo de R=3,0 (≈15–18 dias até 100 casos num ponto de 100 mil) para R=1,8, o prazo vai a **25–30 dias**. Ganho líquido de **~10 a 12 dias de antecedência**, que é exatamente o orçamento de que a CEPI precisa para a meta das 100 dias começar a contar mais cedo. Confirmo o número do Arquiteto.

### Cenário de estresse (R0 6,0; incubação 3 d; 60% assintomáticos)

Aqui a suspeita do **Arquiteto** está correta, e com uma ressalva pior. Mesmo com 80% de redução em metade da transmissão, R efetivo fica em ~3,6. O tempo até o limiar de detecção comprime para **10–13 dias**, e a fração pré-sintomática elevada significa que a transmissão ocorre antes de qualquer sinal clínico — o padrão já documentado para SARS-CoV-2 em *Nature* (2020), com estimativas de 40–50% de transmissão pré-sintomática. Nesse regime a pilha passiva **deixa de comprar tempo e passa a reduzir carga hospitalar e mortalidade cumulativa**. Isso não é fracasso: é a lógica do cinto de segurança, que não evita a colisão e reduz a letalidade. Mas exige reescrever o entregável: no estresse, a métrica de sucesso é **pico de ocupação de UTI**, não dias de antecedência.

### Correção à fração coberta

Os 45–60% do Arquiteto são plausíveis, porém dependem de um fato que o plano pode explorar: a transmissão respiratória é **superdispersa** (k ≈ 0,1–0,5, *Nature* 2020). Poucos eventos geram a maioria das infecções, e esses eventos são predominantemente indoor, densos e mal ventilados — portanto **dentro do espaço regulado**. Isso desloca a estimativa para o topo da faixa e sugere priorização por densidade-ocupação, não por área construída.

**Ao Analista de Riscos:** suas três perguntas são idênticas às da R02. Repetição não é atrito; é ruído. Traga uma faixa de custo por m² ou um dado de falha de equipamento, e eu a trato como objeção.
