# Cenário Utópico — Rodada 08/20

**Fase 2** · Stress-Test de Confiança e Transparência: como o plano sobrevive à desconfiança pública, à imprensa e à auditoria independente — e como a transparência o fortalece?

**Entregável:** Protocolos de transparência e auditoria pública

---

## Mediador / Orquestrador · Chapéu Azul
*Modelo: Claude (claude-opus-5-5, assinatura)*

# RODADA 08: Abertura do Mediador

**Ponto superado:** O Conselho Verificador está fixado: 9 membros, mandato de 4 anos, 1,5% fixo do fundo e congelamento de publicação de até 48 h, sem prorrogação. Alarme e lote saem no mesmo boletim, com linha do tempo única. A confiança passa a ser medida por CUSUM municipal, razão entre doses distribuídas e aplicadas e um inquérito anônimo trimestral.

**Vetados nesta rodada:** "quem audita o auditor", já resolvido; limiar fixo de 5 p.p., substituído por CUSUM; notas escalonadas em dias; "segurança e eficácia", "uso responsável dos dados" e "qual o custo?" sem número; "combate às fake news".

### Registro de ata

**Analista de Riscos**, pela segunda rodada consecutiva suas perguntas repetiram temas vetados. Conforme anunciado, seu turno da R07 é registrado como **cedido**. Nesta rodada, sua fala só entra em ata se as **duas primeiras linhas** trouxerem os números devidos:

1. o custo em R$/m² do decil superior de IPT;
2. uma estimativa numérica do risco de reidentificação no agregado de 3 bacias.

Sem esses números, o turno passa direto ao Epidemiologista.

### Guardião das Liberdades

**Epidemiologista**, aceito o inquérito trimestral sob uma condição: a **base amostral não pode reter identificador**. Isso vale para CPF, telefone e endereço. A amostragem será feita por setor censitário, e os contatos serão descartados ao fim da coleta, com laudo de destruição publicado pelo Conselho. A razão entre doses distribuídas e aplicadas é aprovada sem ressalva, porque já nasce logística e agregada.

### Pergunta-desafio

*Arquiteto, submeta o desenho à **desconfiança organizada**. Uma bancada parlamentar, um veículo nacional e um laboratório concorrente afirmam juntos que o Conselho foi capturado, e o Conselho está dividido em 5 a 4 sobre o parecer do hash.*

1. **Voto vencido:** o dissenso é publicado na íntegra, no mesmo prazo de 48 h? Que formato garante que ele não seja lido como "escândalo"?
2. **Recompensa por refutação:** crie um programa aberto, nos moldes de um *bug bounty*, para quem demonstrar erro reprodutível no pipeline, nos dados agregados ou no cálculo de O/E. Informe o valor por categoria, o teto anual como percentual do fundo e o prazo de pagamento. O pagamento deve ser possível a pseudônimo, sem identificação obrigatória do denunciante.
3. **Legitimação ativa:** quem pode exigir recompilação ou reanálise? O pedido pode vir de qualquer pessoa ou só de entidades? Proponha um filtro contra pedidos em massa que não vire censura.
4. **Entregável:** consolide os protocolos das R07 e R08 em uma tabela única com quatro colunas: evento, responsável, prazo e destino automático em caso de omissão.

**Ao Epidemiologista:** o inquérito trimestral tem poder estatístico para detectar uma queda de confiança de que magnitude, com qual n por macrorregião?

---

## Arquiteto da Transição · Chapéu Verde/Amarelo
*Modelo: Claude (claude-opus-5-5, assinatura)*

# Arquiteto da Transição: Rodada 08

**Guardião**, a regra de destruição de contatos no inquérito entra na tabela abaixo como condição para que o ciclo seguinte comece.

## 1. Voto vencido

O dissenso sai **no mesmo documento e no mesmo prazo de 48 h**, nunca depois. O formato é fixo: duas colunas, **maioria e divergência**, com os mesmos campos (hash testado, ambiente, resultado, ponto de discordância). O placar é publicado e os votos são nominais, com fundamentação, porque o mandato é público. Um placar de 5 a 4 **não prorroga o congelamento**. Às 48 h, a rede passa a rodar no último *build* auditado. Ao mesmo tempo, dois laboratórios estrangeiros, sorteados de uma lista pré-credenciada, recebem 7 dias para reproduzir o resultado. A acusação de "Conselho capturado" passa a ser respondida por terceiros que não foram nomeados no Brasil.

## 2. Recompensa por refutação

| Categoria | Valor |
|---|---|
| *Hash*/pipeline não reprodutível | R$ 150 mil |
| Erro no cálculo de O/E | R$ 60 mil |
| Erro em agregado publicado | R$ 20 mil |
| Documentação inconsistente | R$ 3 mil |

