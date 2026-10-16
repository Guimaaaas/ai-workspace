# A Arquitetura Silenciosa da Imunidade Planetária
**Classificação**: Cenário Utópico
**Eixo Exclusivo**: "Da forma mais silenciosa e não-invasiva"
**Contexto**: Preparação para a próxima pandemia, preservando integralmente as liberdades civis
**Modelos**: Remoto (Claude (claude-opus-5-5, assinatura)) + Local (Llama local (llama3.1:8b) via Ollama)
**Iterações**: 20 turnos de deliberação multiagente
**Compilado em**: 07/10/2026

---


## 1. Resumo Executivo

O plano propõe uma camada de proteção pandêmica que **não pede nada à população**: nem adesão diária, nem cadastro, nem suspensão de direitos. Ela funciona como a cloração da água ou a norma predial de incêndio. Tem quatro componentes:
- **Ar limpo** em edificações priorizadas pelo Índice de Prioridade de Transmissão (IPT), com meta em L/s·pessoa conforme a ASHRAE 241-2023.
- **Far-UVC 222 nm** onde a densidade de ocupação o justifica, dentro dos limites ACGIH.
- **Vigilância ambiental** em esgoto e terminais, anônima por construção.
- **Biomanufatura em base morna**, com pool de licenças pré-assinado e compra paramétrica acionada por contrato, sem decreto.

Projeta-se que, no cenário modelado, essa infraestrutura reduza a pressão hospitalar de uma Doença X, com pico de UTI na faixa de **45–80**. Esse valor é *computado sobre premissa*, não observado. O plano não leva o R abaixo de 1 por si só. Ele desloca o pico, reduz a área sob a curva e preserva a força de trabalho hospitalar.

A adesão não depende de convencimento, porque a proteção entra pelo **habite-se, pelo laudo PMOC e pelo contrato público**. O financiamento separa duas lógicas:
- **Custo-efetividade sanitária**, paga pelo FNS em escolas, salas de espera de UBS e transporte. Ela só se sustenta com co-benefícios interpandêmicos (influenza, VSR e, nas UBS, tuberculose).
- **Retorno fiscal e produtivo**, pago pelo município via IPTU em condomínios privados.

O problema do carona é tratado de três formas:
- Parcelamento 60/40, com a parcela de 40% condicionada aos dois termos do laudo (CO₂ e horímetro).
- Bônus regional proporcional à fração de municípios conformes.
- Cláusula de restituição com teto provisório de 0,6% da RCL, ou 0,3% no quintil crítico.

O caminho crítico é a lei do fundo. Uma trilha infralegal paralela descola de 9 a 12 meses do cronograma.

O estado final não é "imunidade" no sentido clínico. É uma **proteção estrutural difícil de reverter por conveniência política e reversível apenas por evidência**:
- A desinstalação exige maioria de 7/9 do Conselho Verificador e um substituto de eficácia igual ou superior.
- A hibernação orçamentária suspende o relógio de rebaixamento de norma e nunca o antecipa.
- O anonimato é uma catraca de mão única gravada em firmware, contrato e lei.

A condição de validade é explícita. O modelo só deixa de ser autorreferente se passar no **critério C3, testado no S11**. Se ele falhar, cai a priorização por IPT, mas não a camada de ar limpo, que se apoia em limites normativos.

## 2. Vetores Sistêmicos de Proteção Silenciosa

- **Vetor Epidemiológico.** Os parâmetros de planejamento são:
  - **Cenário central:** R₀ 3,0, incubação de 5 dias, cerca de 40% de transmissão pré-sintomática ou assintomática, via predominante aérea em ambientes internos.
  - **Cenário de estresse:** R₀ 6,0, incubação de 3 dias, 60% de assintomáticos.

  Com transmissão silenciosa alta, qualquer estratégia baseada em sintomas chega tarde. A defesa precisa agir no meio (o ar e o efluente), não na pessoa.

  A detecção ambiental só é plausível de 25 a 30 dias após a introdução. Esse número é um *requisito de projeto*, não um desempenho medido. Por isso o indicador relevante é a distância, em dias, entre o alarme e a saturação hospitalar.

  A transmissão é superdispersa (k ≈ 0,1–0,5). Isso concentra o risco em poucos ambientes densos, mal ventilados e de contato rotativo, justamente os que a regulação alcança.

  No estresse, nenhuma cobertura vacinal leva o R abaixo de 1. A métrica de sucesso passa a ser o **pico de UTI**. A sensibilidade do resultado é dominada pelo R₀ (cerca de 2,5×), seguido do IPT (cerca de 1,4×) e da taxa de aplicação (cerca de 1,2×).

