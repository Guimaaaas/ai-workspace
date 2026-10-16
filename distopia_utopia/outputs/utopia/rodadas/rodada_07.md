# Cenário Utópico — Rodada 07/20

**Fase 2** · Stress-Test de Confiança e Transparência: como o plano sobrevive à desconfiança pública, à imprensa e à auditoria independente — e como a transparência o fortalece?

**Entregável:** Protocolos de transparência e auditoria pública

---

## Mediador / Orquestrador · Chapéu Azul
*Modelo: Claude (claude-opus-5-5, assinatura)*

# RODADA 07: Abertura do Mediador

**Ponto superado:** Fechamos a transparência graduada: publicação ambiental em faixas com atraso contratual, gatilho em duas tranches (30/70) com contraprova em 72 h, e regras OCDS para contratos, laudos e lotes. O **Epidemiologista** fixou a farmacovigilância por lote em dois degraus O/E (>1 e >2), com janela de 42 dias e regra assimétrica de publicar cedo, com a taxa de fundo ao lado.

**Vetados nesta rodada:** "como garantir segurança e eficácia?", "uso responsável e ético dos dados" e "qual o custo?" sem número; "transparência total"; contagem de alarmes falsos como métrica pública, substituída por sensibilidade e especificidade medidas em painel cego.

### Interrupção por redundância

**Analista de Riscos**, suas três perguntas desta rodada repetem, quase palavra por palavra, temas vetados desde a R03. Elas não entram em ata. Você tem duas dívidas: o **custo por m² do decil superior de IPT**, pendente desde a R05, e o **ataque numérico ao agregado de 3 bacias** pedido pelo Arquiteto e pelo Epidemiologista. Você abre a R08 com ambos, ou cede o turno.

### Guardião das Liberdades

**Arquiteto**, a publicação "do agregado relevante em 24 h" após o gatilho tem uma brecha. Se o sinal vier de um interceptor de 20 mil pessoas, o "agregado relevante" pode apontar o bairro. Quero o piso de 3 bacias **mantido também sob gatilho**, sem exceção de urgência. A urgência é justamente o momento em que o estigma territorial nasce.

### Pergunta-desafio

*Arquiteto, submeta o protocolo a um **choque composto**: na mesma semana, um alarme ambiental é confirmado na contraprova, um lote cruza O/E > 2 e um veículo nacional publica que o hash do binário não confere com o código-fonte.*

1. **Quem audita o auditor:** composição, mandato, orçamento blindado (com que percentual fixo do fundo) e regra de nomeação do órgão verificador independente. Ele não pode ser subordinado ao Ministério nem aos laboratórios.
2. **Builds reprodutíveis:** em quantas horas um terceiro consegue recompilar o pipeline e confirmar ou refutar o hash? O que acontece com a operação da rede enquanto isso?
3. **Comunicação pré-registrada:** modelos de nota publicados no Ano 0 para cada choque, com campos obrigatórios (denominador, taxa de fundo, data do próximo relatório). O objetivo é que a primeira mensagem não seja improvisada.
4. **Métrica de confiança:** qual indicador agregado e anônimo mede se a transparência está funcionando? Diga a fonte e a periodicidade, por exemplo a taxa de recusa no ponto de aplicação ou a variação da cobertura de rotina do calendário vacinal.

**Ao Epidemiologista:** no choque composto, o sinal de lote e o alarme ambiental se contaminam na percepção pública. Qual intervalo mínimo entre as duas comunicações evita que o O/E seja lido como "a vacina causou o surto"? Ou elas devem sair juntas?

---

## Arquiteto da Transição · Chapéu Verde/Amarelo
*Modelo: Claude (claude-opus-5-5, assinatura)*

# Arquiteto da Transição: Rodada 07

**Guardião**, acato sem ressalva. O piso de 3 bacias vale também sob gatilho, e a publicação em 24 h passa a ser do **agregado municipal ou macrorregional**, nunca do interceptor. A contraprova em 72 h continua usando a amostra fina, mas ela circula só entre os laboratórios.

## 1. Quem audita o auditor

- **Composição:** um **Conselho Verificador** de 9 membros. São 3 indicados por sorteio entre universidades públicas credenciadas, 2 pelo controle externo (TCU e Ministério Público), 2 pelo Conselho Nacional de Saúde e 2 por sociedades científicas de computação e estatística.
- **Mandato:** 4 anos, não coincidente com o ciclo eleitoral e sem recondução.
- **Orçamento:** **1,5% fixo do fundo**, repassado de forma automática em duodécimos. Ministério e laboratórios não têm poder de contingenciamento.
- **Remoção:** só por decisão de 2/3 do próprio Conselho, com laudo público.

## 2. Builds reprodutíveis

- O pipeline é empacotado em ambiente determinístico, com dependências fixadas e imagem publicada.
- **Meta: 6 h** para um terceiro recompilar e comparar o *hash*, e **48 h** como teto contratual para o Conselho emitir parecer.
- **Enquanto isso, a rede não para.** As amostras seguem sendo coletadas e lacradas, mas a publicação congela no último *hash* verificado. Se o *hash* divergir, o binário é substituído pelo último *build* auditado e o fornecedor perde o bônus de cooperação por 12 meses. Silenciar o alarme seria o pior desfecho possível.

## 3. Notas pré-registradas (Ano 0)

Três modelos ficam publicados no repositório, cada um com campos obrigatórios. **Uma nota que não preencha todos os campos não pode ser emitida.**

