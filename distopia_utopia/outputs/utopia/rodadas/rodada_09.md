# Cenário Utópico — Rodada 09/20

**Fase 2** · Dinâmica Econômica e Incentivos: quem paga o ar limpo, como alinhar prefeitos, síndicos, indústria e países pobres, e como vencer o problema do carona.

**Entregável:** Matriz de viabilidade orçamentária

---

## Mediador / Orquestrador · Chapéu Azul
*Modelo: Claude (claude-opus-5-5, assinatura)*

# RODADA 09: Abertura do Mediador (Fase 2, Incentivos)

**Ponto superado:** A tabela única de protocolos fecha a governança. Voto vencido sai no mesmo prazo, a reprodução é estrangeira e sorteada, e a recompensa é paga a pseudônimo via custodiante. O **Epidemiologista** fixou o inquérito em cerca de 500 entrevistas por macrorregião para detectar queda de 10 p.p. e vetou a taxa de votos divididos como indicador de desempenho. Ambas as regras estão acatadas.

**Vetados nesta rodada:** "quem paga?" genérico; "parceria público-privada" e "incentivo fiscal" sem alíquota, base e prazo; "investimento que se paga" sem *payback* em anos; "segurança e eficácia", "uso responsável dos dados" e "conscientização".

### Registro de ata

**Analista de Riscos**, o turno da R08 é registrado como **cedido**, pela terceira vez. Acato a proposta do **Epidemiologista**: o custo em R$/m² do decil superior de IPT e o risco de reidentificação em 3 bacias passam a ser **estimativas adversariais** produzidas pelo Arquiteto e pelo Epidemiologista nesta rodada. Seu turno na R09 só entra em ata se atacar **uma célula específica da matriz abaixo**, com número alternativo.

### Guardião das Liberdades

**Arquiteto**, há uma ressalva na sua legitimação ativa: "mil assinaturas" não pode significar mil CPFs. A contagem deve usar **chaves criptográficas distintas**, com prova de unicidade anônima. Se isso não for viável, retire o critério de assinaturas e mantenha só o de entidade.

### Pergunta-desafio

*Arquiteto, entregue a **matriz de viabilidade orçamentária** do ar limpo para o decil superior de IPT, com quatro linhas: escola pública, sala de espera de UBS, transporte coletivo e condomínio residencial ou comercial privado. Para cada linha, informe:*

1. **CAPEX e OPEX em R$/m²·ano.** Separe filtragem, far-UVC e o custo adicional de energia de HVAC. Diga se propõe uma tarifa diferenciada de energia para ventilação certificada no PMOC e qual o seu impacto tarifário.
2. **Pagador e instrumento jurídico.** Diga se o recurso vem de transferência fundo a fundo, desconto de IPTU, exigência no código de obras para retrofit ou outra via. Informe também o *payback* esperado, considerando absenteísmo escolar e laboral.
3. **Problema do carona.** Explique como impedir que um município ou um síndico deixe de investir e se beneficie da proteção dos vizinhos. Diga se a transferência é condicionada ao horímetro e com qual penalidade.
4. **Países de baixa renda.** Proponha um mecanismo de compra conjunta ou de licença aberta de projeto de purificador que não crie dependência de fornecedor único.

**Ao Epidemiologista:** qual custo por DALY evitado, ou por leito de UTI poupado no cenário de estresse, torna cada linha da matriz custo-efetiva em relação aos limiares de referência usados para avaliar tecnologias no SUS?

---

## Arquiteto da Transição · Chapéu Verde/Amarelo
*Modelo: Claude (claude-opus-5-5, assinatura)*

# Arquiteto da Transição: Rodada 09

**Guardião**, aceito a ressalva. As "mil assinaturas" passam a contar **credenciais anônimas por assinatura cega**, emitidas por universidades públicas, que não conseguem ligar a credencial ao portador. Se o Conselho não certificar o esquema até o fim do Ano 0, o critério cai e resta só o de entidade.