- **Vetor de Infraestrutura Passiva.**
  - **Ar limpo:** a pilha de filtragem com far-UVC reduz a dose inalada em 75–85% no espaço regulado, levando a transmissão local para R de 0,5 a 0,8. Ela é permanentemente ligada, sem "modo pandemia".
  - **Prioridade de cobertura:** a meta é de 15–20% do estoque edificado ranqueado pelo IPT = (D × H × M)/Q, calculado só com dados de alvará.
  - **Hospitais:** 12 eACH na emergência, 8 na enfermaria, 10% dos leitos conversíveis em pressão negativa e inclusão de vestiários.
  - **Rede ambiental:** cerca de 50 pontos por metrópole de 10 milhões de habitantes. Os terminais funcionam como alarme e os interceptores como mapa. O sequenciamento é metagenômico não direcionado, com contraprova em 72 h.
  - **Biomanufatura:** 5 plataformas macrorregionais produzem a rotina do PNI em tempos normais. A meta de cobertura voluntária é de 44–57%, e o gargalo é a aplicação (mais de 50 dias), não a produção.

- **Vetor Normativo.**
  - **Norma de desempenho:** ABNT, em L/s·pessoa, sem indicar marca nem equipamento. Ela é incorporada aos códigos de obras por **lei municipal remissiva à "NBR vigente"**, de modo que revogá-la exija lei.
  - **Conformidade:** o PMOC (Lei 13.589/2018) passa a ter dois termos de peso igual, CO₂ e horímetro. O denominador é a lotação de projeto.
  - **Transparência:** contratos, laudos e liberação de lote em padrão OCDS.
  - **Licenciamento:** pool tecnológico pré-licenciado com cláusula *grant-back*.
  - **Consórcios:** consórcios públicos (Lei 11.107/2005), aviso prévio de uma temporada respiratória para retirada e âncora estadual subsidiária no S5.

- **Vetor Econômico.**
  - **Pagadores:** FNDE e FNS financiam as linhas públicas, as concessões cobrem o transporte, o IPTU cobre o setor privado e a União cobre a cooperação internacional. O fundo é ressalvado da limitação de empenho.
  - **Estoque de reserva:** gira em FIFO pela reposição das UBS. O VMI fica limitado a 40% por fornecedor.
  - **Rede ambiental:** a razão de reversão própria cruza 1 no Ano 6. A hibernação a 26 amostras é a âncora de sobrevivência mais barata.
  - **Cooperação internacional:** reciprocidade agregada no modelo PABS (ainda em negociação) e 20% da capacidade reservada, alocada por população. A contribuição em espécie é ponderada por população coberta e fluxo de entrada.

- **Vetor de Garantias Civis.**
  - **Pisos de agregação:** piso de 10 mil pessoas por ponto e descarte de leituras humanas no sequenciador. A publicação exige agregação mínima de 3 bacias, inclusive sob gatilho.
  - **Proibições:** é vedada a amostragem predial e domiciliar. Também são vedados PNR, câmeras, contagem por Wi-Fi e cadastro nominal como condição de acesso.
  - **Rastreabilidade:** só por lote e ponto de aplicação, com comprovante físico em poder do cidadão.
  - **Nulidade:** a legitimidade é difusa (MP, Defensoria, ANPD, Conselho e ação popular).
  - **Limitação declarada:** farmacovigilância e inquérito recebem entradas individuais. A formulação aceita é: *nenhum dado individual aciona medida, e nenhum dado novo é criado.*

## 3. Roadmap Passo a Passo (Do Ano 0 à Autossustentação)

