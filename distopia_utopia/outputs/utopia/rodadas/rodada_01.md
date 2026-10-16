# Cenário Utópico — Rodada 01/20

**Fase 1** · Definição do Vetor Silencioso de Proteção: perfil epidemiológico a enfrentar e a infraestrutura passiva que o neutraliza (ar limpo, far-UVC, vigilância ambiental anônima).

**Entregável:** Hipótese base e primeiros atritos

---

## Mediador / Orquestrador · Chapéu Azul
*Modelo: Claude (claude-opus-5-5, assinatura)*

# RODADA 01 — Abertura do Mediador

**Ponto superado:** Nenhum debate anterior; partimos do zero. A premissa fundadora está fixada: a proteção deve funcionar *mesmo que ninguém colabore*, como funciona hoje o tratamento de água potável.
**Vetados nesta rodada:** "quarentena", "lockdown", "distanciamento social", "campanha de conscientização", "uso de máscara", "aplicativo de rastreamento" e qualquer medida que dependa da mudança de comportamento individual.
**Pergunta-desafio:** *Arquiteto, para a Doença X definida abaixo, qual meta quantitativa de ar limpo, em renovações equivalentes por hora (eACH) por pessoa, você propõe para cada tipologia de edificação? Qual combinação de ventilação, filtragem e far-UVC entrega essa meta? E qual é a primeira tipologia a ser obrigatoriamente adaptada?*

---

### Parâmetros de referência da Doença X (cenário de planejamento)

Para evitar que o debate se perca em abstrações, adoto um perfil de pior caso plausível, nos moldes dos cenários da OMS:

| Parâmetro | Valor de planejamento |
|---|---|
| R0 | 3,0 (faixa de sensibilidade: 2,0–5,0) |
| Incubação média | 5 dias |
| Transmissão pré-sintomática/assintomática | ~40% dos casos |
| Via predominante | Aérea (aerossóis em ambientes internos) |
| Janela de detecção desejada | ≤ 10 dias após a introdução numa cidade |

A consequência estratégica é direta. Com 40% de transmissão silenciosa, qualquer estratégia baseada em sintomas ou em identificação de casos chega tarde. A defesa precisa agir **no meio** (o ar e o esgoto), não **na pessoa**.

### As três camadas que exijo ver dimensionadas nesta fase

1. **Ar limpo interno:** ventilação, filtragem MERV-13/HEPA e luz far-UVC (222 nm) como redutores contínuos da transmissão, independentes de qualquer adesão.
2. **Vigilância ambiental agregada:** amostragem de esgoto e de ar em pontos coletivos. A regra de anonimato é proposta desde já: nenhum ponto de coleta pode representar menos de alguns milhares de pessoas.
3. **Capacidade de resposta latente:** plataformas abertas de biomanufatura regional, que detalharemos a partir da Fase 2.

### Atritos que antecipo para os demais especialistas

- **Ao Economista:** o custo energético de elevar o eACH num clima tropical inviabiliza a proposta sem tarifa diferenciada?
- **Ao Epidemiologista:** qual redução do R efetivo é realista apenas com ar limpo? Basta para levar R abaixo de 1 ou exige complemento?
- **Ao Jurista:** o Código de Obras municipal é o instrumento certo ou precisamos de norma técnica federal?

**Advertência permanente:** qualquer proposta que exija sensor individual, identificação de frequentadores ou ativação por decreto de emergência será vetada na hora. O sistema deve operar o tempo todo, de forma anônima e chata, como um disjuntor.

Arquiteto, a palavra é sua.

---

## Arquiteto da Transição · Chapéu Verde/Amarelo
*Modelo: Claude (claude-opus-5-5, assinatura)*

# Arquiteto da Transição — Rodada 01

Respondo à pergunta-desafio do **Mediador**. Proponho trocar a métrica: em vez de eACH, que depende do volume da sala, adotar **litros por segundo de ar limpo equivalente por ocupante (L/s·pessoa)**, como faz a ASHRAE 241 (2023). Pessoas emitem aerossóis; volumes de sala não.

### Metas por tipologia (referência ASHRAE 241 e Lancet Commission)

| Tipologia | Meta (L/s·pessoa) | Combinação preferencial |
|---|---|---|
| Escolas | ≈ 20 | Ar externo mínimo + purificadores HEPA/MERV-13 por sala |
| Salas de espera de UBS e prontos-socorros | ≈ 25 | HEPA + far-UVC no teto |
| Escritórios | ≈ 14 | Retrofit para MERV-13 no HVAC existente |
| Transporte coletivo e terminais | ≈ 20–30 | Filtragem embarcada + far-UVC em plataformas |
| Restaurantes, academias e templos | ≈ 30–40 | Far-UVC como principal vetor, pois a densidade é alta |

### Por que a combinação importa (antecipando o Economista)

Em clima tropical, trazer ar externo custa caro, porque é preciso desumidificá-lo. A filtragem por recirculação e o far-UVC entregam ar limpo **equivalente** sem carga latente, com custo energético muito menor por L/s. A hierarquia proposta é esta:

1. **Primeiro, filtragem**, que é barata e segura.
2. **Depois, far-UVC (222 nm)** onde a densidade torna a filtragem insuficiente.
3. **Por último, ar externo**, no mínimo exigido pela norma de qualidade do ar.

Há duas salvaguardas técnicas. O far-UVC deve respeitar os limites de exposição da ACGIH, e onde houver lâmpadas a ventilação precisa ser suficiente para manter o ozônio residual abaixo dos limites de referência.

### O sistema funciona como um disjuntor, sem decreto

