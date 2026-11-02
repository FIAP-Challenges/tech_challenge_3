# Visualizações e insights

## Índice

- [Finalidade](#finalidade)
- [Conteúdo e origem dos resultados](#conteúdo-e-origem-dos-resultados)
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
- Análise financeira carregada de `resultados/tabelas/07_financas_por_faixa_ano.csv`.

Essa distinção significa que reexecutar o notebook não atualiza automaticamente todos os resultados a partir dos artefatos mais recentes. O notebook apresenta gráficos e tabelas nas saídas das células; não possui chamadas de exportação de figuras com `savefig`.

## Pré-requisitos e execução

Para consultar a narrativa e as saídas salvas, abra o notebook. Para reexecutar, use Jupyter com pandas, Matplotlib e IPython disponíveis no kernel. O notebook importa pandas diretamente; confira sua disponibilidade no ambiente escolhido.

O CSV financeiro deve estar presente. A célula procura a raiz a partir do diretório atual e de seus ancestrais. Abra o notebook dentro do repositório e execute **Restart Kernel and Run All Cells** para preservar as dependências entre células.

O CSV deve incluir `feature`, `ano_referencia`, `faixa` e `taxa_observada`, além de `registros`, `feature_media` e `probabilidade_media` usados na tabela exibida. As variáveis financeiras esperadas são Bolsa Família, Fundeb, receitas e PIB per capita, com os nomes transformados definidos no código. Se o arquivo estiver ausente, gere-o pelas etapas correspondentes do [pipeline consolidado](../notebooks/TC3_Pipeline_Completo_Alfabetizacao.ipynb).

## Limitações e manutenção

Taxas observadas e probabilidades estimadas são medidas distintas. Importância e SHAP não demonstram causalidade; valores financeiros transformados não devem ser lidos diretamente em reais. A comparação temporal cobre apenas 2023 e 2024, com as restrições territoriais descritas na [documentação das fontes](FONTES_INTEGRACAO_GRANULARIDADE.md).

O gráfico de metas mostra sua cobertura, sem identificar sozinho quais municípios estão em risco. Para essa análise, consulte as estimativas agregadas e os produtos descritos em [metas e perguntas de negócio](METAS_PERGUNTAS_NEGOCIO.md). Os clusters são descritivos e incluem grupo pequeno, exigindo cautela.

Após nova execução oficial, confira os valores inseridos nas células, as imagens incorporadas, os textos e o CSV financeiro para manter a mesma referência de resultados. A fonte de verdade permanece o pipeline consolidado; este notebook é uma síntese para comunicação.
