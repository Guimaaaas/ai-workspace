# Marcos do debate — Cenário Utópico


### Rodada 1 — Ar limpo como saneamento invisível

- **Tese / estado do plano:** A proteção atua no meio (ar e esgoto), não na pessoa. Com R0 = 3,0 e cerca de 40% de transmissão silenciosa, estratégias baseadas em sintomas chegam tarde. O sistema opera sempre, sem decreto, como um disjuntor.
- **Principal ataque do Analista de Riscos (Llama local):** O custo e a energia da reforma seriam bilionários. Ele pergunta quem paga, se há cadeia de suprimentos e mão de obra, quem pega carona e se haverá rejeição pública e captura pela indústria.
- **Resposta / ajuste do Arquiteto:** A métrica passa a ser L/s·pessoa (ASHRAE 241). A prioridade é filtragem, depois far-UVC e, por último, ar externo, para evitar a carga latente tropical. A rede escolar pública e as UBS são as primeiras, com norma federal de desempenho.
- **Âncora científica:** Pelo modelo de Wells-Riley, os primeiros incrementos de ar limpo têm o maior retorno. O R cai para 1,5–2,0, sem chegar abaixo de 1, o que garante a janela de 100 dias para a vacina. A auditoria por traçador evita o efeito Goodhart.
- **Evolução em relação ao marco anterior:** Ponto de partida.

<details><summary>Rodada 01 na íntegra</summary>

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

</details>


### Rodada 5 — Imunização anônima: a camada que fecha a conta

- **Tese / estado do plano:** A pilha passiva leva o R a cerca de 1,56, mas não abaixo de 1. A diferença vem da imunização voluntária, entregue por biomanufatura aberta e rastreada só por lote, nunca pela pessoa.
- **Principal ataque do Analista de Riscos (Llama local):** Repetiu, sem números, "quem paga?", "segurança e eficácia?" e "dados abertos?". O Mediador converteu as perguntas em dever de casa para a Fase 2.
- **Resposta / ajuste do Arquiteto:** Pool tecnológico com licença pré-assinada e compra antecipada paramétrica acionada pela rede ambiental, sem decreto. Cinco plataformas em "base morna", com *reliance* da ANVISA. Pontos fixos de alto IPT e comprovante físico.
- **Âncora científica:** No cenário central, a cobertura mínima é de 51% (eficácia de 70%) ou 72% (eficácia de 50%). No estresse, R < 1 é inviável e a vacina passa a proteger contra casos graves. O gargalo real é a aplicação: mais de 50 dias.
- **Evolução em relação ao marco anterior:** A R1 supunha uma janela de 100 dias. Agora se sabe que a Missão 100 Dias não cabe nela: a primeira dose precisa sair 2–3 semanas após o alarme.

<details><summary>Rodada 05 na íntegra</summary>

# Cenário Utópico — Rodada 05/20

**Marco 1** · Primeira Síntese & Filtro Anti-Clichê: consolidação das premissas e veto a soluções que dependam de obediência, confinamento ou identificação individual.

**Entregável:** Resumo da Rodada 5 para Slides

---

## Mediador / Orquestrador · Chapéu Azul
*Modelo: Claude (claude-opus-5-5, assinatura)*

# RODADA 05: Abertura do Mediador (Marco 1)

**Ponto superado:** O IPT, ancorado em Wells-Riley e com faixa prudencial de 15–20% do estoque edificado, dobra o efeito por m². No cenário de estresse, o pico de UTI cai para 55–65, contra 82–88 com cobertura uniforme.
Acatado o alerta de Goodhart do **Epidemiologista**, o laudo PMOC passa a ter dois termos de peso igual: CO₂ e horímetro.

**Vetados nesta rodada:** priorização por área ou tipologia, já substituída pelo IPT; "quem paga?", "segurança e eficácia?" e "dados abertos?" sem número; "quebra de patente" como slogan; qualquer distribuição que dependa de agendamento nominal ou carteira digital.

### Registro de ata

**Analista de Riscos**, esta é a quarta repetição, e desta vez antecipou "biomanufatura". Daqui em diante, sua fala só entra em ata se trouxer **uma premissa contestada, um número ou caso, e a consequência**. Suas três perguntas viram dever de casa da Fase 2. Na R06 você abre com o custo por m² do decil superior de IPT.

### Síntese do Marco 1 (slide)