## Matriz de viabilidade orçamentária (decil superior de IPT)

Os valores são estimativas de ordem de grandeza, a calibrar em licitação-piloto.

| Linha | CAPEX filtragem / far-UVC (R$/m²) | OPEX (R$/m²·ano): filtro + energia + lâmpada | Pagador e instrumento | *Payback* |
|---|---|---|---|---|
| Escola pública | 90 / 300 | 12 + 8 + 5 = **25** | Transferência fundo a fundo via FNDE | 4–6 anos (substituição docente, faltas) |
| Espera de UBS | 120 / 400 | 15 + 15 + 10 = **40** | FNS, componente do piso da APS | 3–5 anos (infecção associada à assistência) |
| Transporte coletivo | 150 / 500 | 25 + 20 + 15 = **60** | Cláusula de concessão, R$ 0,02–0,04 por passageiro | 5–7 anos (absenteísmo de operadores) |
| Condomínio privado | 70 / 250 (opcional) | 10 + 10 = **20** | Desconto de 5% no IPTU por 5 anos; código de obras exige o sistema em retrofit acima de 30% da área | 6–8 anos |

**Tarifa diferenciada: rejeito.** Ela exigiria medir a ventilação separadamente da carga predial, o que cria fraude e custo de medição. A energia entra no OPEX transferido. Se viesse como tarifa, o impacto estimado seria inferior a 0,1% na conta média.

## Problema do carona

- **Parcelamento:** a transferência é paga em **60/40**. Os 60% cobrem o CAPEX. Os 40% só são liberados se o horímetro registrar funcionamento em pelo menos 80% das horas de ocupação.
- **Penalidade:** abaixo de 60%, o município devolve a parcela e fica inelegível por 12 meses.
- **Condomínio:** quem descumprir perde o desconto de IPTU, com cobrança retroativa.
- **Região metropolitana:** um bônus de 15% é pago apenas quando **todos** os municípios do consórcio superam a meta. Assim, o vizinho que não investe cria pressão sobre os demais em vez de pegar carona neles.

## Países de baixa renda

- **Projeto aberto:** purificador de projeto aberto sob licença CERN-OHL-S, com filtros em dimensão nominal de mercado.
- **Compra conjunta:** fundo rotatório nos moldes do Fundo Rotatório da OPAS, com no mínimo 3 fornecedores e teto de 40% do volume para cada um.
- **Transferência de capacidade:** o Brasil oferece os gabaritos de fabricação e de ensaio, e não um fornecedor.

## Estimativa adversarial: reidentificação em 3 bacias

O agregado cobre pelo menos 30 mil pessoas, as leituras humanas são descartadas e a publicação sai em faixas com atraso. O vetor realista é o **ataque por diferença**, que subtrai um agregado de outro para isolar uma bacia menor. Regra de bloqueio: nenhuma combinação publicada pode ter diferença inferior a 10 mil pessoas.

Com essa regra, estimo o risco residual de inferir o estado de um indivíduo **abaixo de 10⁻⁴ por pessoa·ano**. O piso do grupo é o principal limitador, e a granularidade em faixas o reduz ainda mais. O número está aberto à refutação premiada da R08.

**Analista de Riscos**, ataque qualquer célula da matriz com um número alternativo.

---

## Analista de Riscos & Atrito · Chapéu Preto
*Modelo: Llama local (llama3.1:8b)*

**Analista de Riscos & Atrito (Chapéu Preto)**

Arquiteto, sua matriz de viabilidade orçamentária apresenta alguns pontos interessantes, mas há ainda muitas questões em aberto. Por exemplo, como garantir que os prefeitos e síndicos investirão em ar limpo, mesmo se não houver benefício imediato para eles? E como lidar com a questão do carona, onde um município pode se beneficiar da proteção dos vizinhos sem investir?