- **Marco 1 (Ano 0: Normas técnicas e pilotos)**
  - **Trilha legal (caminho crítico):** o projeto de lei do fundo é protocolado no mês 0, com 1,5% fixo para o Conselho Verificador e ressalva da limitação de empenho. Na hipótese central, a sanção ocorre no T4.
  - **Trilha infralegal paralela:** corre sem esperar a lei e descola de 9 a 12 meses do caminho crítico.
    - Consulta pública da revisão do PMOC por portaria do MS, com dois termos (CO₂ e horímetro) e denominador na lotação de projeto.
    - Instalação da Comissão de Estudo ABNT para a norma em L/s·pessoa.
    - Portaria de qualificação das 5 plataformas em base morna, sem compra.
    - Edital OCDS dos 12 primeiros pontos ambientais, em bacias com pelo menos 10 mil habitantes, custeado por fonte já existente do FNS.
  - **Piloto de ar limpo:** 120 edificações de alto IPT (escolas e salas de espera de UBS) em 6 municípios, com orçamento de R$ 34–42 milhões. A unidade de cadastro é o CNPJ e o projeto aprovado, nunca o ocupante. O ponto elétrico e o suporte de far-UVC são pré-instalados na obra de filtragem (cerca de R$ 15/m²), condição para a instalação em 72 h após um alarme.
  - **Protocolos de base:**
    - Publicação das notas pré-registradas para alarme, lote O/E > 2 e *hash* contestado.
    - Regra de virada clínica do retro-teste sazonal fixada *ex ante*.
  - *Encadeamento:* o Ano 0 cria os instrumentos (norma, contrato e linha de base) que permitem medir antes de escalar.

- **Marco 2 (Ano 2: Escala nos prédios e no saneamento)**
  - **Governança:** a lei do fundo destrava a receita vinculada e permite empossar o Conselho Verificador, que passa a validar a contraprova de 72 h. Sem ele, o gatilho em duas tranches (30/70) não opera.
  - **Rede ambiental:** sobe de 12 para 30 e depois 40 pontos.
  - **Validação da rede:**
    - O **retro-teste sazonal nº 1** compara o alerta ambiental com a virada do SIVEP-Gripe e exige antecipação de 7–10 dias.
    - No T8 ocorre o primeiro *spike-in* cego, com 4 injeções em bacias distintas, sob laboratório estrangeiro sorteado. Ele é rotulado como **teste de integridade da cadeia**, não como medição de sensibilidade.
  - **Avaliação bifurcada do piloto:**
    - Falha de projeto acima de 15% trava a expansão e ativa o Ramo B: revisão do texto de vazão e novo piloto de 60 edificações.
    - Falha de operação acima de 30% aciona requalificação contratual sem travar a expansão.
  - **Norma e financiamento:** a NBR entra em consulta nacional e a matriz IPTU entra nas LOAs municipais.
  - *Encadeamento:* o piloto do Marco 1 fornece os laudos que decidem o ramo, e a lei fornece o Conselho que torna o gatilho auditável. A escala só começa sobre dados próprios.

- **Marco 3 (Ano 5: Proteção embutida no cotidiano)**
  - **S5:** começa a parcela de 40%, condicionada aos dois termos do laudo, com cláusula de restituição sob teto provisório. A expansão atinge 5% do estoque pelo IPT.
  - **S5, âncora estadual (caminho crítico):** o estado entra como subsidiário para os pontos aeroportuários isolados. A tolerância da série é de 1 temporada para a operação e 0 lacunas consecutivas para o C3, o que não admite a janela de vulnerabilidade dos Anos 4–5.
  - **S6:** a NBR é publicada e 8 capitais aprovam lei remissiva à "NBR vigente", com vigência para alvarás novos em 180 dias.
  - **S7:** o estoque coberto chega a 10%, e sai o primeiro habite-se com laudo em L/s·pessoa.
  - **S8:** a rede completa cerca de 50 pontos, chega à 10ª injeção acumulada e publica a primeira sensibilidade **com IC 95%**, sem declarar critério.
  - **S9:** o critério de detecção é testado com o IC já disponível.
  - **S10:** Ramo A chega a 20%, Ramo B a 15%. O Ramo B declara o efeito modelado de 4 a 6 pontos no pico de UTI, abaixo do poder de medição, sem afirmar suficiência.
  - **Proteção da rede no ciclo eleitoral:**
    - Aviso prévio de retirada de uma temporada completa, que eleva a razão para cerca de 1,14 no ano 4 do PPA.
    - Hibernação a 26 amostras como estado jurídico com duração máxima de 1 temporada.
  - **Custos:** o custo por amostra cai de cerca de R$ 2.500 para cerca de R$ 1.400 (premissa).
  - *Encadeamento:* a norma validada no Marco 2 entra no código de obras. A partir daí, a proteção deixa de depender de convênio e passa a depender do alvará, cuja revogação exige lei.

