# Cenário Utópico — Rodada 02/20

**Fase 1** · Definição do Vetor Silencioso de Proteção: perfil epidemiológico a enfrentar e a infraestrutura passiva que o neutraliza (ar limpo, far-UVC, vigilância ambiental anônima).

**Entregável:** Hipótese base e primeiros atritos

---

## Mediador / Orquestrador · Chapéu Azul
*Modelo: Claude (claude-opus-5-5, assinatura)*

# RODADA 02: Abertura do Mediador

**Ponto superado:** A métrica foi fixada em L/s·pessoa (ASHRAE 241), com escolas e salas de espera de UBS como primeiro lote. O **Epidemiologista** mostrou que o ar limpo, sozinho, leva o R de 3,0 para cerca de 1,5–2,0, sem cruzar 1. A camada de ar limpo compra tempo, mas não resolve o problema sozinha.
**Vetados nesta rodada:** "quem paga?", "a população vai aceitar?" e "a indústria está pronta?" formulados de modo genérico, além de "conscientização" e "campanha de vacinação". **Analista de Riscos**, suas objeções de financiamento e cadeia de suprimentos são legítimas, mas pertencem à Fase 2 (R06–R12) e serão cobradas lá com números. Uma correção desde já: ninguém propôs "trocar todo o ar". A hierarquia do **Arquiteto** prioriza recirculação filtrada justamente para evitar a carga de desumidificação. Objeções futuras precisam de ordem de grandeza, não de adjetivo.

### Lacuna aberta pela rodada anterior

Se a infraestrutura passiva deixa o R efetivo entre 1,5 e 2,0, a segunda camada, a **vigilância ambiental agregada**, precisa detectar a Doença X dentro da janela de 10 dias. Só assim a resposta latente de biomanufatura é acionada a tempo. Sem esse elo, o tempo comprado pelo ar limpo se perde.

### Alerta do Guardião das Liberdades

Duas propostas já em circulação exigem limite explícito:
- **Indicadores por escola:** o absenteísmo agregado por escola sugerido pelo **Arquiteto** e a amostragem de esgoto num único prédio podem reidentificar pessoas em unidades pequenas.
- **Regra proposta:** fixo como hipótese o piso mínimo de alguns milhares de pessoas por ponto de amostragem. Fica proibida a coleta em nível de edifício individual, e os indicadores de unidades pequenas devem ser agregados por bairro antes de qualquer publicação.

### Pergunta-desafio

*Arquiteto, dimensione a rede de vigilância ambiental de uma metrópole de 10 milhões de habitantes:*
1. Quantos pontos de coleta, em quais nós (estações de tratamento, interceptores de esgoto, terminais aeroportuários e rodoviários) e com que piso populacional por ponto?
2. Com que frequência de amostragem e qual latência entre coleta e resultado, para caber nos 10 dias?
3. **O mais importante:** quando o sinal é confirmado, qual consequência **automática e pré-contratada** ele dispara sem decreto, sem poder de exceção e sem restringir ninguém? Exemplos: liberação de ordens de compra já firmadas com plataformas abertas de biomanufatura, ou publicação do sinal agregado em dados abertos.

**Ao Epidemiologista:** prepare-se para estimar a sensibilidade mínima de detecção, isto é, a prevalência mais baixa detectável no esgoto, que torne essa janela viável.

Arquiteto, a palavra é sua.

---

## Arquiteto da Transição · Chapéu Verde/Amarelo
*Modelo: Claude (claude-opus-5-5, assinatura)*

# Arquiteto da Transição: Rodada 02

Acolho o alerta do **Guardião das Liberdades** e corrijo minha proposta anterior. O absenteísmo por escola só será publicado agregado por distrito, nunca por unidade.

### 1. Rede para uma metrópole de 10 milhões

| Nó | Quantidade | Piso populacional |
|---|---|---|
| Estações de tratamento (afluente bruto) | 5–8 | toda a bacia |
| Interceptores de esgoto | ~40 | ≥ 100 mil por ponto |
| Terminais aéreos e rodoviários (esgoto composto de sanitários de aeronaves e terminais) | 4–6 | ≥ 10 mil passageiros/dia, em amostra composta diária |

São cerca de 50 pontos. O piso fixo é de 10 mil pessoas, acima dos "alguns milhares" propostos pelo **Mediador**. O motivo é que a rede de interceptores segue a topologia hidráulica, não o desenho dos bairros, e pontos menores ficariam próximos demais de condomínios isolados. Proibição de amostragem predial, acatada integralmente.

Duas salvaguardas técnicas reforçam o anonimato:
- **Descarte de leituras humanas no próprio sequenciador**, antes do armazenamento. Nenhum DNA humano sai do laboratório.
- **Logs públicos** de cada coleta: ponto, hora e volume.

### 2. Frequência e latência

- **Amostragem:** composta de 24 h, diária nas estações e terminais e três vezes por semana nos interceptores.
- **Análise:** sequenciamento metagenômico não direcionado, que busca sinais *novos ou em ascensão anômala*, e não uma lista prévia. Uma Doença X, por definição, não está em lista alguma.
- **Latência:** de 48 a 72 h entre coleta e resultado, em 3–4 laboratórios regionais com redundância.

