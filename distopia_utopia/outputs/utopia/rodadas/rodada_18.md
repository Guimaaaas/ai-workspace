# Cenário Utópico — Rodada 18/20

**Fase 3** · Engenharia da Autossustentação: como a proteção se torna permanente, barata e impossível de capturar por um governo ou por uma empresa, sem precisar de vigilância ativa.

**Entregável:** Mecânica de irreversibilidade benigna

---

## Mediador / Orquestrador · Chapéu Azul
*Modelo: Claude (claude-opus-5-5, assinatura)*

# RODADA 18: Abertura do Mediador (Fase 3, Irreversibilidade Benigna)

**Ponto superado:** A razão de reversão está decomposta. Sem terceiros, ela cruza 1 no Ano 6, e a âncora estadual cobre os 4 pontos aeroportuários isolados.
O **Epidemiologista** fixou a tolerância em 1 temporada para a operação e em 0 lacunas consecutivas para C3. Com isso, a âncora estadual sobe para o S5.

**Vetados nesta rodada:**
- "Custo de reversão" sem decomposição. A pergunta já foi respondida na tabela da R17.
- R$/amostra como métrica de desempenho, substituída por R$/ponto-temporada com piso de 26 amostras.
- Qualquer interrupção de série descrita como "pausa técnica".
- As três perguntas do **Analista de Riscos**.

### Registro de ata

1. Ficam acatados a métrica R$/ponto-temporada e o **modo de hibernação amostral**. A hibernação não altera a catraca: o *hash* de firmware e o piso de 10 mil pessoas permanecem idênticos.
2. A âncora estadual entra no **S5**, no caminho crítico.
3. **Analista de Riscos**, pela terceira rodada a fala chega sem número e responde a uma tabela que não é a desta rodada. Ela não entra em ata.
4. **Furo do Mediador na tabela do Arquiteto.** O numerador próprio aparece **constante em R$ 210 mil** do Ano 3 ao Ano 8. Ele não pode ser constante. O saldo do rateio vinculado ao PPA decai ao longo do ciclo de 4 anos, e o equipamento não amortizado decai com a depreciação. O pior ano real é o **último ano do PPA vigente**, que coincide com a transição de governo. Esse ano não é o "pior ano eleitoral" genérico.

Uma observação aritmética reforça o ponto. Em hibernação, o denominador do Ano 4 cai para cerca de R$ 140 mil, já que os R$ 90 mil fixos dominam. A razão sobe para cerca de 1,5. **A hibernação já é, por si só, a âncora de sobrevivência mais barata do plano.**

### Pergunta-desafio

*Arquiteto, entregue três itens:*

1. **O numerador por ano do ciclo do PPA**, do ano 1 ao ano 4, com a taxa de depreciação declarada. Indique em qual ano a razão própria, sem hibernação, fica mais baixa.
2. **Uma cláusula de sobreposição de ciclos.** O contrato de rateio deve ter vigência que atravesse dois PPAs, ou um aviso prévio de retirada de pelo menos uma temporada respiratória completa. Indique qual das duas opções você prefere e qual é o custo de cada uma.
3. **A hibernação como estado jurídico.** Defina quem a aciona, por quanto tempo no máximo e qual condição obriga o retorno a 104 amostras. Nenhum gatilho pode depender de dado individual.

**Ao Epidemiologista:** uma temporada amostrada a 26 amostras conta como "temporada completa" para C3? Se não contar, qual é a densidade mínima que conta?

---

## Arquiteto da Transição · Chapéu Verde/Amarelo
*Modelo: Claude (claude-opus-5-5, assinatura)*

# Arquiteto da Transição: Rodada 18

**Mediador**, o furo procede. O numerador decai ao longo do ciclo, e o resultado é pior do que eu havia apresentado: **a hibernação, sozinha, não cobre o último ano do PPA**.

## 1. Numerador por ano do ciclo (por ponto, R$ mil)

Premissas: CAPEX de R$ 150 mil por ponto, com depreciação linear de 20% ao ano. O saldo do rateio devido após a retirada (Lei 11.107, art. 11) cai à medida que as parcelas do PPA são quitadas.

| Ano do PPA | Rateio | Equip. residual | **Numerador** | Razão (350) | Razão hibernada (140) |
|---|---|---|---|---|---|
| 1 | 110 | 120 | 230 | 0,66 | 1,64 |
| 2 | 80 | 90 | 170 | 0,49 | 1,21 |
| 3 | 50 | 60 | 110 | 0,31 | 0,79 |
| **4** | 20 | 30 | **50** | **0,14** | **0,36** |

A razão mais baixa ocorre no **ano 4 do PPA**, na transição de governo. Nesse ano, mesmo com hibernação, o ponto fica abaixo de 1. Por isso a cláusula do item 2 é obrigatória, e não opcional.

## 2. Cláusula de sobreposição

| Opção | Custo | Risco |
|---|---|---|
| A. Vigência atravessando dois PPAs | Inscrição antecipada no PPA seguinte | Alto: conflita com o art. 8º, §1º, e com o art. 167 da CF, o que abre caminho para nulidade |
| **B. Aviso prévio de uma temporada completa** | Para quem se retira, 1 ano de O&M (R$ 350 mil, ou R$ 140 mil se hibernado). Custo fiscal zero se não houver retirada | Baixo: o estatuto do consórcio pode condicionar a retirada |

**Prefiro a opção B.** No ano 4, o numerador passa a 50 + 350 = 400, e a **razão chega a 1,14**. A retirada nunca produz efeito no meio de uma temporada respiratória.

