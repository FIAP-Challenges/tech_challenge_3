# Resultados e artefatos analíticos

## Índice

- [Organização dos resultados](#organização-dos-resultados)
- [Síntese analítica](#síntese-analítica)
- [Análise final](#análise-final)
- [Métricas](#métricas)
- [Tabelas](#tabelas)
- [Figuras](#figuras)
- [Análise gerencial e figuras para apresentação](#análise-gerencial-e-figuras-para-apresentação)
- [Relatórios de execução](#relatórios-de-execução)
- [Índice geral](../INDICE.md)

## Organização dos resultados

O diretório `resultados/` reúne as evidências produzidas pelo pipeline consolidado. Métricas, tabelas, figuras e relatórios devem permanecer vinculados à execução que os gerou, com estágio, período, população, backend e limitações identificados. Os valores oficiais são os registrados pelo notebook `notebooks/TC3_Pipeline_Completo_Alfabetizacao.ipynb`.

## Síntese analítica

O Random Forest, selecionado antes do acesso ao teste, foi avaliado em **581.591 registros** e obteve **ROC AUC 0,6705** (IC95% **0,6673–0,6737**), **Average Precision 0,6841**, **Balanced Accuracy 0,6196** e **F1 0,6392**. O desempenho é superior ao acaso, porém moderado, e sustenta análises agregadas — não decisões individuais automatizadas.

As variáveis com maior importância preditiva foram **sigla_uf, valor_bolsa_familia__signed_log1p, media_inse, rede, in_laboratorio_informatica**. Elas representam sinais predominantemente territoriais e contextuais; nenhuma delas deve ser interpretada como causa da alfabetização. Na análise de sensibilidade, retirar `sigla_uf` alterou o ROC AUC em **-0,0052** e a Average Precision em **-0,0069**. Isso quantifica dependência preditiva do contexto territorial, não efeito causal da UF.

A persistência municipal entre 2023 e 2024 foi calculada em **5.653 pares município-rede comparáveis**, com correlação de Spearman observada de **0,447**. Essa evidência descreve persistência de curto prazo, não tendência histórica longa. A análise territorial identificou **3 perfis contextuais municipais** (silhouette **0,241**); os grupos são descritivos e não representam mecanismos causais.

As estimativas municipais foram comparadas às metas oficiais no mesmo município, rede e publicação. O déficit é definido como meta menos probabilidade média. Categorias de risco e cobertura foram exportadas, incluindo territórios sem correspondência de meta. As metas futuras são cenários condicionais ao contexto observado, não projeções completas até 2030.

O treinamento final levou **1,3 minuto** e a inferência **0,61 segundo**, usando **RAPIDS cuML — NVIDIA GeForce RTX 3050 6GB Laptop GPU (6,0 GB de VRAM)**. O conjunto de teste não foi utilizado para alterar features, algoritmo, hiperparâmetros ou limiar.

## Análise final

Os resultados confirmam que as fontes integradas contêm sinal preditivo para distinguir os casos de alfabetização acima do acaso. Ao mesmo tempo, a magnitude das métricas mostra que esse sinal é parcial: o modelo não captura sozinho a complexidade do processo educacional. A principal contribuição da solução é, portanto, oferecer uma leitura quantitativa e reproduzível para análises agregadas, e não substituir avaliações pedagógicas ou produzir diagnósticos individuais.

A predominância de variáveis territoriais e contextuais indica que parte relevante da capacidade preditiva está associada a diferenças estruturais entre localidades, redes e condições socioeconômicas. A sensibilidade limitada à retirada de `sigla_uf` mostra que o desempenho não depende exclusivamente dessa variável, mas sua importância reforça a necessidade de interpretar o resultado como associação contextual. Nenhuma importância de feature, valor SHAP ou diferença entre grupos estabelece causalidade.

As análises municipais acrescentam uma dimensão prática ao modelo ao permitir comparar probabilidades agregadas, persistência de curto prazo, perfis contextuais e distância em relação às metas oficiais. Esses produtos podem apoiar investigação, priorização exploratória e formulação de novas perguntas. Não devem ser usados como ranking punitivo, projeção garantida de cumprimento das metas ou justificativa isolada para direcionar recursos.

Em conjunto, o projeto demonstra um fluxo tecnicamente viável, rastreável e reprodutível, com prevenção explícita de leakage, seleção anterior ao teste e avaliação independente. O Random Forest é adequado como referência analítica para o escopo estudado, desde que seus resultados sejam acompanhados das ressalvas de cobertura, temporalidade, incerteza e ausência de interpretação causal. Estudos futuros podem ampliar a série histórica, melhorar a granularidade das fontes e realizar validação externa antes de qualquer uso operacional.

## Métricas

Os arquivos de métricas registram baseline, comparação inicial, otimização, validação e avaliação independente. Resultados de validação não devem ser confundidos com o teste independente. Backend, seed, amostra, estágio e identificação da execução devem acompanhar cada artefato. A interpretação detalhada está em [Avaliação e interpretabilidade](../AVALIACAO_INTERPRETABILIDADE.md).

## Tabelas

As tabelas finais incluem dicionários gerados, respostas quantitativas, análises territoriais e comparações com metas. Cada tabela deve conservar grão, período, fonte e definição das colunas. Ausência de cobertura não deve ser convertida silenciosamente em zero.

## Figuras

As figuras apresentam resultados do pipeline oficial e das análises territoriais. Cada visualização deve informar universo, período, unidade, tratamento de ausências e limitação interpretativa relevante. Gráficos descritivos, importâncias e agrupamentos não devem ser apresentados como evidência causal.

## Análise gerencial e figuras para apresentação

A documentação própria de [Análise Gerencial do Random Forest](../ANALISE_GERENCIAL_RANDOM_FOREST.md) descreve método, entradas e execução do notebook. A [documentação de Visualizações e Insights](../VISUALIZACOES_E_INSIGHTS.md) explica o outro notebook de comunicação, voltado à síntese das perguntas norteadoras. Esta seção detalha os arquivos de figuras gerenciais.

O [notebook de análise gerencial](../../notebooks/TC3_Analise_Gerencial_Random_Forest.ipynb) complementa o pipeline oficial com comparações entre grupos reais do teste. Ele carrega o modelo final e seus artefatos, sem realizar treinamento ou ajuste. As comparações são descritivas e preditivas, sem interpretação causal.

Para reproduzir as figuras:

1. Disponibilize os produtos do pipeline consolidado: `modelos/random_forest/modelo_pipeline.joblib`, `dados/dados_processados/preparado/manifesto_base_modelagem_com_chave_escola.json`, os Parquets indicados pelo campo `padrao_leitura` desse manifesto, `resultados/metricas/fase_7/resultado_final.json` e as tabelas `resultados/tabelas/importancia_permutacao.csv` e `resultados/tabelas/18_sensibilidade_sigla_uf.csv`.
2. Use um ambiente compatível com o modelo serializado e suas versões registradas; consulte o [guia de execução](../GUIA_EXECUCAO_REPRODUTIBILIDADE.md).
3. Abra o notebook gerencial a partir do projeto e execute **Restart Kernel and Run All Cells**. As células de gráficos dependem dos resultados das células anteriores.

As quatro imagens são gravadas em `resultados/figuras/analise_gerencial/`; uma nova execução substitui os arquivos de mesmo nome.

| Arquivo | Conteúdo e uso |
|---|---|
| `observado_vs_estimado_random_forest.png` | diferenças observadas e estimadas entre grupos; a comparação SP–CE fica fora deste gráfico |
| `robustez_modelo_com_sem_uf.png` | comparação de AUC e Average Precision dos modelos com e sem UF, a partir da tabela de sensibilidade |
| `painel_executivo_comparacoes_random_forest.png` | painel 16:9 com comparações e leituras para apresentação |
| `quadro_compacto_powerpoint_random_forest.png` | quadro compacto para inserir no layout dos slides |

Nos quadros, **Reg.** é a quantidade de registros, **Prev.** é a média das probabilidades do modelo e **Obs.** é a proporção observada de alfabetização no grupo. **pp** significa pontos percentuais; a variação estimada representa o grupo B menos o grupo A. Os indicadores de infraestrutura descrevem proporções municipais de escolas, sem confirmar o recurso na escola frequentada por cada aluno.

Os [slides em PowerPoint](../apresentacao/apresentacao.pptx) e o vídeo da apresentação executiva ([MP4 local](../apresentacao/apresentacao.mp4) e [YouTube](https://youtu.be/IDaZaM82j6s)) são materiais de comunicação. O notebook gera as imagens, mas não atualiza automaticamente os slides ou o vídeo.

## Relatórios de execução

Os relatórios reúnem conclusões, ambiente, auditorias e estado do fluxo. Os principais registros são:

- `ambiente_execucao.json`: versões, backend, seed, modelo e configuração;
- `status_execucao.json`: conclusão, modelo oficial, métrica e artefatos validados;
- conclusão dinâmica: síntese derivada das métricas e análises finais, incorporada neste documento.

Esses arquivos constituem evidência operacional da execução e devem ser interpretados em conjunto com o [guia de execução e reprodutibilidade](../GUIA_EXECUCAO_REPRODUTIBILIDADE.md).
