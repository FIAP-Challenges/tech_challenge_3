# Tech Challenge FIAP — Fase 3

Machine Learning e inteligência analítica para alfabetização no Brasil.

## Índice

- [Visão geral](#visão-geral)
- [Problema e objetivo](#problema-e-objetivo)
- [Dados e escopo](#dados-e-escopo)
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

> Para navegar por toda a documentação, consulte o [índice técnico](docs/INDICE.md).

## Problema e objetivo

O objetivo central é avaliar em que medida variáveis contextuais disponíveis permitem estimar alfabetização e produzir evidências agregadas úteis para gestores e pesquisadores.

A solução não demonstra causalidade e não deve fundamentar decisões individuais automatizadas. O resultado deve ser interpretado como capacidade preditiva e associação contextual.

Detalhes: [problema, objetivos e escopo](docs/PROBLEMA_OBJETIVOS_ESCOPO.md).

## Dados e escopo

A base principal é a Feature Table `ml_aluno`, complementada por Censo Escolar, INSE, Bolsa Família, Fundeb, receitas municipais, PIB municipal e metas oficiais de alfabetização.

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
- [aquisição e linhagem](docs/AQUISICAO_LINHAGEM_FONTES.md);
- [análise exploratória e qualidade](docs/EDA_QUALIDADE_DADOS.md).

## Preparação e prevenção de leakage

O contrato final contém 18 features não constantes. Informações diretamente relacionadas à própria avaliação, como `proficiencia`, `presenca`, `preenchimento_caderno` e `caderno`, foram excluídas. Identificadores e chaves de controle também não são utilizados como features.

Imputação, encoding e transformações são ajustados exclusivamente no treino. A seed padrão é 42 e a validação usa agrupamento por `chave_escola_ano` quando aplicável.

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

Detalhes: [avaliação final e interpretabilidade](docs/AVALIACAO_INTERPRETABILIDADE.md).

## Interpretação e aplicação

Importância por permutação, SHAP e sensibilidade com e sem `sigla_uf` descrevem o comportamento do modelo. As variáveis relevantes são sinais preditivos contextuais, não causas da alfabetização.

As probabilidades foram agregadas por município e comparadas às metas oficiais quando existe correspondência no mesmo grão. O déficit representa risco condicionado ao cenário observado, não uma projeção temporal completa até 2030.

A leitura integrada dos resultados, de sua utilidade e de seus limites está na [análise final](docs/resultados/RESULTADOS_ARTEFATOS_ANALITICOS.md#análise-final).

Detalhes:

- [metas e perguntas de negócio](docs/METAS_PERGUNTAS_NEGOCIO.md);
- [limitações, ética e uso responsável](docs/LIMITACOES_ETICA.md).

## Notebooks

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
| problema e escopo | [PROBLEMA_OBJETIVOS_ESCOPO.md](docs/PROBLEMA_OBJETIVOS_ESCOPO.md) |
| fontes e granularidade | [FONTES_INTEGRACAO_GRANULARIDADE.md](docs/FONTES_INTEGRACAO_GRANULARIDADE.md) |
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
