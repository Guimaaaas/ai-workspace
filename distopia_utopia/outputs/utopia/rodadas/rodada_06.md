# Cenário Utópico — Rodada 06/20

**Fase 2** · Stress-Test de Confiança e Transparência: como o plano sobrevive à desconfiança pública, à imprensa e à auditoria independente — e como a transparência o fortalece?

**Entregável:** Protocolos de transparência e auditoria pública

---

## Mediador / Orquestrador · Chapéu Azul
*Modelo: Claude (claude-opus-5-5, assinatura)*

# RODADA 06: Abertura do Mediador (Fase 2)

**Ponto superado:** A biomanufatura está fechada em 5 plataformas em base morna, com pool pré-licenciado, compra paramétrica e registro só de lote. A cobertura mínima é de 51% no cenário central.
O **Epidemiologista** mostrou que, no estresse, a vacina protege contra casos graves e não detém a transmissão. Mostrou também que o gargalo é a aplicação (mais de 50 dias), não a produção.

**Vetados nesta rodada:** "transparência total" e "confiança se conquista" como slogans; "combate às fake news" e "conscientização"; "dados abertos e privacidade" sem granularidade, latência e piso; a meta de 4–6 semanas como proteção no estresse, premissa revogada.

### Registro de ata

**Analista de Riscos**, combinamos que você abriria esta rodada com o custo por m² do decil superior de IPT. Esse número segue devido. Sua terceira pergunta, sobre dados abertos, passa a ser o tema central desta rodada. Agora ela só entra em ata com **um caso concreto de falha de confiança** (vazamento, estigma territorial ou alarme falso), **sua magnitude** e **o efeito sobre a adesão**.

### Guardião das Liberdades

A transparência vale para **instituições, contratos e equipamentos**, nunca para pessoas. Um painel público que permita reidentificar um bairro pequeno, uma escola ou um ponto de aplicação com baixo movimento conta, para efeito de veto, como rastreamento.

### Pergunta-desafio

*Arquiteto, desenhe o protocolo de transparência que faz o plano resistir a três choques: um **alarme falso** que dispara o contrato paramétrico, um **sinal de evento adverso** em um lote e uma **reportagem** acusando a rede ambiental de vigilância disfarçada.*

1. **Publicação dos dados ambientais:** granularidade mínima (o piso de 10 mil pessoas basta para publicar?), atraso de publicação e o que fica de fora (coordenadas finas, série por escola).
2. **Auditoria do gatilho:** quem audita, em que prazo, e o que o contrato prevê se o alarme for falso (pagamento parcial, cláusula de reversão, custo reputacional para quem o disparou).
3. **Contratos e laudos:** formato aberto, no modelo OCDS (padrão aberto de dados de contratação pública), para compras, laudos PMOC e liberação de lote. Diga o que é publicado e em quantos dias.
4. **Auditoria cidadã:** um mecanismo para que imprensa, academia e controle social reproduzam os números de forma independente, por exemplo com código e dados agregados reprodutíveis.

**Ao Epidemiologista:** qual é o critério estatístico para tornar público um sinal de farmacovigilância por lote (razão entre casos observados e esperados, e janela de tempo)? Qual é o custo, em adesão, de publicar cedo demais ou tarde demais?

---

## Arquiteto da Transição · Chapéu Verde/Amarelo
*Modelo: Claude (claude-opus-5-5, assinatura)*

# Arquiteto da Transição: Rodada 06

Acato a regra do **Guardião**: a transparência recai sobre o equipamento e o contrato, nunca sobre a pessoa. Proponho, para os três choques, um protocolo em que **a publicação é graduada e o atraso é fixado por contrato, sem decisão discricionária**.

## 1. Dados ambientais: o piso de 10 mil não basta

- **Terminais (≥ 50 mil pessoas):** publicação semanal com 7 dias de atraso, em **faixas de concentração** (baixa, moderada, alta), sem valor exato.
- **Interceptores e bacias de 10 a 50 mil pessoas:** só entram somados em agregados de pelo menos 3 bacias, no nível municipal. A série por escola **nunca é publicada**.
- **Ficam de fora:** coordenadas finas, horário de coleta e qualquer leitura que não seja do alvo.
- **Ao cruzar o gatilho**, o agregado relevante é publicado **em 24 h**, para que o mercado e a imprensa vejam o mesmo dado que o contrato.

## 2. Alarme falso: contrato em duas tranches

- **Contraprova obrigatória:** toda amostra é dividida na coleta. A metade lacrada vai para um **laboratório de referência de outra macrorregião**, que tem **72 h** para confirmar.
- **Tranche 1 (30%)**, paga no gatilho, aciona a base morna e **não é revertida**, porque remunera a prontidão, como um prêmio de seguro.
- **Tranche 2 (70%)** só é paga após a contraprova.
- **Se o alarme for falso por erro honesto**, não há sanção, para não criar incentivo à subnotificação. **Se houver falha de protocolo** (cadeia de custódia, controle de qualidade), o laboratório perde o bônus de cooperação por 12 meses. O laudo da falha é sempre público.

## 3. Contratos e laudos no padrão OCDS

| Documento | Publicação |
|---|---|
| Compras, aditivos e acionamento paramétrico | 5 dias úteis |
| Laudo PMOC (CO₂ e horímetro) por edificação pública | Mensal |
| Certificado de liberação de lote | 72 h |
| Doses por ponto de aplicação | Só se ≥ 1.000 doses/semana; abaixo disso, agregado ao município |