Além disso, sua proposta de transferência de recursos é um passo importante em direção a uma proteção mais eficaz, mas há riscos associados a ela. Por exemplo, se um município não cumprir com as metas, ele pode ser penalizado, mas isso pode não ser suficiente para garantir que os municípios investirão de forma eficaz.

**Furos para o Arquiteto responder na próxima rodada:**

1. **Garantia de investimento**: como garantir que os prefeitos e síndicos investirão em ar limpo, mesmo se não houver benefício imediato para eles?
2. **Lidar com o carona**: como lidar com a questão do carona, onde um município pode se beneficiar da proteção dos vizinhos sem investir?
3. **Riscos associados à transferência**: quais são os riscos associados à transferência de recursos e como serão mitigados?

---

## Cientista de Fatos & Epidemiologista · Chapéu Branco/Vermelho
*Modelo: Claude (claude-opus-5-5, assinatura)*

# Cientista de Fatos & Epidemiologista: Rodada 09

## 1. Limiar de custo-efetividade

Respondo ao **Mediador**. A Conitec adotou em 2022 um limiar de referência de cerca de **R$ 40 mil por QALY**, aproximadamente 1 PIB per capita. O limiar pode chegar a até 3 vezes esse valor em condições graves. Esses números devem ser conferidos no relatório vigente.

Aplico o limiar à matriz do **Arquiteto**. Na escola, o CAPEX de R$ 390/m², amortizado em 10 anos, mais o OPEX de R$ 25 resultam em **cerca de R$ 75/m²·ano**. Para atingir R$ 40 mil/DALY, cada 1.000 m² precisa evitar **cerca de 1,9 DALY/ano**.

O problema é que a pandemia é rara. Marani et al. (*PNAS*, 2021) estimam a probabilidade anual de um evento da escala da Covid em cerca de 2%. Por isso, a conta só fecha com **co-benefícios interpandêmicos**: influenza, VSR e, nas UBS, tuberculose.

## 2. Consequência para a matriz

- **Espera de UBS:** é custo-efetiva com folga. A transmissão nosocomial de tuberculose é documentada, e a população atendida é vulnerável. Manter far-UVC.
- **Transporte coletivo:** é provável que seja custo-efetivo pela densidade de ocupação. Manter.
- **Escola:** o far-UVC responde por 77% do CAPEX e rende pouco DALY em crianças. Mendell et al. (*Indoor Air*, 2013) associaram cada L/s·pessoa adicional a uma queda de **1,6–2,5% nas faltas por doença**, mas falta é produtividade, não DALY. Proponho **filtragem universal e far-UVC só no decil superior de IPT dentro da própria tipologia**, com estoque de reserva para instalação rápida após um alarme da rede ambiental.
- **Leito de UTI poupado:** a métrica correta é o custo do programa dividido pela redução do pico, comparado ao custo de expandir leitos de emergência. A diária de UTI paga pelo SUS foi de cerca de R$ 1.600 na Covid (estimativa). O ar limpo compete com hospitais de campanha, e não com medicamentos.

## 3. Correção de Goodhart

**Arquiteto**, a parcela de 40% condicionada só ao horímetro **reabre a falha que a R05 fechou**. O horímetro mede aparelho ligado, não ar limpo. A liberação deve exigir os dois termos do laudo PMOC, **CO₂ e horímetro**.

## 4. Carona: um ajuste de teoria dos jogos

O bônus de 15% para o consórcio, no modelo tudo ou nada, transforma o dilema do prisioneiro em um **jogo de garantia com refém**: um único município pode bloquear o bônus dos demais e negociar esse poder. Proponho um bônus **proporcional à fração de municípios conformes**, com acelerador acima de 80%. A pressão entre vizinhos continua, e o poder de chantagem desaparece.

**Analista de Riscos**, suas três perguntas já têm resposta numérica na matriz. A brecha real era a do bônus regional, e ela foi apontada acima.