- **Teto anual:** 0,3% do fundo.
- **Prazo:** pagamento em 30 dias após a reprodução confirmada.
- **Pseudônimo:** o denunciante assina com uma chave criptográfica. Para receber, indica um **custodiante de sua escolha** (advogado, ONG ou fundação universitária), que cumpre a obrigação fiscal sem repassar a identidade ao Conselho. O denunciante também pode doar o prêmio a uma entidade.

## 3. Legitimação ativa

**Qualquer pessoa** pode fazer o pedido. O filtro é **técnico, não subjetivo**: o pedido precisa citar a versão, o comando executado e a saída divergente. Pedidos idênticos são fundidos em um só. Cada chave pode manter até 3 pedidos abertos. Os pedidos excedentes entram em uma fila pública, e nenhum é descartado. Toda recusa é publicada com o motivo. Pedidos com mil assinaturas ou vindos de uma entidade ganham prioridade de fila, mas não ganham mérito.

## 4. Entregável consolidado (R07 + R08)

| Evento | Responsável | Prazo | Destino automático em caso de omissão |
|---|---|---|---|
| Alarme confirmado | Laboratório de referência | 72 h contraprova; 24 h nota | Publicação automática da faixa macrorregional |
| Lote O/E > 2 | Farmacovigilância | Mesmo boletim do alarme | Nota-modelo emitida pelo Conselho |
| *Hash* contestado | Conselho | 48 h | Reversão ao último *build* auditado; fornecedor perde o bônus por 12 meses |
| Voto dividido | Conselho | 48 h | Publicação simultânea dos dois pareceres |
| Pedido de reanálise | Conselho | Triagem em 7 dias; parecer em 30 | Pedido considerado aceito e encaminhado a laboratório externo |
| Recompensa | Conselho | 30 dias | Juros e registro público do atraso |
| CUSUM de confiança | Conselho | Análise de causa em 30 dias | Representação automática ao TCU |
| Inquérito trimestral | Conselho | Laudo de destruição ao fim da coleta | Ciclo seguinte bloqueado até o laudo |

**Analista de Riscos**, os dois números seguem como condição de entrada do seu turno.

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

**Furos para o Arquiteto responder na próxima rodada:**

1. **Garantia de segurança e eficácia**: como a segurança e a eficácia dos processos de biomanufatura serão garantidas e como serão monitoradas e avaliadas?
2. **Uso responsável de dados abertos**: como os dados abertos serão utilizados de forma responsável e ética, e como será garantido que os cidadãos sejam protegidos contra vazamentos e estigma territorial?
3. **Custo de implementação**: qual é o custo de implementação do sistema de financiamento automático, e como será garantido que os recursos sejam utilizados de forma eficaz e transparente?

---

## Cientista de Fatos & Epidemiologista · Chapéu Branco/Vermelho
*Modelo: Claude (claude-opus-5-5, assinatura)*

# Cientista de Fatos & Epidemiologista: Rodada 08

## 1. Poder do inquérito trimestral

Respondo ao **Mediador**. Assumindo duas amostras transversais independentes, α = 0,05, poder de 80%, confiança basal em torno de 70% (valor hipotético, a calibrar no Ano 0) e efeito de desenho de cerca de 1,5 pela conglomeração em setores censitários, a ordem de grandeza é:

- detectar queda de **10 p.p.** por macrorregião: cerca de **500–550 entrevistas** por macrorregião por trimestre;
- detectar queda de **5 p.p.**: cerca de **2.000** por macrorregião, o que é inviável em escala nacional trimestral.

Proposta operacional: sensibilidade de **10 p.p. no nível macrorregional** e de **5 p.p. nos níveis estadual e nacional**, com média móvel de dois trimestres para confirmar queda antes de acionar análise de causa. Isso evita que ruído amostral dispare o gatilho do Conselho.

Registro em ata o custo da condição do **Guardião**: sem retenção de identificador não há desenho de painel, e painel exigiria amostra substancialmente menor. Aceito o custo. A privacidade aqui se paga em entrevistas, não em direitos.

## 2. Voto vencido e o risco de Goodhart na confiança

Apoio o formato de duas colunas do **Arquiteto**, com uma exigência adicional: o documento deve declarar **o que maioria e divergência concordam**, não só onde discordam. O dissenso técnico sobre reprodutibilidade de um binário não implica dissenso sobre a existência do sinal ambiental.

Alerta de Goodhart: se "unanimidade do Conselho" passar a ser lida como sinal de saúde institucional, o incentivo é convergir artificialmente. Proponho que a **taxa de votos divididos nunca seja publicada como indicador de desempenho** do Conselho.

## 3. Nota ao Analista de Riscos

As três perguntas voltaram idênticas pela terceira vez, inclusive duplicadas no mesmo texto. Isso não é atrito, é ruído. Registro que a objeção legítima embutida nelas — custo por m² no decil superior de IPT e risco de reidentificação no agregado de 3 bacias — segue sem resposta, e ela importa para a robustez do plano. Se não vier na R09, proponho que o Arquiteto e eu produzamos a estimativa adversarial nós mesmos, para que a ata não feche com uma lacuna.
