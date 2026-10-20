## Conclusão da entrega analítica

O Random Forest, selecionado antes do acesso ao teste, foi avaliado em **581,591 registros** e obteve **ROC AUC 0.6705** (IC95% **0.6673–0.6737**), **Average Precision 0.6841**, **Balanced Accuracy 0.6196** e **F1 0.6392**. O desempenho é superior ao acaso, porém moderado, e sustenta análises agregadas — não decisões individuais automatizadas.

As variáveis com maior importância preditiva foram **sigla_uf, valor_bolsa_familia__signed_log1p, media_inse, rede, in_laboratorio_informatica**. Elas representam sinais predominantemente territoriais e contextuais; nenhuma delas deve ser interpretada como causa da alfabetização. Na análise de sensibilidade, retirar `sigla_uf` alterou o ROC AUC em **-0.0052** e a Average Precision em **-0.0069**. Isso quantifica dependência preditiva do contexto territorial, não efeito causal da UF.

A persistência municipal entre 2023 e 2024 foi calculada em **5,653 pares município-rede comparáveis**, com correlação de Spearman observada de **0.447**. Essa evidência descreve persistência de curto prazo, não tendência histórica longa.

A análise territorial identificou **3 perfis contextuais municipais** (silhouette **0.241**). Os grupos são descritivos e não representam mecanismos causais.

As estimativas municipais foram comparadas às metas oficiais no mesmo município, rede e publicação. O déficit é definido como meta menos probabilidade média. Categorias de risco e cobertura foram exportadas, incluindo territórios sem correspondência de meta. As metas futuras são cenários condicionais ao contexto observado, não projeções completas até 2030.

O treinamento final levou **1.3 minutos** e a inferência **0.61 segundos**, usando **RAPIDS cuML — NVIDIA GeForce RTX 3050 6GB Laptop GPU (6.0 GB de VRAM)**. O conjunto de teste não foi utilizado para alterar features, algoritmo, hiperparâmetros ou limiar.