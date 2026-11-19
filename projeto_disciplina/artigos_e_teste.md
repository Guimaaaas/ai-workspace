# artigos e teste · Chão Público

> levantamento de 18/11/2026. **abra cada link antes de usar**: nenhum texto completo foi lido. a coluna
> *conferido* diz até onde cada artigo foi checado. regras de veículo: [veiculos.md](https://lucassf.pages.dev/ai4good/artefatos/cmp/veiculos.md)
> (só artigo completo conta; dos 3 escolhidos, pelo menos 2 em veículo de excelência e no máximo 1 do arXiv).

## 1 · artigos

**o núcleo do Chão Público**, usado como filtro: (1) dado público ou oficial espalhado e difícil de usar →
(2) IA com ferramentas ou vários agentes que juntam e conferem esse dado → (3) uma saída verificável e
acionável, com fonte → (4) para quem está na linha de frente (movimento, trabalhador de base, cidadão, órgão
público). o tema não precisa ser imóvel: vale saúde, alimentação, benefícios, compras públicas.

ficha: **C**enário · **U**suário · **P**roblema · **T**ecnologia, cada um **=** igual, **≈** parecido ou **≠** diferente.

### 1.1 · em veículo de excelência

| artigo | veículo | tema | onde converge | C U P T | conferido |
|:--|:--|:--|:--|:-:|:--|
| **[RequestAtlas: Supporting the Slow and Iterative Process of Requesting Public Records](https://doi.org/10.1145/3711056)** (Warren, Pickoff-White, Parameswaran, Salehi, 2025) | PACM HCI (CSCW) · A1 | pedidos de informação | ferramenta para acompanhar pedidos de registros públicos, conferir se a resposta veio completa e negociar com o órgão. é o nosso fluxo de LAI e de anexar respostas. as primeiras tentativas com IA não funcionaram e a expertise humana continuou essencial. | ≈ ≈ ≈ ≈ | Crossref |
| **[ASHABot: An LLM-Powered Chatbot to Support the Informational Needs of Community Health Workers](https://doi.org/10.1145/3706598.3713680)** (Ramjee, Chhokar, Sachdeva, Meena, Abdullah, Vashistha, Nagar, Jain, 2025) | CHI · A1 | saúde | LLM no WhatsApp responde a agentes comunitárias de saúde (Índia) só com diretrizes oficiais; quando não sabe, encaminha à enfermeira supervisora, como o nosso "não encontrado → pedido de LAI". trata o LLM como "recurso falível e complementar". Sul Global, implantação real (20 agentes, 2 meses). | ≠ ≈ ≈ ≈ | Crossref |
| [AI Trust Reshaping Administrative Burdens: Understanding Trust-Burden Dynamics in LLM-Assisted Benefits Systems](https://doi.org/10.1145/3715275.3732077) (Jo, Zhang, Cai, Goyal, 2025) | FAccT | alimentação (SNAP) | entrevistas com quem pede o benefício sobre ajuda de LLM para lidar com o Estado. dá nome ao nosso problema: **carga administrativa** (*administrative burden*), o custo de lidar com a burocracia. discute o risco de confiar demais na IA. | ≠ ≈ ≈ ≈ | listagem do OpenAlex |
| [FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation](https://aclanthology.org/2023.emnlp-main.741) (Min et al., 2023) | EMNLP, trilha principal | avaliação de LLM | divide o texto em afirmações atômicas e mede quantas a fonte sustenta (ChatGPT: 58% em biografias). base do revisor, da validação em código e do teste da seção 2. | ≠ ≠ ≈ = | ACL Anthology |
| [Enabling Large Language Models to Generate Text with Citations (ALCE)](https://doi.org/10.18653/v1/2023.emnlp-main.398) (Gao, Yen, Yu, Chen, 2023) | EMNLP, trilha principal | avaliação de LLM | mede se as citações de um LLM sustentam o que ele afirma; o melhor modelo ficou sem suporte completo em cerca de metade das respostas do ELI5. argumento do "todo número com [E#]". | ≠ ≠ ≈ = | Crossref |
| [Improving Factuality and Reasoning in Language Models through Multiagent Debate](https://proceedings.mlr.press/v235/du24e.html) (Du, Li, Torralba, Tenenbaum, Mordatch, 2024) | ICML (PMLR 235) | avaliação de LLM | vários agentes que se contestam erram menos fatos que um agente só. sustenta a divisão em agentes; o custo extra também é o nosso. | ≠ ≠ ≈ = | PMLR |
| [Privacy versus Transparency: Navigating Public Records Requests and Adversarial Dynamics in a Distributed Multi-Stakeholder Collaboration](https://doi.org/10.1145/3711050) (Moran, Venkatagiri, Spiro, Starbird, 2025) | PACM HCI (CSCW) · A1 | pedidos de informação | o outro lado dos pedidos de registros públicos: transparência contra privacidade. justifica a regra de não nomear pessoa física. | ≠ ≠ ≈ ≠ | Crossref |
| [Chain-of-Verification Reduces Hallucination in Large Language Models](https://aclanthology.org/2024.findings-acl.212) (Dhuliawala et al., 2024) | **Findings** of ACL · perguntar ao professor se Findings conta | avaliação de LLM | o modelo planeja perguntas de verificação e responde sem ver o rascunho, o mesmo princípio do revisor separado do redator. | ≠ ≠ ≈ = | ACL Anthology |
| [NLP-based Page Classification for Efficient LLM Extraction from Brazilian Public Tender Documents](https://aclanthology.org/2026.propor-1.61/) (2026) | PROPOR · conferir se é artigo completo | compras públicas | LLM extrai dados estruturados de editais brasileiros. único com dado público brasileiro e LLM, mas só extrai: não verifica nem gera documento para cobrar. | ≈ ≠ ≈ ≈ | título na ACL Anthology; autores não |

### 1.2 · fora da lista (arXiv ou fora da computação)

| artigo | veículo | tema | onde converge | C U P T | conferido |
|:--|:--|:--|:--|:-:|:--|
| **[EpiNarrate: Agentic Generation of Grounded Narratives from Epidemiological Scenario Projections](https://arxiv.org/abs/2607.15544)** (2026) | arXiv | saúde pública | agentes geram relatórios de saúde pública **separando o cálculo dos números da escrita do texto**, como o nosso dossiê e redator. mostra que pedir direto a um LLM de ponta para resumir os dados gera inconsistências frequentes: é o "por que não só jogar no Claude", com números. | ≠ ≈ ≈ = | só busca |
| [Food4All: A Multi-Agent Framework for Real-time Free Food Discovery with Integrated Nutritional Metadata](https://arxiv.org/abs/2510.18289) (Yuan et al., 2025) | arXiv | alimentação | dois agentes com ferramentas (planejador e executor) cruzam bases oficiais e redes sociais para achar comida gratuita. tem 312 casos anotados para avaliação, modelo para o nosso teste. a versão mais nova mudou de título: conferir qual vale. | ≠ ≈ ≈ = | só busca |
| [Information Extraction from Brazilian News Articles on Public Procurement Fraud](https://sol.sbc.org.br/index.php/sbbd/article/view/43989) | SBBD · não está na lista | compras públicas | compara regra fixa, RAG e LLM puro para extrair dados de notícias sobre fraude em licitação. brasileiro e comparativo, como o nosso teste. | ≈ ≠ ≈ ≈ | só busca |
| [Hallucination-Free? Assessing the Reliability of Leading AI Legal Research Tools](https://doi.org/10.1111/jels.12413) (Magesh, Surani, Dahl, Suzgun, Manning, Ho, 2025) | Journal of Empirical Legal Studies · fora da computação | jurídico | avaliação pré-registrada de Lexis+ AI e Westlaw AI: mesmo com RAG em base jurídica, erram ou citam fonte que não sustenta a afirmação em 17% a 33% das respostas. motivação no § 0. | ≠ ≈ ≈ ≈ | Crossref (DOI) |
| [A aplicação do Parcelamento, Edificação ou Utilização Compulsórios (PEUC)](https://www.scielo.br/j/urbe/a/53jR6hSRpxT378PTHk7pGbx/?lang=pt) | Urbe (SciELO) · fora da computação | política urbana | o levantamento citado (Denaldi et al., 2015) diz que, até jan/2014, só 8 dos 288 municípios com mais de 100 mil habitantes tinham aplicado o PEUC. evidência de que a seção fiscal do laudo ataca um problema real. **número tirado de resumo de busca: conferir no texto.** | = ≠ = ≠ | só busca; autores não |

### 1.3 · sugestão para os 3 artigos do § 4 do cmp.md

- **RequestAtlas** (CSCW, A1): o fluxo de pedido de informação.
- **ASHABot** (CHI, A1): IA ancorada em fonte oficial, com especialista humano na linha de frente, no Sul Global.
- **EpiNarrate** (arXiv, a única vaga permitida): a mesma arquitetura e a prova de que um LLM sozinho erra.

saem dos 3: *Cidadão.AI* (concurso de TCC) e *From Data Activism* (que vai para o § 7, "tentei derrubar", como a
melhor crítica). o artigo da FAccT entra no § 0 ou § 1, como fundamento da carga administrativa. FActScore,
ALCE e Multiagent Debate entram como base técnica, ao lado do ReAct: têm tecnologia igual e problema
diferente, então não entram nos 3.

## 2 · estratégia de teste

**pergunta:** o Chão Público entrega um laudo mais confiável que um movimento conseguiria sozinho com um LLM
genérico? e, se sim, o ganho vem do prompt, das ferramentas ou do revisor?

### 2.1 · o método

adaptamos o FActScore (Min et al., EMNLP 2023) para texto com citação, como no ALCE (Gao et al., EMNLP 2023).
o [código original](https://github.com/shmsw25/FActScore) (licença MIT) não serve direto: só usa a Wikipédia em
inglês (`enwiki-20230401`), supõe um texto sobre uma entidade só (biografia) e usa modelos aposentados
(InstructGPT). aproveitamos o método e o protocolo:

1. **quebrar** o laudo em afirmações atômicas verificáveis ("o IPTU de 2023 foi R$ X", "o dono é a União"),
   com exemplos tirados de laudos nossos no prompt. opiniões, avisos e recomendações ficam de fora.
2. **rotular** cada afirmação em duas perguntas:
   - **a fonte citada sustenta?** abre o [E#] citado (`ler_pagina` ou a mesma consulta à base) → *sustentada*,
     *não sustentada* ou *contradita*;
   - **é verdadeira?** quando não há citação (comum no LLM puro), o verificador busca a fonte sozinho.
3. **calcular** a nota e as demais métricas (2.3).

### 2.2 · as 4 fases (versões comparadas)

as quatro rodam sobre os mesmos imóveis.

| fase | versão | o que é | o que isola |
|:--|:--|:--|:--|
| **A** | Claude puro | claude.ai com busca na web e o pedido "monta um laudo técnico do prédio X…" | o que um movimento faria hoje |
| **B** | Claude com o nosso prompt | um agente só, com o prompt do redator e busca na web | o valor do **prompt** |
| **C** | Chão Público sem revisor | os agentes com a correção desligada (opção do modo desenvolvedor) | o valor das **ferramentas e do dossiê** |
| **D** | Chão Público completo | o fluxo de hoje | o valor do **revisor** |

leitura: se B ficar perto de D, a vantagem é só o prompt. se C ganhar de B, as ferramentas se pagam. se D
ganhar de C, o revisor se paga.

### 2.3 · métricas, por versão

- **FActScore:** porcentagem de afirmações sustentadas.
- **taxa de contradição:** porcentagem de afirmações contraditas. é a mais grave: o número errado que queima o
  movimento.
- **cobertura:** dos campos esperados (dono, IPTU ano a ano, inundação, lei de PEUC no município, gasto
  público…), quantos o laudo preencheu com afirmação sustentada. o FActScore mede só precisão: um laudo que diz
  "não encontrado" para tudo tira 100%. a cobertura evita isso.
- **violações de regra:** nome ou CPF de pessoa física, acusação de fraude, "serve para moradia".
- **custo e tempo** por laudo.

### 2.4 · cuidados

1. **calibrar o verificador:** anotar umas 100 afirmações à mão e medir a concordância com o verificador
   automático, como o FActScore fez (erro abaixo de 2%). sem isso, a nota é um modelo dando nota a outro.
2. **verificador de outro modelo:** de preferência de outro provedor (Gemini, GPT), ou no mínimo diferente do
   que gerou o laudo. Claude não julga Claude.
3. **mesmas condições:** o mesmo pedido em todas as fases, na mesma semana (as bases mudam), salvando o texto
   de cada laudo.

### 2.5 · tamanho

- 5 a 8 imóveis no Recife: prédio público, prédio privado e pelo menos um caso com pouca informação.
- 4 fases × 6 imóveis = 24 laudos, de 30 a 60 afirmações cada.
- o maior custo é rodar o Chão Público (C e D); o verificador sai barato num modelo menor.
- trabalho humano: escolher os imóveis, rodar a fase A no claude.ai e anotar as 100 afirmações de calibração.

### 2.6 · o código (a fazer em `chao_publico/avaliacao/`)

| arquivo | o que faz |
|:--|:--|
| `extrair.py` | laudo → lista de afirmações atômicas, cada uma com o [E#] citado, se houver |
| `verificar.py` | abre a fonte citada (ou busca uma) e rotula: sustentada, não sustentada, contradita. reaproveita `ler_pagina` e as consultas de `fontes.py` |
| `metricas.py` | FActScore, contradição, cobertura e violações; gera um CSV por fase |
| `calibrar.py` | compara os rótulos do verificador com a anotação humana e mede a concordância |

cerca de 300 linhas: metade do trabalho (abrir páginas, consultar bases) já existe no Chão Público.

**como escrever no trabalho:** "adaptamos o método do FActScore (Min et al., EMNLP 2023) para textos com
citação: cada afirmação é verificada contra a fonte que o próprio laudo cita, como no ALCE (Gao et al., EMNLP
2023), e o verificador é validado contra anotação humana."

o resultado alimenta o § 7 do [cmp.md](cmp.md) ("tentei derrubar").
