# Tech Challenge FIAP — Fase 3

Machine Learning e inteligência analítica para alfabetização no Brasil.

## Índice

- [Visão geral](#visão-geral)
- [Apresentação executiva](#apresentação-executiva)
- [Problema e objetivo](#problema-e-objetivo)
- [Dados e escopo](#dados-e-escopo)
- [Análise exploratória e qualidade](#análise-exploratória-e-qualidade)
- [Preparação e prevenção de leakage](#preparação-e-prevenção-de-leakage)
- [Modelagem e seleção](#modelagem-e-seleção)
- [Avaliação final](#avaliação-final)
- [Interpretação e aplicação](#interpretação-e-aplicação)
- [Notebooks](#notebooks)
- [Execução rápida](#execução-rápida)
- [Estrutura do repositório](#estrutura-do-repositório)
- [Documentação detalhada](#documentação-detalhada)
- [Limitações e uso responsável](#limitações-e-uso-responsável)
- [Referência técnica](#referência-técnica)

## Visão geral

O projeto desenvolve uma pipeline supervisionada para estimar a probabilidade de um aluno das redes estadual ou municipal ser classificado como alfabetizado. A solução integra dados educacionais, territoriais, socioeconômicos, financeiros e de infraestrutura, com prevenção explícita de data leakage, validação agrupada, teste independente e interpretabilidade.

O notebook consolidado é a referência para reprodução integral. Os notebooks modulares apresentam cada etapa separadamente para facilitar a avaliação acadêmica.

O trabalho percorre o ciclo de uma solução de Machine Learning: entendimento e integração das fontes, análise exploratória, preparação dos dados, comparação de algoritmos, otimização, avaliação independente e comunicação dos resultados. A entrega inclui o modelo serializado, métricas, tabelas, visualizações e uma análise gerencial baseada em grupos reais do conjunto de teste.

O principal resultado é um Random Forest com **ROC AUC de 0,67048 no teste independente**. Esse desempenho indica sinal preditivo, mas também limita a precisão das conclusões: os dados contextuais ajudam a caracterizar padrões educacionais, sem explicar integralmente a alfabetização de cada aluno. A contribuição do projeto combina essa avaliação quantitativa com um processo rastreável e uma leitura responsável dos resultados.

Para avaliação acadêmica, este README apresenta a narrativa completa do trabalho. As seções seguintes explicam o que foi feito, por que as decisões foram adotadas e como interpretar os resultados; os links ao final de cada tema levam às evidências e aos procedimentos detalhados.

> Para navegar por toda a documentação, consulte o [índice técnico](docs/INDICE.md).


## Apresentação executiva

Consulte os [slides em PowerPoint](docs/apresentacao/apresentacao.pptx) e o vídeo da apresentação executiva, disponível no [YouTube](https://youtu.be/IDaZaM82j6s) e como [arquivo MP4 local](docs/apresentacao/apresentacao.mp4).

## Problema e objetivo

O objetivo central é avaliar em que medida variáveis contextuais disponíveis permitem estimar alfabetização e produzir evidências agregadas úteis para gestores e pesquisadores.

A tarefa é uma **classificação binária**, cujo alvo é `alfabetizado`. A unidade preditiva é o registro de aluno, enquanto a interpretação gerencial utiliza agregações por município, UF, rede e ano. Essa distinção é necessária porque grande parte das variáveis disponíveis descreve o território, e não as condições individuais do aluno.

O trabalho procura responder três perguntas: há sinal preditivo nas fontes integradas? Quais variáveis e contextos estão associados às estimativas do modelo? Como os resultados agregados podem apoiar a investigação de diferenças territoriais e da distância em relação às metas oficiais?

Para responder a essas perguntas, o sucesso técnico não se resume a uma métrica elevada. Também exige comparar o modelo com um baseline, impedir vazamento de informação, preservar um teste independente e registrar as condições de execução e os limites das análises.

A solução não demonstra causalidade e não deve fundamentar decisões individuais automatizadas. O resultado deve ser interpretado como capacidade preditiva e associação contextual.

Detalhes: [problema, objetivos e escopo](docs/PROBLEMA_OBJETIVOS_ESCOPO.md).

## Dados e escopo

A base principal é a Feature Table `ml_aluno`, complementada por Censo Escolar, INSE, Bolsa Família, Fundeb, receitas municipais, PIB municipal e metas oficiais de alfabetização.

| Fonte | Contribuição para a análise | Regra de utilização |
|---|---|---|
| `ml_aluno` | classificação de alfabetização, chaves e contexto educacional | registros de 2023 e 2024 das redes estadual e municipal |
| Censo Escolar e INSE | infraestrutura e contexto socioeconômico municipal | snapshot de 2023 aplicado aos dois anos |
| Bolsa Família, Fundeb e receitas municipais | contexto de transferência de renda, financiamento e capacidade fiscal | correspondência com o ano do registro |
| PIB municipal | contexto econômico por meio do PIB per capita | defasagem de um ano |
| Metas oficiais | referência para análise posterior das estimativas agregadas | excluídas das features e da seleção do modelo |

Os identificadores de escola da base principal são anonimizados e não permitem uma ligação pública segura com o código de escola do Censo. Por isso, os indicadores escolares complementares foram agregados no nível municipal antes da integração. Uma proporção de escolas com biblioteca, por exemplo, caracteriza o município e não confirma que o aluno frequente uma escola com esse recurso. A rede privada foi excluída por cobertura insuficiente.

Pontos centrais:

- registros dos anos de 2023 e 2024;
- redes estadual e municipal;
- variáveis complementares integradas majoritariamente no nível municipal;
- Censo e INSE como snapshots contextuais de 2023;
- PIB com defasagem de um ano;
- metas utilizadas somente depois da modelagem;
- São Paulo presente apenas em 2024.

Detalhes:

- [fontes, integração e granularidade](docs/FONTES_INTEGRACAO_GRANULARIDADE.md);
- [catálogo de variáveis da base principal](docs/dados/CATALOGO_VARIAVEIS_ML_ALUNO.md);
- [dicionário de campos das bases complementares](docs/dados/DICIONARIO_BASES_COMPLEMENTARES.md);
- [aquisição e linhagem](docs/AQUISICAO_LINHAGEM_FONTES.md);
- [análise exploratória e qualidade](docs/EDA_QUALIDADE_DADOS.md).

## Análise exploratória e qualidade

A análise exploratória examina distribuição do alvo, balanceamento das classes, valores ausentes, duplicidades, outliers e relações entre variáveis. Também compara recortes territoriais, redes de ensino e anos para verificar se as diferenças observadas podem ser interpretadas sob a mesma cobertura.

A integração das fontes é acompanhada por verificações de tipos, chaves, contagens e cobertura. Duplicidades nas bases complementares precisam ser resolvidas antes dos cruzamentos para evitar multiplicar registros de alunos. Ausências de dados complementares permanecem identificadas; falta de informação não é interpretada automaticamente como ausência de recurso ou valor financeiro zero.

As principais restrições afetam diretamente a leitura dos resultados: São Paulo aparece somente em 2024; Censo e INSE não representam uma atualização entre os dois anos; valores financeiros extremos podem refletir o porte municipal. Transformações logarítmicas ajudam a reduzir assimetrias, mas não convertem montantes totais em investimento por aluno. Com apenas dois anos, as comparações temporais descrevem diferenças de curto prazo.

Detalhes e evidências: [análise exploratória e qualidade dos dados](docs/EDA_QUALIDADE_DADOS.md).

## Preparação e prevenção de leakage

O contrato final contém 18 features não constantes. Informações diretamente relacionadas à própria avaliação, como `proficiencia`, `presenca`, `preenchimento_caderno` e `caderno`, foram excluídas. Identificadores e chaves de controle também não são utilizados como features.

Imputação, encoding e transformações são ajustados exclusivamente no treino. A seed padrão é 42 e a validação usa agrupamento por `chave_escola_ano` quando aplicável.

O contrato de entrada reúne UF, rede, ano, variáveis financeiras transformadas, INSE, oito proporções municipais de infraestrutura e indicadores de ausência de cobertura. Manter esse contrato explícito permite comparar os algoritmos com as mesmas informações e verificar a compatibilidade entre base, pré-processamento e modelo final.

A exclusão de variáveis da própria avaliação evita que o modelo receba informações que antecipem diretamente o resultado que deveria estimar. Já o ajuste do pré-processamento somente no treino impede que estatísticas da validação ou do teste influenciem a preparação. O agrupamento por escola/ano busca evitar que registros do mesmo grupo apareçam simultaneamente no treino e na validação agrupada; isso não equivale a demonstrar generalização para anos futuros ou territórios inéditos.

Detalhes: [preparação, features e prevenção de leakage](docs/PREPARACAO_FEATURES_LEAKAGE.md).

## Modelagem e seleção

A modelagem inicial compara:

- baseline Dummy;
- Regressão Logística;
- KNN;
- SVM linear;
- Árvore de Decisão;
- Random Forest;
- Gradient Boosting.

Regressão Logística, Random Forest e Gradient Boosting avançaram para otimização sob o mesmo contrato. Random Forest foi selecionado antes do acesso ao teste por desempenho em validação agrupada, gap de generalização e F1.

O Dummy fornece uma referência mínima para verificar o ganho da modelagem. Os demais algoritmos permitem comparar relações lineares, vizinhança, árvores e conjuntos de árvores. A etapa inicial organiza essa comparação; a otimização concentra o orçamento nos três finalistas, sob protocolo comum de amostragem, features e validação.

A seleção considera tanto as métricas de validação quanto a distância entre treino e validação, usada como diagnóstico de generalização. Random Forest e Gradient Boosting ficaram em empate técnico pelo critério adotado; a escolha do Random Forest também considerou o menor gap e o F1 ligeiramente superior. Assim, a decisão não depende de uma diferença isolada de AUC.

| Modelo finalista | ROC AUC de validação | Average Precision | Balanced Accuracy | F1 |
|---|---:|---:|---:|---:|
| Random Forest | 0,65646 | 0,66565 | 0,61082 | 0,63460 |
| Gradient Boosting | 0,65578 | 0,66546 | 0,61036 | 0,62493 |
| Regressão Logística | 0,59168 | 0,59902 | 0,56047 | 0,57453 |

Detalhes:

- [modelagem inicial](docs/MODELAGEM_INICIAL.md);
- [otimização, validação e seleção](docs/OTIMIZACAO_VALIDACAO.md).

## Avaliação final

O Random Forest congelado foi avaliado uma única vez em 581.591 registros do teste independente.

| Métrica | Resultado |
|---|---:|
| ROC AUC | 0,67048 |
| Average Precision | 0,68410 |
| Balanced Accuracy | 0,61962 |
| F1 | 0,63919 |

A execução GPU validada utilizou Python 3.12.11, scikit-learn 1.7.2, Polars 2.0.0, RAPIDS cuML, RTX 3050 Laptop com 6 GB de VRAM e SHAP com 100 observações.

As métricas respondem a aspectos diferentes. ROC AUC mede a capacidade de ordenar positivos acima de negativos ao variar o limiar; Average Precision resume a relação entre precisão e recuperação da classe positiva. Balanced Accuracy equilibra a recuperação das duas classes, enquanto F1 combina precisão e recuperação da classe positiva no limiar utilizado. Nenhuma dessas medidas representa a confiança de uma previsão individual.

O ROC AUC teve intervalo de confiança de 95% de **0,6673 a 0,6737** na avaliação registrada. O conjunto dos resultados indica desempenho moderado: existe informação útil nas fontes, mas uma parcela relevante da variação permanece fora do alcance do modelo. Calibração, matriz de confusão e estabilidade por ano, rede e UF complementam a avaliação para evitar que uma única média esconda diferenças entre recortes.

Após a seleção, algoritmo, features, hiperparâmetros e protocolo permaneceram congelados para a avaliação oficial. As análises descritivas posteriores do teste não são usadas para retornar à otimização. Reexecutar a análise gerencial com o modelo já congelado serve à comunicação dos resultados, sem constituir uma nova seleção de modelo.

Detalhes: [avaliação final e interpretabilidade](docs/AVALIACAO_INTERPRETABILIDADE.md).

## Interpretação e aplicação

Importância por permutação, SHAP e sensibilidade com e sem `sigla_uf` descrevem o comportamento do modelo. As variáveis relevantes são sinais preditivos contextuais, não causas da alfabetização.

As probabilidades foram agregadas por município e comparadas às metas oficiais quando existe correspondência no mesmo grão. O déficit representa risco condicionado ao cenário observado, não uma projeção temporal completa até 2030.

Entre os sinais de maior importância preditiva estão UF, valor de Bolsa Família transformado, INSE médio, rede e proporção municipal de escolas com laboratório de informática. A importância por permutação mede a perda de desempenho ao embaralhar uma variável; SHAP complementa a descrição das contribuições do modelo em uma amostra controlada. Esses métodos explicam o comportamento preditivo observado e precisam ser lidos junto às limitações de cobertura e granularidade.

Os produtos analíticos incluem comparações de infraestrutura e INSE, leitura de variáveis financeiras, persistência municipal entre 2023 e 2024 e agrupamentos de perfis contextuais. Foram identificados três perfis municipais, com silhouette de **0,241**, o que recomenda tratar os grupos como uma organização descritiva dos contextos. A persistência foi examinada em **5.653 pares município-rede comparáveis**, com correlação de Spearman observada de **0,447**; isso não estabelece uma trajetória histórica de longo prazo.

Na comparação com metas, o déficit é calculado como **meta menos probabilidade média estimada**. A correspondência deve respeitar município, rede e referência da publicação; municípios sem meta correspondente permanecem identificados. Um déficit positivo descreve uma distância no cenário analisado, sem garantir que ela persistirá ou que a meta deixará de ser cumprida.

O notebook gerencial traduz essas evidências para apresentação ao comparar grupos reais do teste: mostra quantidade de registros, proporção observada de alfabetização e média das probabilidades estimadas. Para infraestrutura e INSE, os limites dos grupos são definidos no desenvolvimento e aplicados ao teste. Como os grupos também diferem em outras características, os contrastes orientam perguntas e investigação, sem medir o efeito de uma intervenção.

A leitura integrada dos resultados, de sua utilidade e de seus limites está na [análise final](docs/resultados/RESULTADOS_ARTEFATOS_ANALITICOS.md#análise-final).

Detalhes:

- [metas e perguntas de negócio](docs/METAS_PERGUNTAS_NEGOCIO.md);
- [limitações, ética e uso responsável](docs/LIMITACOES_ETICA.md).

## Notebooks

### Notebooks de comunicação dos resultados

Dois notebooks complementam a avaliação acadêmica e a apresentação executiva, com funções distintas:

| Notebook | Finalidade | Documentação própria |
|---|---|---|
| [TC3_Visualizacoes_e_Insights.ipynb](notebooks/TC3_Visualizacoes_e_Insights.ipynb) | síntese visual das perguntas norteadoras, com resultados previamente registrados, imagens incorporadas e leitura do CSV financeiro | [Visualizações e insights](docs/VISUALIZACOES_E_INSIGHTS.md) |
| [TC3_Analise_Gerencial_Random_Forest.ipynb](notebooks/TC3_Analise_Gerencial_Random_Forest.ipynb) | carrega o modelo final, calcula probabilidades para grupos reais do teste e gera quatro figuras para apresentação | [Análise gerencial do Random Forest](docs/ANALISE_GERENCIAL_RANDOM_FOREST.md) |

Para uma leitura executiva das perguntas do trabalho, comece por Visualizações e Insights. Para examinar os contrastes entre grupos e a preparação das figuras gerenciais, consulte a Análise Gerencial. Nenhum dos dois treina ou ajusta o modelo. Os documentos próprios explicam entradas, execução, produtos e cuidados de atualização; o pipeline consolidado permanece a referência oficial.

### Fluxo consolidado

```text
notebooks/TC3_Pipeline_Completo_Alfabetizacao.ipynb
```

É a referência metodológica para execução integral, métricas finais e artefatos oficiais. O notebook não possui uma chave de tarefa própria: ele está vinculado à chave geral do projeto por consolidar o trabalho de várias atividades. A divisão modular é a forma recomendada de desenvolver, revisar e apresentar cada etapa; o consolidado foi mantido para permitir a execução sequencial e sem interrupções de todo o pipeline, inclusive durante a noite.

Como a execução contínua validada foi realizada por esse arquivo, ele é adotado como fonte de verdade. A justificativa completa está em [organização interna e rastreabilidade no Jira](docs/jira/ORGANIZACAO_INTERNA.md#notebook-consolidado-e-chave-do-projeto).

### Fluxo modular

O particionamento organiza a análise detalhada na seguinte sequência:

1. auditoria, entendimento e integração das bases;
2. análise exploratória e qualidade dos dados;
3. preparação e contrato de modelagem;
4. baseline e comparação dos modelos iniciais;
5. otimização e seleção do modelo;
6. avaliação final independente;
7. visualizações e comunicação dos resultados.

Os identificadores presentes nos nomes de alguns notebooks servem apenas para rastreabilidade do desenvolvimento. A ordem de leitura e execução é definida pelas fases metodológicas acima, não pela numeração desses identificadores.

A execução modular apresentou pequenas diferenças numéricas em relação à execução integral, sem alterar o modelo selecionado nem as conclusões do projeto. Essa estabilidade dentro das tolerâncias esperadas reforça a reprodutibilidade operacional; os valores oficiais permanecem os do pipeline consolidado. Consulte a [comparação entre execuções](docs/GUIA_EXECUCAO_REPRODUTIBILIDADE.md#14-comparação-e-equivalência-entre-execuções).

Consulte a [ordem detalhada e os modos de execução](docs/GUIA_EXECUCAO_REPRODUTIBILIDADE.md#9-formas-de-executar-os-notebooks).

## Execução rápida

Os comandos abaixo iniciam o JupyterLab nos ambientes Docker. A reprodução da análise também requer as fontes locais e os artefatos das etapas anteriores: abrir o ambiente não baixa automaticamente toda a base do projeto. Para reproduzir o fluxo completo, abra o notebook consolidado e execute **Restart Kernel and Run All Cells** após conferir os pré-requisitos do guia de execução.

### CPU

```powershell
docker compose build notebook-cpu
docker compose up -d notebook-cpu
```

Abra `http://localhost:8888` e selecione `Python 3 (tc3-cpu)`.

### GPU

```powershell
docker compose --profile gpu build notebook-gpu
docker compose --profile gpu up -d notebook-gpu
```

Abra `http://localhost:8889` e selecione `Python 3 (tc3-gpu)`.

Para instalação local, requisitos de hardware, validação, logs, parada e reconstrução separadas, consulte o [guia completo de execução](docs/GUIA_EXECUCAO_REPRODUTIBILIDADE.md).

## Estrutura do repositório

```text
tech_challenge_3/
|-- notebooks/
|   |-- TC3_Pipeline_Completo_Alfabetizacao.ipynb
|   |-- fase_2_entendimento_base_dados/
|   |-- fase_3_analise_exploratoria_de_dados/
|   |-- fase_4_preparacao/
|   |-- fase_5_modelagem/
|   |-- fase_6_otimizacao/
|   `-- fase_7_avaliacao_independente/
|-- dados/
|   |-- fontes_originais/
|   |-- dados_processados/
|   `-- dados_analiticos/
|-- modelos/
|-- resultados/
|   |-- metricas/
|   |-- tabelas/
|   |-- figuras/
|   `-- relatorios/
|-- docs/
|-- Dockerfile
|-- Dockerfile.gpu
|-- compose.yaml
`-- requirements.txt
```

Documentos específicos das pastas:

- [aquisição, organização e linhagem das fontes](docs/AQUISICAO_LINHAGEM_FONTES.md);
- [resultados e artefatos analíticos](docs/resultados/RESULTADOS_ARTEFATOS_ANALITICOS.md).

## Documentação detalhada

| Tema | Documento |
|---|---|
| slides da apresentação executiva | [PowerPoint](docs/apresentacao/apresentacao.pptx) |
| vídeo da apresentação executiva | [MP4 local](docs/apresentacao/apresentacao.mp4) e [YouTube](https://youtu.be/IDaZaM82j6s) |
| problema e escopo | [PROBLEMA_OBJETIVOS_ESCOPO.md](docs/PROBLEMA_OBJETIVOS_ESCOPO.md) |
| fontes e granularidade | [FONTES_INTEGRACAO_GRANULARIDADE.md](docs/FONTES_INTEGRACAO_GRANULARIDADE.md) |
| variáveis e metadados da base principal | [CATALOGO_VARIAVEIS_ML_ALUNO.md](docs/dados/CATALOGO_VARIAVEIS_ML_ALUNO.md) |
| campos das bases complementares | [DICIONARIO_BASES_COMPLEMENTARES.md](docs/dados/DICIONARIO_BASES_COMPLEMENTARES.md) |
| EDA e qualidade | [EDA_QUALIDADE_DADOS.md](docs/EDA_QUALIDADE_DADOS.md) |
| preparação e leakage | [PREPARACAO_FEATURES_LEAKAGE.md](docs/PREPARACAO_FEATURES_LEAKAGE.md) |
| modelagem inicial | [MODELAGEM_INICIAL.md](docs/MODELAGEM_INICIAL.md) |
| otimização e seleção | [OTIMIZACAO_VALIDACAO.md](docs/OTIMIZACAO_VALIDACAO.md) |
| avaliação final | [AVALIACAO_INTERPRETABILIDADE.md](docs/AVALIACAO_INTERPRETABILIDADE.md) |
| metas e negócio | [METAS_PERGUNTAS_NEGOCIO.md](docs/METAS_PERGUNTAS_NEGOCIO.md) |
| ética e limitações | [LIMITACOES_ETICA.md](docs/LIMITACOES_ETICA.md) |
| aquisição e linhagem | [AQUISICAO_LINHAGEM_FONTES.md](docs/AQUISICAO_LINHAGEM_FONTES.md) |
| execução CPU/GPU | [GUIA_EXECUCAO_REPRODUTIBILIDADE.md](docs/GUIA_EXECUCAO_REPRODUTIBILIDADE.md) |
| navegação e evidências | [GUIA_NAVEGACAO_EVIDENCIAS.md](docs/GUIA_NAVEGACAO_EVIDENCIAS.md) |
| síntese visual das perguntas norteadoras | [VISUALIZACOES_E_INSIGHTS.md](docs/VISUALIZACOES_E_INSIGHTS.md) |
| comparações gerenciais com o modelo final | [ANALISE_GERENCIAL_RANDOM_FOREST.md](docs/ANALISE_GERENCIAL_RANDOM_FOREST.md) |
| interpretação dos resultados e reprodução das figuras gerenciais | [RESULTADOS_ARTEFATOS_ANALITICOS.md](docs/resultados/RESULTADOS_ARTEFATOS_ANALITICOS.md) |

## Limitações e uso responsável

- o modelo trabalha principalmente com contexto territorial e municipal;
- infraestrutura não representa diretamente a escola frequentada;
- valores financeiros podem refletir o porte do município;
- existem somente dois anos de observação;
- predição e importância de variáveis não demonstram causalidade;
- resultados agregados não devem ser usados para punir territórios ou decidir sobre indivíduos.

Leia as orientações completas em [limitações, ética e uso responsável](docs/LIMITACOES_ETICA.md).

## Referência técnica

O pipeline consolidado é a fonte de verdade para métricas, decisões e artefatos oficiais. O fluxo modular é a apresentação recomendada para avaliação detalhada e deve permanecer alinhado às decisões oficiais do consolidado.

Consulte a [justificativa de rastreabilidade](docs/jira/ORGANIZACAO_INTERNA.md#notebook-consolidado-e-chave-do-projeto) e o [guia de navegação e evidências](docs/GUIA_NAVEGACAO_EVIDENCIAS.md).
