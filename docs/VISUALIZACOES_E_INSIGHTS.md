# Visualizações e Insights

## Objetivo

O notebook tem como objetivo organizar e apresentar os resultados consolidados do projeto por meio de análises exploratórias, indicadores e gráficos.

Sua finalidade é facilitar a interpretação dos dados e apoiar a identificação de padrões relevantes para a alfabetização.

As visualizações também apoiam a análise das perguntas norteadoras do projeto, relacionando os resultados obtidos aos indicadores de infraestrutura escolar, contexto socioeconômico, desempenho municipal e metas educacionais.

O notebook utiliza resultados previamente produzidos pelo pipeline analítico, sem realizar novamente o treinamento dos modelos.

## Fontes de dados

As análises utilizam tabelas consolidadas, principalmente arquivos CSV disponíveis no diretório:

`resultados/tabelas/`

Também podem ser utilizados arquivos JSON contendo métricas de avaliação dos modelos.

Os conjuntos de dados contemplam informações relacionadas a:

- Indicadores de alfabetização;
- Infraestrutura escolar;
- Índice de Nível Socioeconômico (INSE);
- Indicadores municipais;
- Agrupamentos de municípios (*clusters*);
- Classificações de risco e metas educacionais;
- Resultados e métricas dos modelos preditivos.

As regras de preparação e consolidação dos dados pertencem às etapas anteriores do pipeline.

## Bibliotecas e ambiente

O notebook utiliza Python em ambiente compatível com Jupyter.

As principais bibliotecas empregadas são:

- **Pandas:** leitura e manipulação de dados.
- **NumPy:** operações numéricas.
- **Matplotlib:** construção de gráficos.
- **Seaborn:** visualizações estatísticas.
- **Pathlib:** gerenciamento de caminhos e diretórios.
- **JSON:** leitura de métricas consolidadas.

## Metodologia

O processo de análise e visualização é organizado nas seguintes etapas:

1. Localização dos arquivos no repositório.
2. Carregamento das tabelas consolidadas.
3. Inspeção das estruturas, colunas e valores ausentes.
4. Seleção e preparação dos indicadores.
5. Construção das visualizações.
6. Interpretação dos resultados e identificação de limitações.

As análises preservam os critérios de cálculo e classificação estabelecidos no pipeline original.

## Visualizações e análises

### Indicadores municipais e alfabetização

Exploração dos indicadores de alfabetização e das diferenças observadas entre municípios, períodos e agrupamentos disponíveis.

As comparações consideram a granularidade e a cobertura das informações utilizadas.

### Infraestrutura escolar

Análise das relações entre os indicadores de alfabetização e as condições de infraestrutura escolar, incluindo recursos educacionais e conectividade.

As visualizações permitem identificar padrões e associações, sem estabelecer relações diretas de causalidade.

### Contexto socioeconômico

Exploração do Índice de Nível Socioeconômico (INSE) e das correlações disponíveis.

Os resultados devem ser interpretados considerando que indicadores contextuais não representam necessariamente características individuais dos estudantes.

### Importância das variáveis e resultados preditivos

Apresentação de resultados previamente calculados pelo pipeline, incluindo métricas de avaliação e importância preditiva das variáveis, quando disponíveis.

A importância de uma variável no modelo não representa, isoladamente, um efeito causal sobre a alfabetização.

### Agrupamentos, risco e metas

Exploração dos agrupamentos municipais e das classificações de risco relacionadas às metas educacionais.

As categorias e os critérios utilizados seguem as definições presentes nas tabelas consolidadas do projeto.

## Reprodutibilidade

Para executar o notebook em outro ambiente:

1. Obter o repositório do projeto, preservando sua estrutura de diretórios.
2. Abrir o notebook na pasta `notebooks/`.
3. Verificar a disponibilidade das bibliotecas Python necessárias.
4. Confirmar a existência dos arquivos utilizados em `resultados/tabelas/` e nos demais diretórios referenciados.
5. Ajustar o caminho da raiz do projeto, caso necessário.
6. Executar as células na sequência apresentada.
7. Conferir eventuais mensagens relacionadas a arquivos ausentes ou diferenças na estrutura das tabelas.

A reprodução das visualizações depende da disponibilidade dos arquivos consolidados utilizados pelo notebook.

## Limitações

As análises apresentam algumas limitações metodológicas:

- A disponibilidade dos indicadores pode variar entre municípios e períodos.
- Diferenças na cobertura e composição das bases podem influenciar comparações temporais.
- Resultados com filtros e níveis de agregação distintos não devem ser comparados diretamente.
- Correlações e associações estatísticas não comprovam causalidade.
- A importância preditiva das variáveis depende do método utilizado pelo modelo.
- Probabilidades e projeções representam estimativas sujeitas a erro.
- As classificações de risco devem respeitar os critérios estabelecidos no pipeline original.

## Considerações finais

O notebook de Visualizações e Insights complementa as etapas de processamento e modelagem ao transformar resultados consolidados em representações gráficas e análises interpretáveis.

As visualizações contribuem para a compreensão dos indicadores educacionais, a identificação de padrões e a comunicação dos principais resultados, preservando as limitações metodológicas das informações utilizadas.