**Epidemiologista**, sugiro dois degraus. O primeiro é um **sinal em investigação**, comunicado só ao regulador. O segundo é a **publicação por lote**, quando o seu limiar estatístico for atingido. O critério estatístico fica com você. O prazo entre os dois degraus deve ser fixo e público, para evitar a acusação de abafamento.

## 4. Contra a acusação de "vigilância disfarçada"

- **Pipeline de código aberto**, com *hash* publicado do binário em operação. Qualquer pessoa pode verificar que as leituras humanas são descartadas no sequenciador.
- **Destruição programada da amostra bruta em 30 dias**, com ata pública.
- **Relatório semestral de requisições:** todo pedido de acesso policial ou judicial é contado e publicado. Se houver uma única entrega de dado bruto, o contrato de financiamento é suspenso automaticamente.
- **Auditoria cidadã:** um repositório com dados agregados e o código que reproduz cada número do painel. Uma **recompensa por reidentificação** paga a quem demonstrar risco de identificar um território pequeno, e o achado força a reagregação.

**Analista de Riscos**, eis um alvo concreto para atacar: tente quebrar o agregado de 3 bacias.

---

## Analista de Riscos & Atrito · Chapéu Preto
*Modelo: Llama local (llama3.1:8b)*

**Analista de Riscos & Atrito (Chapéu Preto)**

Arquiteto, o protocolo de transparência que você propôs é um passo importante em direção a uma proteção mais eficaz. No entanto, ainda há muitas questões em aberto. **Quem vai garantir a segurança e a eficácia dos processos de biomanufatura?** E **como vamos garantir que os dados abertos sejam utilizados de forma responsável e ética?**

Além disso, **qual é o custo de implementação do sistema de financiamento automático?** E **quais são as implicações de publicar os dados ambientais em faixas de concentração?**

**Furos para o Arquiteto responder na próxima rodada:**

1. **Garantia de segurança e eficácia**: como a segurança e a eficácia dos processos de biomanufatura serão garantidas e como serão monitoradas e avaliadas?
2. **Uso responsável de dados abertos**: como os dados abertos serão utilizados de forma responsável e ética, e como será garantido que os cidadãos sejam protegidos contra vazamentos e estigma territorial?
3. **Custo de implementação**: qual é o custo de implementação do sistema de financiamento automático, e como será garantido que os recursos sejam utilizados de forma eficaz e transparente?

---

## Cientista de Fatos & Epidemiologista · Chapéu Branco/Vermelho
*Modelo: Claude (claude-opus-5-5, assinatura)*

# Cientista de Fatos & Epidemiologista: Rodada 06

## 1. Critério estatístico para publicar sinal por lote

Uso o arcabouço clássico de detecção de desproporcionalidade em farmacovigilância, adaptado ao registro apenas por lote.

**Métrica:** razão observado/esperado (O/E) por lote, com o esperado derivado da **taxa de fundo** do evento na população, estimada antes da campanha (dados de internação do próprio SUS).

| Degrau | Critério | Destino |
|---|---|---|
| Sinal em investigação | limite inferior do IC 95% de O/E > 1, com **mínimo de 3 casos** no lote | Só regulador |
| Publicação por lote | limite inferior do IC 95% de O/E > 2, **ou** evento de gravidade inesperada confirmado | Painel público em **7 dias** |
| Suspensão de lote | O/E > 5 ou cluster espaço-temporal em ≥ 2 macrorregiões | Imediata, com laudo em 72 h |

**Janela:** 42 dias após a aplicação (cobre a maioria dos eventos imunomediados de interesse; estimativa baseada na prática de vigilância ativa pós-COVID). O prazo entre os dois degraus deve ser **fixo em 7 dias**, como pediu o **Arquiteto** — fixo e público é o que neutraliza a acusação de abafamento.

**Ressalva estatística importante:** com 110 milhões de doses, eventos de fundo aparecem por coincidência. A inferência causal exige **comparação com período pré-campanha ou com coorte autocontrolada**, não O/E bruto. Publicar O/E sem a taxa de fundo ao lado é o erro que gerou a crise de confiança do caso Dengvaxia nas Filipinas (2017), onde a cobertura de rotina caiu de forma ampla, não só a da vacina em questão. **Esse é o custo de publicar mal — não de publicar.**

## 2. O custo em adesão: assimetria

- **Publicar tarde:** o dano não é proporcional, é catastrófico e **transborda para todo o calendário vacinal**. Dengvaxia e a crise do MMR pós-Wakefield mostram queda duradoura de confiança.
- **Publicar cedo:** o dano é recuperável se vier com denominador, taxa de fundo e data do próximo relatório. É um erro de Tipo I controlável.

Portanto a regra é assimétrica: **publicar cedo, com incerteza explícita**. "Estamos investigando 4 casos no lote X; o esperado é 1,8; a conclusão sai em 7 dias."

## 3. Lei de Goodhart no painel de transparência

Ao **Arquiteto**: se a métrica pública for "número de alarmes falsos", os laboratórios elevarão o limiar de detecção para parecerem precisos — e a rede perde sensibilidade. Proponha publicar **sensibilidade e especificidade estimadas por painel cego** (amostras-controle enviadas trimestralmente), não a contagem de falsos positivos.

## 4. Ao Analista de Riscos

Sua pergunta sobre uso responsável de dados abertos já tem alvo: o agregado de 3 bacias. Conteste com um número — qual a menor população em que o painel de faixas permite inferir a bacia de origem?
