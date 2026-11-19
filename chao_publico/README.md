# Chão Público: protótipo

Chat em que um movimento social, a Defesa Civil ou um órgão público descreve um **imóvel ocioso** (prédio ou
terreno público sem uso, ou imóvel privado abandonado) e três agentes de IA devolvem um laudo com fonte para cada
número:
- **quanto o abandono custa ao poder público**;
- a **situação fiscal e os instrumentos da função social**: IPTU lançado ano a ano, alíquota efetiva (indício
  de IPTU progressivo), dívida de IPTU, PEUC, arrecadação por abandono. Entra quando faz sentido: imóvel
  privado, ou público com cobrança de IPTU;
- uma **ficha de aptidão para função social** (riscos como enchente, área, conservação, entorno). O laudo
  não escolhe o uso: se vira moradia, abrigo ou creche é decisão do órgão responsável.

A ideia completa e o estudo de competidores estão em [../projeto_disciplina/cmp.md](../projeto_disciplina/cmp.md).

Cada pessoa usa **a própria chave da API da Anthropic**, colada na barra lateral. A chave fica só na memória da
sessão do navegador: não é gravada em disco.

## Como rodar

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Os agentes

| agente | o que faz | ferramentas |
|:--|:--|:--|
| **Pesquisador** | reúne os fatos e registra cada um no dossiê (E1, E2…) com URL e trecho literal | bases públicas abaixo + busca e leitura na web |
| **Redator** | escreve o laudo **só** com o dossiê; o que falta vira "não encontrado" | nenhuma |
| **Revisor** | parte de "não passa", confere cada número contra o trecho da fonte, refaz as consultas às bases, abre links, dá o veredito | as mesmas bases do pesquisador (sem registrar evidência) + leitura na web |

A revisão é **interna**: quem usa o app recebe só o laudo final. Se o revisor apontar problema grave ou médio,
o redator corrige e o revisor confere de novo, até 2 rodadas. Se ainda sobrar problema, o redator faz uma
versão conservadora que **retira** o que não pôde ser confirmado, sem acrescentar nada. O laudo entregue nunca
carrega um erro que o revisor apontou. O código do fluxo está em [agentes.py](agentes.py).

Com `MODO_DESENVOLVEDOR=1` no `.env`, o app mostra também as revisões, as notas do pesquisador e o veredito de
cada consulta, para quem está ajustando os agentes.

Regras que vieram da auditoria do `cmp.md`:
- o custo do abandono soma **só** o que a fonte atribui a este imóvel; contrato que cobre vários imóveis fica
  fora da soma e aparece à parte ("custo mínimo comprovado");
- a ficha de aptidão nunca recomenda um uso nem diz "serve": as saídas são *apto para avaliação de
  destinação*, *apto com restrições* (as duas pendentes de vistoria), *não recomendado para ocupação* ou
  *dados insuficientes*;
- "não encontrado nas bases" nunca vira "não existe" ou "o município não aplica";
- quando o abandono fica inconclusivo mas há indícios, o laudo ganha a seção *Indícios de ociosidade e
  vistoria recomendada*: põe lado a lado os sinais de uso e de ociosidade (funcionário ou vigia no local não
  prova função social) e recomenda vistoria à fiscalização tributária, ao órgão do PEUC e, se houver risco, à
  Defesa Civil. O laudo nunca afirma fraude: a divergência entre uso declarado e real é apurada pelo fisco;
- pessoa física nunca é nomeada (nem CPF mascarado): aparece como "proprietário pessoa física";
- as normas (função social: CF arts. 5º, XXIII, e 182; Estatuto da Cidade, arts. 5º a 8º; Código Civil,
  art. 1.276; Lei 13.465/2017, arts. 64 e 65; e, para imóvel público, CF art. 23, IX, Lei 11.124/2005,
  Lei 14.133/2021, Decreto 11.929/2024 e Lei 12.608/2012) saem marcadas para conferência.

## Bases consultadas (testadas em 13/11/2026)

