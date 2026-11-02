# Análise gerencial do Random Forest

## Índice

- [Finalidade](#finalidade)
- [Método e interpretação](#método-e-interpretação)
- [Pré-requisitos e execução](#pré-requisitos-e-execução)
- [Produtos e manutenção](#produtos-e-manutenção)
- [Índice geral](INDICE.md)

## Finalidade

O notebook [TC3_Analise_Gerencial_Random_Forest.ipynb](../notebooks/TC3_Analise_Gerencial_Random_Forest.ipynb) apresenta comparações gerenciais usando registros reais do teste oficial e probabilidades calculadas pelo modelo final serializado. Ele não treina nem ajusta o modelo.

Seu foco é mostrar, para cada grupo, quantidade de registros, proporção observada de alfabetização, probabilidade média estimada e diferença entre os grupos. Complementa a [síntese visual das perguntas norteadoras](VISUALIZACOES_E_INSIGHTS.md), que reúne resultados previamente calculados para apresentação.

## Método e interpretação

As dez comparações abrangem energia, conectividade, água e esgoto, biblioteca, laboratório, quadra, índice agregado de infraestrutura, INSE, contextos de SP e CE e redes de ensino.

Para infraestrutura e INSE, os limites são definidos no desenvolvimento: grupos abaixo do percentil 25 e acima do percentil 75 são comparados no teste. UF e rede utilizam os grupos observados. Esses grupos podem diferir em outras características, portanto os contrastes não representam efeitos de intervenções.

Infraestrutura representa proporções municipais de escolas com recursos, sem confirmar a condição da escola frequentada pelo aluno. A média das probabilidades não é a proporção de classificações positivas obtidas com um limiar. Diferenças em pontos percentuais devem ser lidas conforme a ordem dos grupos indicada nos quadros.

O notebook também consulta importância por permutação e a tabela de sensibilidade com e sem UF. Essas leituras descrevem o comportamento do modelo, sem estabelecer causalidade ou substituir a avaliação oficial.

## Pré-requisitos e execução

São necessários o modelo `modelos/random_forest/modelo_pipeline.joblib`, o manifesto `dados/dados_processados/preparado/manifesto_base_modelagem_com_chave_escola.json`, os Parquets apontados por `padrao_leitura`, as métricas `resultados/metricas/fase_7/resultado_final.json` e as tabelas `importancia_permutacao.csv` e `18_sensibilidade_sigla_uf.csv` em `resultados/tabelas/`.

Use o ambiente compatível com o modelo serializado, conforme o [guia de execução](GUIA_EXECUCAO_REPRODUTIBILIDADE.md). Abra o notebook dentro do projeto e execute **Restart Kernel and Run All Cells**. A preparação procura os artefatos no diretório atual e em seus ancestrais, valida o contrato de features e os parâmetros do modelo e calcula probabilidades para os registros do teste. As células seguintes dependem dessa preparação.

Artefatos ausentes devem ser obtidos pela execução das etapas correspondentes do pipeline consolidado. Não substitua o modelo ou as métricas isoladamente sem conferir sua compatibilidade com o manifesto e a base.

## Produtos e manutenção

Além dos resultados exibidos, são geradas quatro imagens em `resultados/figuras/analise_gerencial/`. Nomes, usos, siglas e regras de sobrescrita estão em [figuras para apresentação](resultados/RESULTADOS_ARTEFATOS_ANALITICOS.md#análise-gerencial-e-figuras-para-apresentação).

Após uma nova execução oficial, regenere a análise com artefatos compatíveis e revise os textos interpretativos. As imagens não atualizam automaticamente slides ou vídeo. A referência para seleção e métricas oficiais continua sendo [TC3_Pipeline_Completo_Alfabetizacao.ipynb](../notebooks/TC3_Pipeline_Completo_Alfabetizacao.ipynb).