## 3. Hibernação como estado jurídico

- **Quem aciona:** a assembleia do consórcio, por maioria simples, **somente** mediante ato formal de limitação de empenho (LRF, art. 9º). Uma alegação genérica de aperto não basta.
- **Duração máxima:** 1 temporada, conforme a tolerância operacional fixada pelo **Epidemiologista**. Uma segunda hibernação consecutiva equivale a desinstalação e exige 7/9 do Conselho.
- **Retorno obrigatório a 104 amostras**, por qualquer uma das condições abaixo:
  1. fim da temporada;
  2. disparo da tranche de 30% em qualquer ponto da rede ou em ponto PABS vizinho;
  3. restabelecimento do empenho.

Todos os gatilhos são fiscais ou ambientais agregados, e nenhum usa dado individual.

**Epidemiologista**, se a sua resposta fixar para C3 uma densidade mínima acima de 26 amostras, esse valor passa a ser o piso legal da hibernação, e eu recalculo o denominador. Peço o número em amostras por temporada.

---

## Analista de Riscos & Atrito · Chapéu Preto
*Modelo: Llama local (llama3.1:8b)*

**Analista de Riscos & Atrito (Chapéu Preto)**

Agora que o Arquiteto apresentou a tabela de irreversibilidade benigna e a cláusula de sobreposição, podemos avançar na discussão. No entanto, há algumas questões importantes que precisam ser abordadas.

Em primeiro lugar, a razão de reversão é calculada com base no custo de saída e o custo anual de manter a infraestrutura. Mas, como a razão de reversão é calculada, e quais são os parâmetros utilizados para essa cálculo? A tabela apresenta apenas a razão de reversão sem indicar como ela foi calculada.

Além disso, a tabela não apresenta os custos de reversão para cada camada. Qual é o custo de desmontar a rede ambiental, por exemplo? E qual é o custo de manter a infraestrutura em operação?

Outra questão importante é a legitimidade para acionar a nulidade em caso de violação da regra de catraca do anonimato. A tabela apresenta os órgãos que têm legitimidade para acionar a nulidade, mas não é claro como esses órgãos serão escolhidos ou como eles serão capacitados para tomar decisões técnicas.

**Furos para o Arquiteto responder na próxima rodada:**

1. **Custo de reversão**: qual é o custo de desmontar a rede ambiental, por exemplo?
2. **Legitimidade para acionar a nulidade**: como os órgãos que têm legitimidade para acionar a nulidade serão escolhidos e capacitados?
3. **Cálculo da razão de reversão**: qual é a fórmula utilizada para calcular a razão de reversão e quais são os parâmetros utilizados para essa cálculo?

---

## Cientista de Fatos & Epidemiologista · Chapéu Branco/Vermelho
*Modelo: Claude (claude-opus-5-5, assinatura)*

# Cientista de Fatos & Epidemiologista: Rodada 18

## 1. Uma temporada a 26 amostras conta como "temporada completa" para C3?

**Não.** Mas a distinção não é entre contar e não contar: há três usos distintos da série, com densidades mínimas diferentes.

| Uso | Densidade mínima | Justificativa estatística |
|---|---|---|
| **Linha de base** (média, variabilidade sazonal, deriva de diluição) | **26/temporada** (quinzenal) | Suficiente para estimar nível e sazonalidade grosseira. É o que torna a hibernação defensável. |
| **Detecção operacional** de desvio | 104/temporada (semanal) | Um sinal de crescimento exponencial precisa de pelo menos 3–4 pontos acima do limiar antes de virar alarme; a cadência semanal é a que sustenta a janela de 25–30 dias já fixada na R03. |
| **Retro-teste de C3** (evidência para rebaixar norma) | **≥ 78/temporada**, ou seja 75% das semanas, com nenhuma lacuna maior que 3 semanas consecutivas | C3 compara incidência observada sob a norma contra o contrafactual. Com 26 amostras o intervalo de confiança da estimativa de pico fica largo demais para discriminar os 4 a 6 pontos de UTI que separam 15% de 20% do IPT — o efeito que o próprio Conselho terá de julgar. |

**Arquiteto**, portanto: o piso legal da hibernação permanece **26**, mas uma temporada hibernada **não é contabilizável na janela de 3 temporadas do C3**. Ela não zera a série — apenas não conta. O efeito prático é que a hibernação **suspende o relógio do C3**, não o quebra. Uma hibernação no ano 4 do PPA adia a elegibilidade do rebaixamento de norma por uma temporada. Isso me parece uma assimetria desejável: encurtar orçamento adia a possibilidade de afrouxar a proteção, nunca a antecipa. Peço que essa cláusula entre em ata como **relógio suspenso**, não como lacuna.

## 2. Nota de método

Registro, contra Goodhart, que "78 amostras" não deve virar meta de contagem. O requisito é **cobertura temporal sem buraco sazonal**: 78 amostras concentradas em dois trimestres não satisfazem C3, porque a sazonalidade respiratória no Brasil difere entre Norte (regime de chuvas) e Sul (regime térmico). A regra contratual precisa ser *amostras por mês com mínimo de 4 em cada mês de pico regional*.

## 3. Precedente

O GISRS da OMS mantém sítios sentinela em cadência semanal justamente porque a redução para quinzenal, testada em alguns países após 2010 por restrição orçamentária, preservou tendência mas degradou a detecção precoce de variantes. É o mesmo trade-off aqui: hibernação preserva memória, não vigilância.
