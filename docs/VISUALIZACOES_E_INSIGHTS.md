# Visualizações e insights

## Índice

- [Finalidade](#finalidade)
- [Conteúdo e origem dos resultados](#conteúdo-e-origem-dos-resultados)
- [Percurso de análise](#percurso-de-análise)
- [Pré-requisitos e execução](#pré-requisitos-e-execução)
- [Limitações e manutenção](#limitações-e-manutenção)
- [Índice geral](INDICE.md)

## Finalidade

O notebook [TC3_Visualizacoes_e_Insights.ipynb](../notebooks/TC3_Visualizacoes_e_Insights.ipynb) organiza uma síntese executiva das perguntas norteadoras para avaliação e apresentação. Reúne respostas, gráficos e ressalvas com base nos resultados já calculados pelo pipeline consolidado. Não treina modelos nem refaz a análise completa.

Enquanto a [análise gerencial](ANALISE_GERENCIAL_RANDOM_FOREST.md) calcula probabilidades com o modelo serializado para comparar grupos reais do teste, este notebook apresenta uma narrativa visual de resultados previamente registrados.

## Conteúdo e origem dos resultados

O percurso inclui capacidade preditiva, curva ROC e métricas, SHAP, importância por permutação, infraestrutura, INSE, persistência municipal, finanças, clusters e cobertura das metas.

Há três formas de apresentação dos resultados:

- Valores inseridos nas próprias células e tabelas, resumindo a execução registrada do pipeline.
- Imagens de avaliação e SHAP incorporadas em base64, exibidas sem ler arquivos externos de imagem.
- Análises de infraestrutura e finanças carregadas de `resultados/tabelas/02_infraestrutura_por_faixa_ano.csv` e `resultados/tabelas/07_financas_por_faixa_ano.csv`, respectivamente.

Essa distinção significa que reexecutar o notebook não atualiza automaticamente todos os resultados a partir dos artefatos mais recentes. O notebook apresenta gráficos e tabelas nas saídas das células; não possui chamadas de exportação de figuras com `savefig` e não altera dados, modelos ou resultados externos. Salvar o notebook atualiza o próprio `.ipynb` com saídas e contagens; o Jupyter também pode criar checkpoints.

## Percurso de análise

As visualizações apoiam as perguntas norteadoras do projeto e a comunicação dos resultados consolidados:

- **Desempenho e explicabilidade:** métricas, curva ROC, SHAP e importância por permutação previamente calculados.
- **Infraestrutura e contexto socioeconômico:** comparações por faixa e correlações de INSE, considerando a cobertura e o caráter municipal dos indicadores.
- **Continuidade municipal e finanças:** comparação entre períodos e indicadores financeiros/contextuais, respeitando a granularidade e as transformações das variáveis.
- **Perfis e metas:** síntese dos clusters oficiais e cobertura das metas. A cobertura, isoladamente, não identifica municípios em risco.

A execução localiza os CSVs necessários, prepara os indicadores para apresentação e exibe gráficos e tabelas. As regras de preparação, cálculo e classificação pertencem ao pipeline original; filtros e níveis de agregação distintos não devem ser comparados diretamente.

## Pré-requisitos e execução

Para consultar a narrativa e as saídas salvas, abra o notebook. Para reexecutar, use Jupyter com pandas, NumPy, Matplotlib e IPython disponíveis no kernel. Pathlib e base64 fazem parte da biblioteca padrão do Python. O notebook não depende de seaborn nem lê métricas de arquivos JSON na versão atual. O notebook importa pandas diretamente; confira sua disponibilidade no ambiente escolhido.

Os CSVs de infraestrutura e finanças devem estar presentes e pertencer à mesma execução oficial dos valores fixos e imagens incorporadas. Executar o modular sobre a mesma pasta pode substituí-los por resultados de teste; nesse caso, o notebook poderá misturar referências. Para a apresentação oficial, use os artefatos do consolidado. A célula procura a raiz a partir do diretório atual e de seus ancestrais. Abra o notebook dentro do repositório e execute **Restart Kernel and Run All Cells** para preservar as dependências entre células.

A tabela de infraestrutura utiliza `feature`, `ano_referencia`, `faixa` e `taxa_observada`. O CSV financeiro deve incluir `feature`, `ano_referencia`, `faixa` e `taxa_observada`, além de `registros`, `feature_media` e `probabilidade_media` usados na tabela exibida. As variáveis financeiras esperadas são Bolsa Família, Fundeb, receitas e PIB per capita, com os nomes transformados definidos no código. Se o arquivo estiver ausente, gere-o pelas etapas correspondentes do [pipeline consolidado](../notebooks/TC3_Pipeline_Completo_Alfabetizacao.ipynb).

## Limitações e manutenção

Taxas observadas e probabilidades estimadas são medidas distintas. Importância e SHAP não demonstram causalidade; valores financeiros transformados não devem ser lidos diretamente em reais. A comparação temporal cobre apenas 2023 e 2024, com as restrições territoriais descritas na [documentação das fontes](FONTES_INTEGRACAO_GRANULARIDADE.md).

O gráfico de metas mostra sua cobertura, sem identificar sozinho quais municípios estão em risco. Para essa análise, consulte as estimativas agregadas e os produtos descritos em [metas e perguntas de negócio](METAS_PERGUNTAS_NEGOCIO.md). Os clusters são descritivos e incluem grupo pequeno, exigindo cautela.

Após nova execução oficial, confira os valores inseridos nas células, as imagens incorporadas, os textos e os CSVs de infraestrutura e finanças para manter a mesma referência de resultados. A fonte de verdade permanece o pipeline consolidado; este notebook é uma síntese para comunicação.