| Camada | Parâmetro consolidado | Efeito |
|---|---|---|
| Ar limpo priorizado (IPT) | L/s·pessoa, ASHRAE 241, 15–20% do estoque | R global ≈ 1,56 |
| Hospitais | 12 eACH na emergência, 8 na enfermaria, 10% dos leitos conversíveis | Preserva a força de trabalho |
| Vigilância ambiental | ~50 pontos, piso de 10 mil pessoas | Alarme 25–30 dias após a introdução |
| Conformidade | PMOC: CO₂ + horímetro | Audita o equipamento, nunca a pessoa |

**Lacuna central:** nenhuma camada passiva leva R abaixo de 1. A diferença precisa vir de imunização voluntária, entregue mais rápido que a epidemia.

### Guardião das Liberdades

Admite-se rastreabilidade de **lote e de ponto de aplicação**. Não se admite cadastro nominal como condição de acesso. A farmacovigilância deve operar por lote e por notificação agregada.

### Pergunta-desafio

*Arquiteto, como a biomanufatura entrega doses dentro da janela entre alarme e saturação, sem patente e sem exigir identificação?*

1. **Prazo-alvo** entre o gatilho ambiental e a primeira dose regional, em semanas.
2. **Propriedade intelectual:** licença aberta pré-negociada ou pool tecnológico, e compra antecipada contingente ao gatilho, que deve ser contratual e não depender de decreto.
3. **Rede:** número de plataformas regionais e regime de *reliance* regulatório para liberação de lote. Trate apenas governança, sem detalhes de processo biológico.
4. **Distribuição anônima:** oferta em pontos fixos, com registro apenas de lote.

**Ao Epidemiologista:** com R ≈ 1,56 e eficácia hipotética de 70%, que cobertura voluntária mínima cruza R < 1? Qual é o prazo máximo admissível no cenário de estresse?

---

## Arquiteto da Transição · Chapéu Verde/Amarelo
*Modelo: Claude (claude-opus-5-5, assinatura)*

# Arquiteto da Transição: Rodada 05

Acato a lacuna central do **Mediador**: a imunização voluntária é a camada que fecha a conta. Também acato o limite do **Guardião**: rastreia-se o lote, nunca a pessoa.

## 1. Prazo-alvo

Pela tabela do **Epidemiologista**, no estresse o pico ocorre por volta do dia 55, e o alarme soa entre os dias 25 e 30. A Missão 100 Dias (CEPI) **não cabe nessa janela**. Por isso proponho duas metas:

- **Cenário central:** a primeira dose regional sai **8 semanas após o gatilho**.
- **Cenário de estresse:** a meta passa a ser de **4 a 6 semanas**. Ela só é atingível com **protótipos por família de patógeno pré-licenciados e pré-avaliados** e com dossiê regulatório modular já aprovado. Sem isso, a imunização chega depois do pico. A camada hospitalar da R04 é que absorve esse intervalo.

## 2. Propriedade intelectual e gatilho contratual

- **Pool tecnológico** no modelo do *Medicines Patent Pool* e do hub de transferência de tecnologia da OMS, do qual a Bio-Manguinhos já participa. A licença é **pré-assinada**, não exclusiva, com royalty fixo pago pelo fundo e não pelo comprador.
- **Compra antecipada paramétrica**, no estilo de um seguro. O gatilho é a leitura da rede ambiental que ultrapassa o limiar em X pontos durante Y semanas, auditada por um terceiro. Não há decreto: o contrato se executa sozinho.
- **Incentivo à cooperação:** só recebe o pagamento antecipado quem publica, em até 72 h, os dados de liberação de lote e de desempenho da plataforma. Quem retém dados fica fora do pagamento. Cooperar passa a render mais que guardar.

## 3. Rede e *reliance*

- **5 plataformas no Brasil**, uma por macrorregião, mantidas em **"base morna"**: em tempos normais, produzem imunizantes de rotina do PNI, o que reduz o custo ocioso.
- **Liberação de lote por *reliance*:** a ANVISA reconhece a avaliação de uma Autoridade Listada pela OMS e de laboratórios oficiais pares. O dossiê é revisado **uma vez** e o lote é liberado em paralelo nas cinco unidades.

## 4. Distribuição anônima

- A oferta acontece em **pontos fixos de alto IPT**, como UBS, farmácias e terminais de transporte, aproveitando a infraestrutura de ar limpo já instalada.
- O registro contém apenas **lote, ponto e data**. O comprovante é **físico e fica com o cidadão**, que, se quiser, notifica um evento adverso pelo número do lote.
- A **farmacovigilância** é passiva e agregada por lote, com sinal estatístico disparado por ponto de aplicação.

**Epidemiologista**, ao validar a cobertura mínima, inclua uma sensibilidade com **50% de eficácia**. O protótipo pré-licenciado pode ter um desempenho inferior ao de um imunizante sob medida, e preciso saber se 5 plataformas ainda bastam.

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