- **Marco 4 (Ano 10: Autossustentação e resistência à captura)**

  As atas não fixam um calendário semestral além do S11. Este marco é definido por **critérios**, não por data.
  - **S11:**
    - Teste do critério fiscal, com receita igual ou superior a 1,1× o carregamento nos exercícios dos Anos 3–5, incluindo um ano de pico sazonal.
    - Convergência dos ramos A e B em 20% do IPT.
    - Primeira janela possível da condição de validade C3.
  - **Rede ambiental:** a razão de reversão própria cruza 1 no Ano 6 (1,06) e chega a cerca de 1,18 no Ano 8, com custo de cerca de R$ 850 por amostra, **sem co-financiamento externo**. A métrica contratual é R$ por ponto-temporada, com piso de 26 amostras.
  - **Declaração de autossustentação**, que exige três condições simultâneas:
    1. Critério fiscal cumprido.
    2. Pelo menos 15% do estoque pelo IPT com laudo válido e retenção de 80% em 24 meses.
    3. Sensibilidade de pelo menos 90% e especificidade de pelo menos 95% em painel cego, por dois exercícios.
  - **Se apenas dois critérios forem cumpridos:** o critério falho recebe dois exercícios sob financiamento-ponte da União, limitado a 40%. Se falhar de novo, a linha é reprojetada, e nenhuma outra linha pode compensá-la.
  - **Resistência à captura:**
    - Catraca do anonimato em firmware, contrato e lei.
    - Pool irrevogável com *grant-back*.
    - Rebaixamento de norma apenas por C1+C2+C3, com quórum de 7/9 e substituto não identificatório.
    - Relógio suspenso em temporada hibernada.
  - *Encadeamento:* a infraestrutura embutida no Marco 3 gera as séries de três temporadas que tornam a norma **reversível por evidência e irreversível por conveniência**. Esse é o ponto de autossustentação.

## 4. Matriz de Fricções Superadas (Diálogo Arquiteto vs Analista de Riscos)

O Analista de Riscos repetiu suas objeções em quase todas as rodadas, em geral sem ordem de grandeza. Por isso, a maior parte delas não entrou em ata como formulada. As cinco abaixo continham uma objeção legítima de fundo. O Mediador a extraiu, e a solução foi construída pelo Arquiteto, com correções do Epidemiologista.

| # | Furo apontado pelo Analista | Rodada de origem | Solução consolidada (Arquiteto, com correções) | Rodada da solução | Status em ata |
|---|---|---|---|---|---|
| 1 | **Quem paga a reforma em massa e a manutenção** do ar limpo e dos equipamentos | R01 (reiterado R02–R08) | Matriz de viabilidade com CAPEX/OPEX por linha e pagador distinto: FNDE (escola), FNS (UBS), concessão (transporte), IPTU (condomínio). Duas colunas separadas, R$/DALY e retorno fiscal. Fundo ressalvado da limitação de empenho (LRF, art. 9º). Tarifa diferenciada de energia rejeitada (impacto < 0,1%) | R09–R11 | Resolvido; valores são *premissa* |
| 2 | **Dados abertos, privacidade e uso ético** dos dados ambientais | R02 (reiterado R03–R07) | Publicação em faixas e com atraso. Agregação mínima de 3 bacias, mantida sob gatilho. Descarte de leituras humanas no sequenciador. Bloqueio de ataque por diferença (< 10 mil pessoas). Recompensa por reidentificação. Risco residual estimado < 10⁻⁴ por pessoa·ano | R06–R09 | Resolvido; risco residual é *estimativa adversarial* do Arquiteto |
| 3 | **Segurança e eficácia da biomanufatura** e quem a supervisiona | R02 (reiterado R03–R08) | Escopo restrito a governança: *reliance* regulatório para liberação de lote, certificado publicado em 72 h (OCDS), farmacovigilância por lote em dois degraus O/E (> 1 ao regulador, > 2 público em 7 dias), janela de 42 dias e notas pré-registradas | R05–R07 | Resolvido |
| 4 | **Garantia de investimento e problema do carona** entre prefeitos e síndicos | R09 (reiterado R10–R18) | Parcelamento 60/40, com a parcela de 40% condicionada a CO₂ e horímetro. Bônus regional proporcional, com acelerador acima de 80% (corrige o "tudo ou nada"). Cláusula de restituição com teto de 0,6% da RCL (0,3% no quintil crítico), parcelada em 60 meses | R09, R14–R15 | Resolvido; teto provisório, com revisão no S5 |
| 5 | **Justificativa da contribuição internacional de 0,005% do PIB** | R11 | O valor passa a ser derivado do custo do ativo: 10 a 15 pontos aeroportuários vizinhos, selecionados por fluxo de entrada. O crédito em espécie é ponderado por população coberta × fluxo. A justificativa por *benchmark* foi vetada | R11–R12 | **Única célula do Analista registrada em ata** |