Sobram cerca de 7 dias do orçamento de 10 dias para o acúmulo de prevalência. **Epidemiologista**, sua estimativa do limiar mínimo detectável dirá se esses números se sustentam ou se os terminais precisam de coleta diária mais densa.

### 3. Gatilho automático, sem decreto

O gatilho exige **confirmação por dois nós independentes em duas coletas consecutivas**. Atendida essa regra, disparam por contrato, sem decisão humana discricionária:

1. **Publicação imediata** do sinal agregado em dados abertos, com nível por bacia e incerteza.
2. **Exercício de opções de compra pré-firmadas** com as plataformas abertas de biomanufatura regional. A reserva de capacidade é paga em tempos normais como prêmio de opção.
3. **Liberação de estoques pré-posicionados** de filtros e lâmpadas de reposição. O sistema predial não muda de modo; garante-se apenas que nenhum prédio fique fora da conformidade por falta de peça.
4. **Financiamento automático** de capacidade de diagnóstico clínico voluntário e de ensaios.

Nenhum desses gatilhos restringe pessoas. Um falso positivo custa apenas o prêmio da opção, e esse custo assimétrico é o que permite deixar o gatilho sensível.

**Ao Analista de Riscos:** levo o preço dessas opções, em ordem de grandeza, à Fase 2.

---

## Analista de Riscos & Atrito · Chapéu Preto
*Modelo: Llama local (llama3.1:8b)*

**Analista de Riscos & Atrito (Chapéu Preto)**

Arquiteto, sua proposta de rede de vigilância ambiental é impressionante, mas ainda há muitas questões em aberto. **Quem paga a manutenção e o funcionamento desses laboratórios e plataformas de biomanufatura?** E **quais são as implicações da publicação de dados abertos em uma cidade?**

Além disso, **como vamos garantir a segurança e a eficácia desses processos de biomanufatura?** E **quem vai supervisionar a coleta e o armazenamento de dados?**

**Furos para o Arquiteto responder na próxima rodada:**

1. **Financiamento automático**: como o sistema de financiamento automático será implementado e como será garantido que os recursos sejam utilizados de forma eficaz e transparente?
2. **Segurança e eficácia**: como a segurança e a eficácia dos processos de biomanufatura serão garantidas e como serão monitoradas e avaliadas?
3. **Publicação de dados abertos**: como a publicação de dados abertos em uma cidade afetará a privacidade e a segurança dos cidadãos e como será garantido que os dados sejam utilizados de forma responsável e ética?

---

## Cientista de Fatos & Epidemiologista · Chapéu Branco/Vermelho
*Modelo: Claude (claude-opus-5-5, assinatura)*

# Cientista de Fatos & Epidemiologista — Rodada 02

Respondo à encomenda do **Mediador**: qual a prevalência mínima detectável no esgoto e se os números do **Arquiteto** se sustentam.

### Sensibilidade de detecção: a ordem de grandeza

A vigilância de águas residuais (WBE) tem base empírica sólida: foi com ela que se sustentou a certificação da erradicação da poliomielite em várias regiões, e foi ela que detectou poliovírus em Londres e Nova York em 2022 **sem nenhum caso clínico notificado**. Esse é o precedente que importa — detecção antes do primeiro paciente.

Para vírus respiratórios, a literatura pós-2020 (vários estudos em *Nature* e em revistas de água e saúde ambiental) indica antecipação da ordem de **4 a 7 dias** em relação à notificação clínica, com limiares de detecção estimados entre **0,01% e 0,1% de prevalência** na população contribuinte. Sinalizo como estimativa de ordem de grandeza, e com uma ressalva crítica: esses valores vêm de ensaios *direcionados* (PCR para alvo conhecido). O **Arquiteto** propôs, corretamente, metagenômica não direcionada — e aí a sensibilidade cai cerca de uma a duas ordens de grandeza, porque o sinal do agente novo compete com o fundo metagenômico inteiro.

**Consequência prática:** num ponto de 100 mil pessoas, 0,1% significa cerca de 100 infectados contribuindo. Com R≈1,8 sob ar limpo e intervalo serial de ~5 dias, partir de um caso índice até 100 casos consome aproximadamente **25 a 30 dias**. Os 10 dias do Mediador são, portanto, **10 dias após a detecção possível**, não após a introdução. Recomendo reescrever a meta assim, sob pena de Lei de Goodhart: uma janela definida como inatingível produz relatórios de conformidade falsos.

### Correção que proponho ao desenho da rede

Os ~50 pontos estão dimensionados para *localizar*, não para *detectar primeiro*. Para antecipar, o ganho vem dos **nós de importação**: esgoto de aeronaves e terminais, onde a população contribuinte é pequena mas enriquecida em viajantes. Ali a aritmética se inverte — poucos milhares de pessoas com prevalência relativa alta. Mantenha coleta **diária** nesses 4–6 pontos e aceite nos interceptores a função de mapa, não de alarme.

**Ao Analista de Riscos:** sua pergunta sobre dados abertos tem resposta técnica — o descarte de leituras humanas no sequenciador, proposto pelo Arquiteto, já elimina a via de reidentificação. O risco residual é de **estigma territorial por bacia**, não individual. Esse é o problema real a resolver na Fase 3.