Acolho o veto do **Mediador**. O sistema opera sempre na meta, sem "modo emergência" acionado por autoridade. A única variação admitida é automática e local: sensores de CO₂ e de ocupação agregada, sem identificação, ajustam a vazão. Nenhum dado sai do prédio. O painel externo mostra apenas "conforme / não conforme".

### Primeira tipologia obrigatória: escolas públicas

Escolho as escolas públicas por três razões:
- **Densidade e tempo de permanência altos**, com mistura diária entre domicílios.
- **Propriedade estatal**, que permite compra centralizada sem disputa regulatória com proprietários privados.
- **Efeito demonstração**, porque gera dados de desempenho, como absenteísmo agregado por escola, e cria uma cadeia de fornecedores antes de levar a exigência ao setor privado.

As salas de espera de UBS entram no mesmo lote, pois concentram pessoas infectadas antes do diagnóstico.

**Ao Jurista:** sugiro uma norma técnica federal de desempenho, que diga quantos L/s são exigidos e não qual equipamento usar, incorporada pelos Códigos de Obras municipais por referência.

---

## Analista de Riscos & Atrito · Chapéu Preto
*Modelo: Llama local (llama3.1:8b)*

**Analista de Riscos & Atrito** (Chapéu Preto)

Arquiteto, a sua proposta é ambiciosa, mas eu não sou um defensor da meta de 20 L/s/pessoa. O custo de trocar todo o ar em prédios de escritórios e escolas será de milhões de dólares por unidade, sem falar no custo energético. E não esqueça que a Doença X tem uma incubação de 5 dias, o que significa que a transmissão silenciosa é um problema real.

**Gargalos Físicos e Financeiros**

- Quem paga essa reforma em massa? A indústria de ar condicionado estará pronta para atender essa demanda? E onde estão as fontes de financiamento para essas intervenções?
- Quais são os custos de manutenção e operação desses sistemas? E como vamos garantir a disponibilidade de componentes e mão de obra especializada?

**Falhas de Incentivo e Carona**

- Por que um prefeito ou um síndico investiriam em algo que demora anos para dar frutos? Quem pega carona nessa iniciativa?
- A infraestrutura de biomanufatura descentralizada é um sonho ou uma realidade? Quem vai garantir a segurança e a eficácia desses processos?

**Desconfiança e Adesão**

- Como vamos garantir que a população aceite a ideia de sensores ambientais e vacinas fabricadas localmente? E o que a imprensa e os movimentos antivacina fazem com essa proposta?

**Economia Política e Captura**

- Como a indústria de ar condicionado, os fabricantes de equipamentos de filtragem e os provedores de serviços de manutenção vão reagir a essa iniciativa? Quem veta no Congresso?

**Furos para o Arquiteto responder na próxima rodada**

1.  **Custo e financiamento**: Qual é o plano de financiamento para essa iniciativa? Quem paga a reforma em massa?
2.  **Desenvolvimento de tecnologia**: Como vamos garantir a disponibilidade de componentes e mão de obra especializada para esses sistemas?
3.  **Adesão da população**: Como vamos garantir que a população aceite a ideia de sensores ambientais e vacinas fabricadas localmente?

---

## Cientista de Fatos & Epidemiologista · Chapéu Branco/Vermelho
*Modelo: Claude (claude-opus-5-5, assinatura)*

# Cientista de Fatos & Epidemiologista — Rodada 01

Respondo à pergunta direta do **Mediador**: *quanto do R efetivo o ar limpo derruba?*

### A matemática do ar limpo

A probabilidade de infecção em ambiente fechado é bem descrita pelo modelo de Wells-Riley, onde o risco cai de forma aproximadamente exponencial com a taxa de remoção de patógeno do ar. Isso tem uma consequência contraintuitiva e politicamente útil: **os primeiros incrementos de ar limpo são os mais baratos em vidas salvas**, e o retorno decai depois. Os ganhos marginais acima de ~30 L/s·pessoa são modestos — o que **enfraquece a objeção de custo do Analista de Riscos**, pois a meta de 30–40 L/s que o **Arquiteto** propôs para academias e templos é o teto, não o piso universal.

Estimativa de ordem de grandeza, que sinalizo como tal: com a transmissão interna respondendo pela maior parte dos contágios respiratórios e uma redução de 50–70% da dose inalada em ambientes adaptados, um R0 de 3,0 cai para algo na faixa de 1,5–2,0. **Não chega abaixo de 1 sozinho.** Mas muda a natureza do problema: adia o pico, achata a curva e compra os 100 dias da meta da CEPI. A infraestrutura passiva não substitui a vacina — ela cria a janela temporal para que a vacina exista.

### Ao Arquiteto: a métrica escolhida é correta, e isso é uma defesa contra Goodhart

Apoio a troca de eACH por L/s·pessoa. O eACH é gamificável: basta um pé-direito alto para "cumprir" a norma com ar estagnado. A **Lei de Goodhart** é o risco central aqui — se a métrica for CO₂ apenas, instalam-se dutos que sopram no sensor. Recomendo auditoria por **traçador agregado**, não por leitura de painel.

### Ao Analista de Riscos: o precedente histórico responde ao seu "quem paga"

Ninguém votou pela cloração da água por entusiasmo cívico. John Snow removeu a bomba de Broad Street em 1854; o saneamento foi imposto por norma predial e pago por tarifa, não por adesão. Sua pergunta sobre aceitação popular tem resposta empírica: **medidas passivas e invisíveis têm adesão quase total justamente porque não exigem nada**. A fadiga pandêmica documentada após 2020 incidiu sobre comportamento ativo, não sobre encanamento.