**Fricções não superadas, registradas como lacuna:**
- **Falhas humanas ou técnicas** na mecânica de irreversibilidade (R19). Foram levantadas sem número e respondidas apenas indiretamente: interlock do far-UVC, espectrorradiometria por lote e reversão automática ao último *build* auditado.
- **Teste de falsificação externo ao checklist** (R19–R20). Não foi apresentado e consta do documento como ausência formal.
- **Custo de reversão e fórmula da razão** (R16–R19). Foram respondidos pelas tabelas decompostas das R17–R18, mas reapresentados pelo Analista sem considerar essa resposta.

## 5. Fundamentação Científica, Precedentes e Fontes

As referências abaixo foram citadas pelo Cientista de Fatos & Epidemiologista ao longo do debate. Itens marcados **[estimativa]** foram sinalizados como ordem de grandeza. Itens marcados **[a conferir]** dependem de verificação no documento original ou na versão vigente.

**Modelagem da transmissão aérea**
- Modelo de **Wells-Riley**: o risco cai de forma aproximadamente exponencial com a taxa de remoção do patógeno, com retorno marginal decrescente acima de cerca de 30 L/s·pessoa. A calibração de *quanta* é **pendência de fonte**, sob responsabilidade do Epidemiologista, antes do S11.
- **Superdispersão** da transmissão respiratória, k ≈ 0,1–0,5 (*Nature*, 2020).
- **Transmissão pré-sintomática** de 40–50% no SARS-CoV-2 (*Nature*, 2020).
- Redução do R para 1,5–2,0 com ar limpo, tabela SEIR de pico de UTI e diferença de 4–6 pontos entre 15% e 20% do IPT. **[estimativa; computado, não observado]**

**Ar limpo e desfechos interpandêmicos**
- Mendell et al. (*Indoor Air*, 2013): queda de 1,6–2,5% nas faltas por doença para cada L/s·pessoa adicional.
- Escombe et al. (*PLoS Medicine*, 2007): risco de transmissão de tuberculose em salas mal ventiladas.
- Reichert et al. (*NEJM*, 2001): vacinação escolar contra influenza no Japão e mortalidade excedente em idosos. Fundamenta o efeito indireto da linha escolar.
- Frações do DALY por influenza, VSR e tuberculose em cada linha, e incidência média nacional de TB de cerca de 35–40/100 mil. **[estimativa; calibrar com SIM, SINAN e SIVEP-Gripe]**

**Vigilância ambiental**
- Detecção de poliovírus em esgoto em **Londres e Nova York (2022)** sem caso clínico notificado. Também se cita o uso histórico da vigilância de águas residuais na certificação de erradicação da pólio.
- Antecipação de 4–7 dias sobre a notificação clínica e limiar de 0,01–0,1% de prevalência para ensaios direcionados. Foram citados apenas como "vários estudos em *Nature* e revistas de saúde ambiental", sem referência individual. **[estimativa; a conferir]**
- Perda de 1–2 ordens de grandeza na sensibilidade da metagenômica não direcionada. **[estimativa]**
- Painéis de proficiência externa (EQA) da OMS para redes de poliovírus e influenza, como modelo do *spike-in* cego.
- **GISRS/OMS**: cadência semanal como padrão de reporte. O suposto precedente de redução para cadência quinzenal após 2010 foi **retirado** na R19 por falta de fonte.

**Economia da saúde**
- Limiar de referência da **Conitec** (2022) de cerca de R$ 40 mil/QALY, até 3× em condições graves. **[a conferir no relatório vigente]**
- Marani et al. (*PNAS*, 2021): probabilidade anual de cerca de 2% de um evento da escala da Covid.
- Diária de UTI paga pelo SUS na Covid, cerca de R$ 1.600. **[estimativa]**
- Missão 100 Dias (CEPI), como referência de prazo para imunizantes.