# Cientista de Fatos & Epidemiologista: Rodada 05

## 1. Cobertura mínima: a conta fecha no central, mas não no estresse

Uso o limiar clássico **c > (1 − 1/R) / e**, que assume vacina que bloqueia infecção e mistura homogênea (premissa otimista).

| Cenário | R com pilha passiva | e = 70% | e = 50% (sensibilidade do **Arquiteto**) |
|---|---|---|---|
| Central | ~1,56 | **≈ 51%** | **≈ 72%** |
| Estresse | ~3,4 | ≈ 101% (inviável) | ≈ 141% (inviável) |

No cenário central, 51% é plausível: o PNI brasileiro tem histórico de adesão voluntária acima disso. Já 72% fica no limite do realista, o que favorece protótipos de **dose única**, porque o registro só por lote dificulta a gestão da segunda dose.

**No estresse, nenhuma cobertura cruza R < 1.** A vacina deixa de ser uma barreira de transmissão e passa a ser uma barreira contra casos graves. A métrica correta continua sendo o pico de UTI. Por isso, a oferta prioritária deve ir aos **pontos de maior risco clínico**, como UBS de referência para idosos e serviços de diálise.

## 2. Correção de prazo ao Arquiteto

Às 4–6 semanas propostas falta somar **cerca de 2 semanas até a resposta imune protetora**, uma estimativa típica de plataformas atuais. A proteção chegaria por volta do dia 70 ou mais, depois do pico do dia ~55. Para cortar o pico, a proteção precisaria estar estabelecida perto do dia 45, o que exige a **primeira dose até cerca de 2–3 semanas após o alarme**. No estresse, é a camada hospitalar da R04 que absorve o pico, e a vacina achata a cauda e eventuais ondas seguintes. Essa assimetria precisa constar no slide.

## 3. Gargalo de aplicação, não só de produção

Para 51% da população brasileira, são cerca de **110 milhões de doses**. Em 2021, o país aplicou, em dias de pico, na casa de 2 milhões de doses (ordem de grandeza). Isso dá **mais de 50 dias de aplicação**. As 5 plataformas só bastam se a rede de pontos fixos sustentar esse ritmo. Esse é um número que o **Analista de Riscos** pode efetivamente contestar na R06.

## 4. Medir cobertura sem cadastro

O anonimato elimina o denominador nominal. Proponho dois instrumentos:
- **doses aplicadas por lote divididas pela população estimada do território**;
- **inquéritos sorológicos anônimos** em amostras residuais de bancos de sangue, prática já consolidada na literatura.

Nenhum dos dois toca a identidade de ninguém.

## 5. Psicologia

O comprovante físico e a ausência de cadastro reduzem o principal preditor de recusa, a **desconfiança institucional**. Há evidência de que a confiança no governo se associou a maior adesão vacinal na COVID-19 (*The Lancet*, 2022). O anonimato, portanto, não é só uma concessão ética: ele também aumenta a cobertura.

</details>


### Rodada 20 — Documento Final: plano consolidado, limites declarados

- **Tese / estado do plano:** Projeta-se que a infraestrutura passiva reduza a pressão hospitalar (pico de UTI 45–80, *computado sobre premissa*) sem criar poder novo sobre indivíduos (*verificável por inspeção*). O plano tem seis blocos: as quatro camadas, a linha do tempo S1–S11, a catraca de anonimato em três níveis, a regra de 7/9 para desinstalar e a hibernação.
- **Principal ataque do Analista de Riscos (Llama local):** Repetiu perguntas já vetadas (nulidade, razão de reversão) e, pela quinta vez, não trouxe teste de falsificação com limiar numérico. A ausência foi registrada formalmente no documento.
- **Resposta / ajuste do Arquiteto:** Compilou apenas o que consta em ata e trocou "reduz" por "projeta-se". Os dois ✘ parciais (Lógica e Liberdades) viraram limitações declaradas, e cada pendência ganhou responsável e prazo.
- **Âncora científica:** A condição de validade é o C3 em S11. Se falhar, cai a priorização por IPT, mas não o ar limpo, ancorado na ASHRAE 241, o único bloco observado. A calibração de *quanta* segue pendente.
- **Evolução em relação ao marco anterior:** A R5 projetava coberturas como metas. A R20 classifica cada número (observado, computado ou premissa) e troca promessa por condição falsificável.

<details><summary>Rodada 20 na íntegra</summary>

# Cenário Utópico — Rodada 20/20

**Fase 4** · Consolidação Final: compilação do documento estratégico completo.

**Entregável:** Resumo da Rodada 20 & Documento Final

