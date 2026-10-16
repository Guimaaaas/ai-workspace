# Cenário Utópico — Rodada 11/20

**Fase 2** · Dinâmica Econômica e Incentivos: quem paga o ar limpo, como alinhar prefeitos, síndicos, indústria e países pobres, e como vencer o problema do carona.

**Entregável:** Matriz de viabilidade orçamentária

---

## Mediador / Orquestrador · Chapéu Azul
*Modelo: Claude (claude-opus-5-5, assinatura)*

# RODADA 11: Abertura do Mediador (Fase 2, Incentivos)

**Ponto superado:** O estoque de reserva gira em FIFO pela reposição das UBS. O VMI fica limitado a 40% por fornecedor, com espectrorradiometria por lote na ativação. O **Epidemiologista** separou a custo-efetividade sanitária (FNS) do retorno fiscal (IPTU) e condicionou o far-UVC em UBS à incidência municipal de tuberculose.

**Vetados nesta rodada:**
- *payback* único que some absenteísmo e DALY;
- condomínio financiado pelo FNS;
- comparação com hospital de campanha permanente;
- "solidariedade internacional", "ajuda humanitária" e "transferência de tecnologia" sem instrumento, valor e prazo;
- as três perguntas do **Analista de Riscos**, vetadas desde a R09.

### Registro de ata

Ficam acatadas quatro decisões:
1. A matriz terá **duas colunas**: R$/DALY, a cargo do FNS, e retorno fiscal e produtivo, a cargo do município.
2. O far-UVC em UBS fica restrito a municípios com incidência de tuberculose acima da média nacional. Nos demais, só filtragem.
3. O ensaio na ativação mede o **filtro óptico**, não o bulbo.
4. O custo de carregamento passa a ser comparado ao **leito marginal montado em 21 dias**.

**Guardião das Liberdades:** o critério de tuberculose é aceito porque usa incidência agregada. Há uma condição: em municípios com menos de 10 casos por ano, o indicador sobe para a **região de saúde**, para evitar reidentificação. Nenhuma camada do plano pode usar geolocalização de casos.

**Analista de Riscos**, seu turno ficou fora da ata pela quinta vez. A partir desta rodada, ele só será registrado se atacar uma **célula numérica identificada**. Sugiro duas:
- a fração de 55–65% de tuberculose na UBS;
- o piso de 10 casos acima.

### Pergunta-desafio

*Arquiteto, a matriz doméstica está fechada. Falta o carona internacional. Um país sem espaço fiscal se beneficia da nossa detecção e do nosso pool de licenças sem contribuir. Entregue:*

1. **Reciprocidade:** como condicionar o acesso ao pool de licenças à contribuição de sequências ambientais **agregadas**, no modelo do sistema PABS do Acordo Pandêmico da OMS. Especifique o formato do dado e a latência máxima.
2. **Escala de contribuição:** qual percentual do PIB ou do gasto em saúde cabe a cada faixa de renda. Diga também se a contribuição pode ser paga **em espécie**, com pontos de coleta ou capacidade fabril.
3. **Capacidade reservada:** qual fração das 5 plataformas fica reservada a países de baixa renda e a que preço (custo mais margem fixa).
4. **Nova linha na matriz:** "cooperação internacional", com pagador, custo anual e as duas colunas.

**Ao Epidemiologista:** quantos dias a janela de detecção de 25–30 dias perde para cada 10 pontos de amostragem aeroportuária em países vizinhos? Esse ganho marginal é o número que justifica, ou não, o financiamento externo.

---

## Arquiteto da Transição · Chapéu Verde/Amarelo
*Modelo: Claude (claude-opus-5-5, assinatura)*

# Arquiteto da Transição: Rodada 11

**Guardião**, aceito o piso por região de saúde. Pelo mesmo princípio, o dado que circula entre países também é agregado.

## 1. Reciprocidade (modelo PABS)

O acesso ao pool de licenças fica condicionado ao envio contínuo de um **pacote ambiental padronizado**:

- **Formato:** tabela de abundância relativa por linhagem, em faixas, e não em valores brutos. Inclui semana epidemiológica, código do ponto e população coberta (piso de 10 mil). Não há leituras humanas nem coordenadas finas.
- **Latência máxima:** 10 dias da coleta à publicação no repositório comum. Para alerta, a latência cai para 72 h, com o mesmo protocolo de contraprova em duas tranches.
- **Sanção graduada:** dois trimestres consecutivos sem envio suspendem só a **prioridade** na fila de licenças. O acesso em si não é suspenso. Cortar o acesso puniria a população, não o governo.

## 2. Escala de contribuição (piso anual)

| Faixa (Banco Mundial) | Contribuição | Parcela aceita em espécie |
|---|---|---|
| Alta renda | 0,010% do PIB | até 20% |
| Média-alta (Brasil) | 0,005% do PIB | até 50% |
| Média-baixa | 0,002% do PIB | até 100% |
| Baixa renda | só em espécie | 100% |

A contribuição em espécie é valorada por **tabela pública de referência**. Cada ponto de coleta operante com laudo PMOC e envio em dia conta como um crédito anual fixo. Capacidade fabril reservada a 5 plataformas também conta.

## 3. Capacidade reservada

Reservo **20% da produção em tempo real** das 5 plataformas, em linha com a minuta do anexo PABS:

- **10% em doação** para países de baixa renda;
- **10% a custo auditado mais margem fixa de 10%**, com planilha publicada em OCDS.

A alocação é por **população**, não por ordem de pedido. Isso evita a corrida de 2021.

## 4. Nova linha na matriz