| base | para quê | precisa de chave? |
|:--|:--|:--|
| Serviço Geológico do Brasil, camadas `suscet_inundacao` e `risco_geologico` | suscetibilidade a inundação no ponto (ficha de aptidão) | não |
| Prefeitura do Recife, dados abertos de IPTU (2005–2026, por unidade) | IPTU lançado, valor venal, alíquota efetiva ano a ano, regime (normal, imune…) | não |
| Compras.gov.br, módulo contratos | contratos federais de vigilância, manutenção etc. | não |
| portais CKAN `dados.<ente>.gov.br` (ex.: Recife: "Imóveis da Administração Pública Municipal") | cadastro de imóveis municipais e estaduais | não |
| OpenStreetMap / Nominatim | endereço → coordenadas | não |
| BrasilAPI (CNPJ), IBGE (municípios) | identificar órgão e município | não |
| Portal da Transparência (CGU) | contratos e despesas | sim, gratuita, informada pelo usuário |
| catálogo dados.gov.br | achar bases federais (ex.: os 4 conjuntos "Imóveis da União" da SPU) | sim: token do perfil Consumidor, em *Minha Conta* |
| SPU, Imóveis da União: pontos georreferenciados (GeoJSON) | o prédio está no cadastro da União? RIP, situação, destinação | não, mas o site bloqueia download automático: [baixe no navegador](https://drive.spu.gestao.gov.br/index.php/s/xbmeGFJpNDigXEm/download) e salve em `dados/spu_pontos.geojson` |
| busca e leitura na web (ferramentas do servidor da Anthropic) | SPU, Diário Oficial, TCU/TCE, imprensa | não (cobradas na chave da Anthropic) |

Ficaram de fora por enquanto: a busca textual do PNCP e as bases de cartório (matrícula é paga).

### Chaves locais

Quem usa o app cola as próprias chaves na barra lateral. A tela **Como começar** explica, com links para os sites
do governo, como conseguir cada uma e para que serve. O projeto não distribui chave de ninguém.

Quem roda o app no próprio computador pode deixar as chaves das bases num arquivo `chao_publico/.env`. Elas
ficam no servidor, e a barra lateral só avisa que estão em uso: o valor não vai para o navegador. O `.env` e a
pasta `dados/` estão no `.gitignore` e **não vão para o GitHub**.

```
DADOS_GOV_TOKEN=...
PORTAL_TRANSPARENCIA_CHAVE=...
MODO_ASSINATURA=1
```

`MODO_ASSINATURA=1` mostra na barra lateral a opção de rodar os agentes com o login do Claude Code de quem
roda o app (via Claude Agent SDK, em [assinatura.py](assinatura.py)), sem chave de API. É só para testes
locais: a assinatura é pessoal, e um app publicado deve exigir a chave de cada pessoa. Sem essa linha, a
opção não aparece.

## Custo

A barra lateral mostra uma estimativa em dólares. O padrão é o Claude Opus 5.5, e dá para trocar para o
Sonnet 5.5 ou o Haiku 5.5, que são mais baratos. Uma consulta completa faz várias buscas na web
(US$ 10 a cada mil buscas) e de 5 a 7 chamadas ao modelo.

## Arquivos

- [app.py](app.py): interface de chat (Streamlit), com as telas *Consulta* e *Imóveis laudados* (mapa)
- [agentes.py](agentes.py): os agentes (pesquisador, redator, revisor e pedidos de LAI), seus prompts e o laço
  de ferramentas
- [fontes.py](fontes.py): as ferramentas de consulta às bases públicas, inclusive a leitura própria de páginas
  e PDFs (`ler_pagina`), que tenta a cópia do Wayback Machine quando o site saiu do ar ou só abre no navegador
- [exportar.py](exportar.py): laudo e pedidos em PDF
- [historico.py](historico.py): laudos salvos em `dados/laudos/` (fora do Git), que alimentam o mapa
- [assinatura.py](assinatura.py): modo de testes com a assinatura do Claude Code

## Depois do laudo

- **PDF e .md:** o laudo baixa nos dois formatos.
- **Pedidos de LAI:** um botão gera, a partir das lacunas do laudo, um pedido por órgão, com o canal de
  protocolo (Fala.BR, e-SIC estadual ou municipal), o texto pronto, os prazos (20 + 10 dias) e o recurso
  (10 dias). Matrícula de cartório fica à parte, porque não é LAI.
- **Anexar documentos:** embaixo do laudo mais recente, a pessoa envia o que conseguiu (certidão de matrícula,
  resposta da LAI, certidão de débitos, vistoria) em PDF, texto ou foto. Um agente leitor registra os fatos no
  dossiê (sem nome nem CPF de pessoa física), e o laudo é reescrito e revisado. Documento oficial prevalece
  sobre inferência. PDF escaneado e foto só no modo chave de API; o modo assinatura lê só documento com texto.
- **Imóveis laudados:** cada consulta concluída é salva e vira um ponto no mapa, de onde pode ser reaberta
  para ajuste. Hoje fica no computador de quem roda o app; para várias pessoas usarem juntas, isso precisa
  virar um banco de dados compartilhado.