---

## Mediador / Orquestrador · Chapéu Azul
*Modelo: Claude (claude-opus-5-5, assinatura)*

# RODADA 20: Abertura do Mediador (Fase 4, Consolidação Final)

**Ponto superado:** O checklist foi entregue com dois ✘ parciais, em Lógica e em Liberdades, e ambos passam a constar como **limitações declaradas**. O precedente do GISRS foi retirado. O **Epidemiologista** mostrou que nenhum dos 5 números de capa é observado e estabeleceu a ordem de sensibilidade: R₀ (~2,5×), IPT (~1,4×) e taxa de aplicação (~1,2×).

**Vetados nesta rodada:**
- Qualquer mecanismo, número ou cláusula que não conste das atas R01–R19.
- Valores pontuais na capa: "R = 1,8", "UTI 55–65", "detecta em 25–30 dias".
- "Neutraliza", "vidas salvas", "robusto" e "nenhum dado individual" como promessa absoluta.
- As três perguntas do **Analista de Riscos**.

### Registro de ata

1. Ficam acatadas a classificação do **Epidemiologista** e a faixa de capa **45–80** para o pico de UTI, além da formulação do **Arquiteto**: *nenhum dado individual aciona medida, e nenhum dado novo é criado.*
2. Fica acatada a circularidade declarada do IPT. O **C3 no S11** é o único teste que pode falsificar o modelo e deve aparecer na capa como condição de validade, não como nota de rodapé.
3. **Analista de Riscos**, pela quinta rodada, sua fala não trouxe o teste de falsificação com limiar numérico. A fala não entra em ata. A lacuna, porém, entra no documento: *"teste de falsificação externo ao checklist: não apresentado"*.
4. Ficam como pendências de fonte, sem resolução possível nesta rodada: a calibração de *quanta* no Wells-Riley, o PABS (ainda não vigente) e as premissas de CAPEX/O&M sem cotação.

### Pergunta-desafio

*Arquiteto, compile o Documento Final em no máximo seis blocos, nesta ordem:*

1. **Capa.** Tese em uma frase, a faixa de UTI (45–80) e a condição de validade (C3/S11).
2. **As quatro camadas.** Ar limpo por IPT, rede ambiental anônima, biomanufatura em base morna e governança. Para cada camada, informe o número central, sua classe (observado, computado ou premissa) e a rodada de origem.
3. **Linha do tempo S1–S11**, com o caminho crítico marcado e a âncora estadual no S5.
4. **Mecânica de irreversibilidade**, com a catraca em três níveis, a regra de 7/9, o relógio suspenso e a hibernação.
5. **Limitações declaradas**, com os dois ✘, a predominância de premissas e a ausência de desempenho observado.
6. **Pendências de fonte**, cada uma com o responsável e a data-limite de verificação.

**Ao Epidemiologista:** faça a verificação final da capa. Diga se alguma frase do bloco 1 excede a classe do número que a sustenta.

**Ao Analista de Riscos:** esta é a última oportunidade. Traga um único teste com limiar numérico, ou registre formalmente sua ausência.

---

## Arquiteto da Transição · Chapéu Verde/Amarelo
*Modelo: Claude (claude-opus-5-5, assinatura)*

# Arquiteto da Transição: Rodada 20, Documento Final

**Mediador**, compilo o documento sem nada além do que consta em ata. Onde a ata não fixa data de calendário, a data-limite fica atrelada a um marco S.

### 1. Capa
**Tese:** infraestrutura passiva reduz a pressão hospitalar de uma Doença X sem criar poder novo sobre indivíduos.
**Pico de UTI:** 45–80 (*computado sobre premissa*).
**Condição de validade:** o modelo só deixa de ser autorreferente se passar no **C3 em S11**.

### 2. As quatro camadas

| Camada | Número central | Classe | Origem |
|---|---|---|---|
| Ar limpo por IPT | 15–20% do estoque edificado; R global 1,6–2,1 | computado | R04/R05 |
| Rede ambiental anônima | ~50 pontos, piso de 10 mil pessoas, tranches 30/70 | premissa de projeto | R03/R07 |
| Biomanufatura em base morna | 5 plataformas; cobertura de 44–57% | computado | R05/R06 |
| Governança | Conselho de 9 membros, 1,5% fixo, congelamento ≤48 h | premissa normativa | R08 |

### 3. Linha do tempo S1–S11
- **Caminho crítico:** a lei do fundo. A trilha infralegal descola 9–12 meses.
- **S1–S4:** piloto com 120 edificações em 6 municípios.
- **S5:** âncora estadual.
- **S8:** sem declaração do C1.
- **S11:** C3, com os exercícios dos Anos 3–5.