**Confiança, farmacovigilância e comportamento**
- **Dengvaxia, Filipinas (2017)**: queda ampla da cobertura de rotina após comunicação de risco sem taxa de fundo.
- Crise do **MMR pós-Wakefield**: dano duradouro à confiança vacinal.
- COVID-19 National Preparedness Collaborators (*The Lancet*, 2022), análise de 177 países: confiança no governo e confiança interpessoal associadas a menores taxas de infecção e a maior adesão vacinal.
- *Vaccine Confidence Project* (Larson), como inspiração do inquérito trimestral anônimo.
- **Fadiga pandêmica** (OMS/Europa, 2020): incide sobre medidas ativas, não sobre medidas passivas.
- Poder do inquérito: cerca de 500–550 entrevistas por macrorregião para detectar queda de 10 p.p. **[estimativa]**

**Precedentes históricos e marcos conceituais**
- **John Snow e a bomba de Broad Street (1854)** e o saneamento londrino.
- **Cloração da água** e **pasteurização compulsória do leite**: proteção imposta por norma, com risco de "amnésia de sucesso".
- Normas prediais de incêndio e cinto de segurança, como analogias de habituação.
- **Lei de Goodhart**, aplicada a CO₂, R$/amostra, contagem de alarmes falsos e unanimidade do Conselho.
- **Agamben, estado de exceção**: critério para vetar prorrogações "por urgência".

**Normas técnicas e jurídicas de apoio** (citadas majoritariamente pelo Arquiteto e detalhadas nos Blocos 2 e 3): ASHRAE 241-2023, TLV ACGIH para 222 nm, ABNT NBR 7256, Lei 13.589/2018 (PMOC), Lei 11.107/2005, LRF art. 9º, CF art. 167, padrão OCDS, licença CERN-OHL-S, Fundo Rotatório da OPAS, *Medicines Patent Pool* e o anexo PABS do Acordo Pandêmico da OMS, este **ainda em negociação, não vigente**.

## 6. O Diferencial Criativo

O mecanismo mais engenhoso do debate é a **assimetria de reversão**. A proteção é fácil de instalar e cara de desinstalar. O anonimato, por sua vez, não pode ser desinstalado de forma alguma. Nenhum plano de preparação vigente combina essas duas regras. Juntas, elas permitem que a proteção opere sem pedir nada ao cidadão e sem dar ao Estado nada de novo sobre ele.

**Como funciona, em quatro peças encadeadas:**

1. **Entrada pelo alvará, não pela vontade (R13–R14).** A exigência de ar limpo em L/s·pessoa entra no código de obras por lei municipal remissiva à "NBR vigente". O cidadão nunca escolhe, assim como não escolhe o cloro da água nem o sprinkler. Revisões técnicas não exigem nova votação, mas a revogação exige lei. A adesão deixa de ser um problema de comportamento e passa a ser uma condição do habite-se.

2. **Ativação por contrato, não por decreto (R02, R06).** O alarme ambiental, confirmado por contraprova em outra macrorregião, executa sozinho a compra paramétrica em duas tranches (30/70). Nenhuma autoridade "declara" nada, e nenhum direito é suspenso. O falso positivo custa apenas o prêmio da opção, por isso o gatilho pode ser sensível sem ser perigoso.

3. **Saída só por evidência e com substituto (R16–R18).** Rebaixar um requisito exige três condições cumulativas, C1, C2 e C3, mais quórum de 7/9 do Conselho Verificador. A exigência de substituto (C2) transforma o pedido de corte em pedido de troca tecnológica. Esse substituto não pode ser identificatório. O **relógio suspenso** fecha a última brecha: uma temporada em hibernação orçamentária adia a elegibilidade para afrouxar a norma e nunca a antecipa. Apertar o orçamento, portanto, não abre caminho para desproteger.

4. **Anonimato como catraca de mão única (R16).** O piso de 10 mil pessoas e o descarte de leituras humanas no sequenciador estão gravados em três camadas: firmware com *hash* publicado e suspensão automática de pagamento em caso de divergência, contrato com nulidade de pleno direito e lei do fundo que diz "só podem ser elevados". Qualquer cidadão pode acionar a nulidade por ação popular.

