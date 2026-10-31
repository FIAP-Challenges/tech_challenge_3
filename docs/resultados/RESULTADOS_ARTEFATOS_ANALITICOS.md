# Resultados e artefatos analíticos

## Índice

- [Organização dos resultados](#organização-dos-resultados)
- [Síntese analítica](#síntese-analítica)
- [Análise final](#análise-final)
- [Métricas](#métricas)
- [Tabelas](#tabelas)
- [Figuras](#figuras)
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

## Relatórios de execução

Os relatórios reúnem conclusões, ambiente, auditorias e estado do fluxo. Os principais registros são:

- `ambiente_execucao.json`: versões, backend, seed, modelo e configuração;
- `status_execucao.json`: conclusão, modelo oficial, métrica e artefatos validados;
- conclusão dinâmica: síntese derivada das métricas e análises finais, incorporada neste documento.

Esses arquivos constituem evidência operacional da execução e devem ser interpretados em conjunto com o [guia de execução e reprodutibilidade](../GUIA_EXECUCAO_REPRODUTIBILIDADE.md).