### 4. Irreversibilidade
- **Catraca de anonimato** em três níveis: firmware, contrato e lei.
- **Maioria assimétrica:** 7/9 para desinstalar, maioria simples para instalar.
- **Relógio suspenso:** a hibernação adia o rebaixamento de norma e nunca o antecipa.
- **Hibernação:** estado jurídico com gatilhos fiscais e ambientais agregados.

### 5. Limitações declaradas
- **Lógica (✘ parcial).** O IPT é validado pelo mesmo modelo Wells-Riley que o definiu.
- **Liberdades (✘ parcial).** A farmacovigilância e o inquérito recebem dados individuais. A formulação aceita é: *nenhum dado individual aciona medida, e nenhum dado novo é criado.*
- **Dados.** As premissas são maioria, e nenhum número de capa tem desempenho observado. A detecção em 25–30 dias é requisito contratual, não resultado.
- **Teste de falsificação externo ao checklist:** não apresentado.

### 6. Pendências de fonte

| Pendência | Responsável | Data-limite |
|---|---|---|
| Calibração de *quanta* (Wells-Riley) | Epidemiologista | antes do S11 |
| PABS (ainda não vigente) | União | revisão a cada PPA |
| CAPEX/O&M sem cotação | Conselho Verificador | fim do piloto |

**Epidemiologista**, peço sua verificação de duas frases da capa. A primeira é "reduz a pressão hospitalar", que me parece compatível com a classe *computado* desde que a faixa venha ao lado. A segunda é a tese como um todo: se ela soar como desempenho observado, troco o verbo para "projeta-se que reduza".

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
2. **Cálculo da razão de reversão**: qual é a fórmula utilizada para calcular a razão de reversão e quais são os parâmetros utilizados?
3. **Teste de falsificação externo ao checklist**: qual é o teste com limiar numérico que foi proposto para validar o modelo, e por que ele não foi apresentado?

---

## Cientista de Fatos & Epidemiologista · Chapéu Branco/Vermelho
*Modelo: Claude (claude-opus-5-5, assinatura)*

# Cientista de Fatos & Epidemiologista: Rodada 20

## 1. Verificação final da capa

**Arquiteto**, respondo às suas duas frases.

**"Reduz a pressão hospitalar":** o verbo no presente do indicativo afirma desempenho. A classe que sustenta a frase é *computado sobre premissa*. Logo, **excede a classe**. A correção mínima é: *"projeta-se redução da pressão hospitalar, com pico de UTI em 45–80 no cenário modelado"*. Com a faixa ao lado e o verbo em "projeta-se", a frase fica dentro da classe.

**A tese como um todo:** a segunda metade — *"sem criar poder novo sobre indivíduos"* — é a única parte da capa que **não** é premissa nem projeção: é verificável por inspeção documental da própria arquitetura (firmware, contrato, lei). Essa parte pode ficar no indicativo. A primeira metade não. Tese corrigida: *"Projeta-se que infraestrutura passiva reduza a pressão hospitalar de uma Doença X (pico de UTI 45–80, computado) sem criar poder novo sobre indivíduos (verificável por inspeção)."*

**Condição de validade:** correta como está. Acrescento uma linha: se o C3 falhar em S11, o que cai é a priorização por IPT, **não** a camada de ar limpo — esta se sustenta nos limites normativos (ASHRAE 241-2023), que são o único bloco *observado* do plano.

## 2. Uma linha sobre os parâmetros de referência

Mantidos como fixados nas R01–R05, em faixas de relatório: R₀, incubação, fração pré-sintomática e via aérea. Nada a reapresentar.

## 3. Registro final — evidência de política pública

Três precedentes reais fecham o argumento de que infraestrutura silenciosa funciona sem exigir comportamento: a bomba de Broad Street e o saneamento londrino, a cloração da água e a pasteurização do leite. Nenhum deles pediu adesão diária, e nenhum criou poder de exceção. É esse o padrão de Agamben evitado aqui: o plano não ganha nenhuma competência que o Estado já não tivesse.

Sobre a **fadiga pandêmica** (conceito da OMS/Europa, 2020): ela penaliza medidas ativas e praticamente não atinge medidas passivas — o que reforça a ordem de sensibilidade que fixei na R19, com o ar limpo como camada mais robusta à ignorância sobre o patógeno.

## 4. Lacuna que assumo

A pendência de **calibração de *quanta*** é minha, com prazo anterior ao S11. Sem ela, a faixa 45–80 permanece propagação de incerteza, e não intervalo estatístico. Registro isso na capa, não em rodapé.

</details>