**Por que é imperceptível.** O cidadão não baixa aplicativo, não apresenta comprovante, não muda rotina e não é contado. A única interface visível é um painel predial "conforme / não conforme", que audita o equipamento, nunca o ocupante. A proteção habita o forro, o duto, o esgoto e o contrato. Ela também se protege da "amnésia de sucesso", a indiferença orçamentária que atinge toda proteção invisível quando a doença desaparece.

## 7. Auditoria pelos Critérios de Avaliação

| # | Critério | Nota | Justificativa |
|---|---|---|---|
| 1 | Passo a Passo Lógico e Conectado | **7/10** | Cada marco tem predecessor, responsável, instrumento e marco verificável, com caminho crítico na lei do fundo e trilha infralegal paralela. Há, porém, uma circularidade declarada: o efeito do IPT é validado pelo mesmo modelo Wells-Riley que o definiu, e só o C3 no S11 a rompe. O Marco 4 é definido por critérios, sem calendário além do S11. |
| 2 | Dados e Especialistas que Corroboram | **6/10** | Cita ASHRAE 241-2023, TLV ACGIH, *Nature* (2020), *The Lancet* (2022), *PNAS* (2021), *NEJM* (2001), *Indoor Air* (2013), *PLoS Medicine* (2007), painéis EQA e GISRS da OMS, e precedentes reais (Broad Street, cloração, Dengvaxia, Wakefield). Contudo, nenhum dos 5 números de capa é observado, as premissas são maioria nas atas, a vigilância de esgoto para respiratórios não traz referência individual e CAPEX/O&M não têm cotação. Uma afirmação (GISRS pós-2010) foi retirada por falta de fonte. |
| 3 | Robustez e Credibilidade | **8/10** | O plano resiste a desconfiança (notas pré-registradas, voto vencido publicado, recompensa por refutação, reprodução estrangeira sorteada), a orçamento apertado (hibernação a 26 amostras, aviso prévio de uma temporada, âncora estadual no S5, razão própria acima de 1 no Ano 6) e ao ciclo eleitoral (remissão legal, restituição com teto). A camada vacinal segue sensível à logística de aplicação, e nenhum teste de falsificação externo ao checklist foi apresentado. |
| 4 | Criatividade e Diferenciação | **9/10** | Não recorre a lockdown, passaporte sanitário nem campanha de conscientização. Mecanismos originais: IPT por tempo-pessoa a partir de dados de alvará, gatilho paramétrico sem decreto, catraca de anonimato em três níveis, relógio suspenso e critério de saída com substituto obrigatório. Desconta-se um ponto porque vários componentes isolados (ASHRAE 241, vigilância de esgoto, pools de licenças) já existem. A novidade está na arquitetura que os une. |
| 5 | Garantia de Liberdades | **8/10** | A vigilância ambiental, o ar limpo e todos os gatilhos operam sobre dados agregados ou da edificação. PNR, câmeras, contagem por Wi-Fi, amostragem predial e cadastro nominal ficam vetados, e não há poder de exceção. O ✘ parcial é declarado: a farmacovigilância e o inquérito recebem entradas individuais. Elas são agregadas antes de qualquer uso, usam o fluxo de notificação já existente e não acionam medida sobre ninguém. |

**Nota média: 7,6/10.**

**Limitações declaradas:**
- **Lógica.** A priorização por IPT só deixa de ser autorreferente se passar no C3 em S11. Se falhar, cai a priorização, mas não a camada de ar limpo, que se apoia em limites normativos.
- **Dados.** As premissas predominam e o desempenho sanitário não foi observado. A detecção em 25–30 dias é requisito contratual, e o pico de UTI de 45–80 é propagação de incerteza, não intervalo estatístico, até a calibração de *quanta*.
- **Liberdades.** A formulação aceita é a parcial, não a absoluta: *nenhum dado individual aciona medida, e nenhum dado novo é criado.*
- **Dependências externas.** O PABS ainda está em negociação e não é vigente. O teto de restituição de 0,6% da RCL (0,3% no quintil crítico) é provisório, com revisão no S5.
- **Atrito ausente.** O teste de falsificação externo ao checklist não foi apresentado pelo Analista de Riscos e fica registrado como lacuna formal do documento.