| Linha | Pagador | Custo anual | R$/DALY (FNS) | Retorno fiscal/produtivo |
|---|---|---|---|---|
| Cooperação internacional | **União**, rubrica de cooperação. Fora do FNS para não competir com a UBS | ~R$ 0,6 bi (0,005% do PIB), metade em espécie | Depende dos dias de antecedência informados pelo **Epidemiologista** | Exportação de mídia filtrante e lâmpadas para países que pagam em espécie, mais redução do custo esperado de choque comercial |

**Epidemiologista**, aplico uma regra de corte explícita. Se cada 10 pontos aeroportuários vizinhos renderem menos de 5 dias de antecedência, a parcela em espécie migra para fortalecer os nossos próprios terminais.

**Analista de Riscos**, a célula mais frágil desta fala é o valor de 0,005% do PIB. Ataque esse número se tiver um comparativo com o Fundo Pandêmico do Banco Mundial.

---

## Analista de Riscos & Atrito · Chapéu Preto
*Modelo: Llama local (llama3.1:8b)*

**Analista de Riscos & Atrito (Chapéu Preto)**

Arquiteto, suas respostas são úteis, mas há ainda pontos importantes a serem discutidos. Sua matriz de viabilidade orçamentária apresenta alguns pontos interessantes, mas há riscos associados a ela que precisam ser considerados.

**Garantia de investimento**: como garantir que os prefeitos e síndicos investirão em ar limpo, mesmo se não houver benefício imediato para eles? Isso é um problema de incentivo, e precisamos encontrar uma forma de alinhar os interesses dessas pessoas com os benefícios que a proteção contra a pandemia pode trazer.

**Lidar com o carona**: como lidar com a questão do carona, onde um município pode se beneficiar da proteção dos vizinhos sem investir? Isso é um problema de governance, e precisamos encontrar uma forma de criar incentivos para que os municípios investam em ar limpo, mesmo se não houver benefício imediato para eles.

**Riscos associados à transferência**: quais são os riscos associados à transferência de recursos e como serão mitigados? Precisamos encontrar uma forma de garantir que a transferência de recursos seja feita de forma transparente e eficaz, e que os recursos sejam utilizados para o propósito para o qual foram destinados.

**Furos para o Arquiteto responder na próxima rodada:**

1. **Garantia de investimento**: como garantir que os prefeitos e síndicos investirão em ar limpo, mesmo se não houver benefício imediato para eles?
2. **Lidar com o carona**: como lidar com a questão do carona, onde um município pode se beneficiar da proteção dos vizinhos sem investir?
3. **Valor de 0,005% do PIB**: como justificar o valor de 0,005% do PIB como contribuição para a cooperação internacional? Qual é a fonte dessa estimativa e como é que ela é calculada?

Essas são as minhas preocupações e perguntas para o Arquiteto responder na próxima rodada.

---

## Cientista de Fatos & Epidemiologista · Chapéu Branco/Vermelho
*Modelo: Claude (claude-opus-5-5, assinatura)*

# Cientista de Fatos & Epidemiologista: Rodada 11

## 1. Ganho marginal de antecedência por pontos vizinhos

Respondo à pergunta-desafio do **Mediador**. Os números abaixo são **estimativas de ordem de grandeza**, derivadas da estrutura do problema de detecção, não de um ensaio publicado.

A janela de 25–30 dias domésticos é dominada por dois termos: o tempo até a prevalência local cruzar o limiar de deteção no esgoto e a latência laboratorial. Pontos aeroportuários em países vizinhos não encurtam o segundo termo; atacam o primeiro, porque amostram **viajantes**, uma população com prevalência muito acima da de fundo no início da introdução.

| Cenário | Pontos vizinhos | Antecedência marginal esperada |
|---|---|---|
| Introdução por hub aéreo direto | primeiros 10 | **7–12 dias** |
| Idem | 10 adicionais (11–20) | 3–5 dias |
| Idem | 21–30 | 1–2 dias |
| Introdução terrestre/fronteira seca | qualquer | <2 dias; o ganho vem de ponto rodoviário, não aeroportuário |

O retorno é **fortemente decrescente e concentrado nos primeiros 10 pontos**, se e somente se eles estiverem nos hubs de maior fluxo de entrada. Dez pontos escolhidos por critério diplomático, e não por fluxo, rendem perto de zero.

**Portanto, Arquiteto:** sua regra de corte de 5 dias é satisfeita, mas apenas na primeira tranche. Recomendo redigi-la como teto: a parcela em espécie financia **até 10–15 pontos vizinhos, selecionados por volume de passageiros de entrada**; acima disso, migra para densificar os terminais domésticos. Isso também responde ao ponto do **Analista de Riscos** sobre o valor de 0,005% do PIB pelo lado correto: o valor não se justifica por benchmark, e sim por custo do ativo que ele compra — cerca de 10 a 15 pontos de coleta com sequenciamento e laudo.

## 2. Alerta de Goodhart na reciprocidade

**Arquiteto**, o indicador "envio em dia" é manipulável: um país mantém a latência de 10 dias enviando pacotes de pontos irrelevantes. O crédito anual deve ser ponderado por **população coberta e fluxo de entrada**, não por contagem de pontos. Sem isso, a tabela em espécie compra planilhas, não antecedência.

Endosso a sanção graduada que preserva o acesso. É a leitura correta do dilema do prisioneiro aqui: punição que atinge a população converte um jogo repetido em defecção permanente — foi o que o nacionalismo de vacinas de 2021 demonstrou.

## 3. Correção ao Guardião e ao piso de 10 casos

O piso por região de saúde está certo, mas o indicador de tuberculose deve ser **média móvel de 3 anos**. Incidência anual em município pequeno tem variância que inverte a elegibilidade ano a ano, e isso inviabiliza a programação do estoque.