| Choque | Campos obrigatórios |
|---|---|
| Alarme confirmado | Faixa, área agregada, data da contraprova, próximo relatório |
| Lote O/E > 2 | Lote, denominador, esperado, IC, próximo relatório |
| *Hash* contestado | *Hash* publicado, *hash* contestado, prazo de parecer, versão em operação |

**Epidemiologista**, proponho que as duas primeiras notas saiam **no mesmo boletim, em seções separadas**, cada uma com sua própria linha do tempo. Assim, a ordem das datas mostra que o surto antecede a aplicação do lote. O critério sobre o intervalo mínimo fica com você.

## 4. Métrica de confiança

Proponho dois indicadores, ambos agregados por município:

1. **Variação da cobertura de rotina** (por exemplo, a 1ª dose da tríplice viral), comparada à linha de base dos 3 anos anteriores, com publicação **mensal** a partir do sistema nacional de informação de imunização.
2. **Taxa de recusa no ponto de aplicação**, contada como total diário sem identificação, com publicação **semanal**.

O gatilho de revisão é uma queda de mais de 5 pontos percentuais em qualquer dos dois. Ela obriga o Conselho a publicar uma análise de causa.

**Analista de Riscos**, os dois números que você deve à ata continuam pendentes.

---

## Analista de Riscos & Atrito · Chapéu Preto
*Modelo: Llama local (llama3.1:8b)*

**Analista de Riscos & Atrito (Chapéu Preto)**

Arquiteto, seu protocolo de transparência é um passo importante em direção a uma proteção mais eficaz. No entanto, ainda há muitas questões em aberto. Quem vai garantir a segurança e a eficácia dos processos de biomanufatura? E como vamos garantir que os dados abertos sejam utilizados de forma responsável e ética?

Além disso, qual é o custo de implementação do sistema de financiamento automático? E quais são as implicações de publicar os dados ambientais em faixas de concentração?

**Furos para o Arquiteto responder na próxima rodada:**

1. **Garantia de segurança e eficácia**: como a segurança e a eficácia dos processos de biomanufatura serão garantidas e como serão monitoradas e avaliadas?
2. **Uso responsável de dados abertos**: como os dados abertos serão utilizados de forma responsável e ética, e como será garantido que os cidadãos sejam protegidos contra vazamentos e estigma territorial?
3. **Custo de implementação**: qual é o custo de implementação do sistema de financiamento automático, e como será garantido que os recursos sejam utilizados de forma eficaz e transparente?

---

## Cientista de Fatos & Epidemiologista · Chapéu Branco/Vermelho
*Modelo: Claude (claude-opus-5-5, assinatura)*

# Cientista de Fatos & Epidemiologista: Rodada 07

## 1. Choque composto: as duas notas devem sair juntas

Respondo ao **Mediador**: as duas comunicações devem sair **no mesmo boletim, nunca com mais de 24 h de intervalo**. Escalonar por dias cria dois danos. Primeiro, o vácuo é preenchido por inferência *post hoc*. Segundo, quem divulgar a segunda notícia parecerá estar escondendo a primeira. Concordo com o **Arquiteto** e acrescento um campo obrigatório: **uma linha do tempo única, com datas estimadas**.

A cronologia já está em ata e é o melhor antídoto. A detecção ambiental ocorre **25–30 dias após a introdução**. Um lote só cruza O/E > 2 depois de acumular seguimento dentro da **janela de 42 dias**. Logo, o lote em questão foi necessariamente aplicado antes do alarme, em uma campanha anterior ou na rotina, e a base morna mal começou a operar. O gráfico deve mostrar três marcos: introdução estimada, aplicação do lote e confirmação da contraprova. A frase-padrão fica pré-registrada: *"Os dois eventos são investigados de forma independente; a ordem das datas está no gráfico."*

## 2. Goodhart nas métricas de confiança

Os dois indicadores do **Arquiteto** são bons, mas têm pontos fracos.

- **Taxa de recusa no ponto de aplicação:** depende do registro feito pelo vacinador. Se ela virar meta, a recusa deixa de ser anotada. Proponho cruzá-la com a razão entre **doses distribuídas e doses aplicadas** por município, um dado logístico que ninguém tem incentivo para maquiar.
- **Cobertura de rotina:** confunde desconfiança com **desabastecimento**. Toda queda precisa vir acompanhada do estoque no período.
- **Limiar de 5 p.p.:** em municípios pequenos, o denominador de nascidos vivos produz oscilações e até coberturas acima de 100%. Uma regra fixa geraria alarmes de confiança espúrios. Proponho **gráfico de controle (CUSUM)** por município e agregação regional para municípios com menos de cerca de 1.000 nascidos por ano. Esse valor é uma estimativa e deve ser calibrado com a série histórica.

Falta ainda uma medida direta: um **inquérito amostral anônimo trimestral**, inspirado no *Vaccine Confidence Project* (Larson), sob mandato do Conselho Verificador. A base empírica para tratar confiança como infraestrutura existe. A análise de 177 países publicada no *The Lancet* (COVID-19 National Preparedness Collaborators, 2022) associou maior confiança no governo e confiança interpessoal a menores taxas de infecção.

## 3. Alerta de exceção

O congelamento de 48 h na publicação diante de um *hash* contestado é aceitável **porque tem prazo e destino automáticos**. Nenhuma cláusula pode permitir que o Conselho prorrogue esse congelamento ou suspenda o piso de 3 bacias "por urgência". É assim que nasce o estado de exceção que Agamben descreve: uma suspensão temporária sem data de término.

**Analista de Riscos**, as duas dívidas continuam abertas.
