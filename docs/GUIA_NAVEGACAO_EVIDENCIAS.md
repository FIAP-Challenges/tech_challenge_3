# Guia de navegação e evidências

## Índice

- [Finalidade](#finalidade)
- [Percurso recomendado de avaliação](#percurso-recomendado-de-avaliação)
- [Mapa de evidências](#mapa-de-evidências)
- [Referência executável](#referência-executável)
- [Rastreabilidade dos notebooks](#rastreabilidade-dos-notebooks)
- [Índice geral](INDICE.md)

## Finalidade

Este guia organiza as principais evidências metodológicas, executáveis e documentais do Tech Challenge 3. Seu objetivo é facilitar a navegação pelo projeto e relacionar cada eixo da solução aos respectivos notebooks, resultados e documentos de aprofundamento.

## Percurso recomendado de avaliação

1. Começar pelo [README principal](../README.md), que resume problema, dados, método, resultados e execução.
2. Consultar o [pipeline consolidado](../notebooks/TC3_Pipeline_Completo_Alfabetizacao.ipynb) para reprodução integral e resultados oficiais.
3. Usar os notebooks modulares disponíveis para examinar em detalhe as decisões de cada etapa.
4. Consultar os documentos temáticos abaixo para verificar contratos metodológicos, justificativas e limitações.

## Mapa de evidências

| Eixo da solução | Síntese da evidência | Documentação detalhada |
|---|---|---|
| problema e objetivo | definição da população, target, objetivo preditivo e limites de uso | [Problema, objetivos e escopo](PROBLEMA_OBJETIVOS_ESCOPO.md) |
| fontes e integração | origem dos dados, chaves, granularidade, temporalidade e cobertura | [Fontes, integração e granularidade](FONTES_INTEGRACAO_GRANULARIDADE.md) e [Aquisição e linhagem](AQUISICAO_LINHAGEM_FONTES.md) |
| entendimento da base | auditoria da feature table, catálogo de variáveis, seleção inicial e análise de leakage | [notebooks da fase 2](../notebooks/fase_2_entendimento_base_dados/) e [Preparação, features e leakage](PREPARACAO_FEATURES_LEAKAGE.md) |
| análise exploratória | distribuição do target e das features, nulos, outliers, relações territoriais e temporais | [notebooks da fase 3](../notebooks/fase_3_analise_exploratória_de_dados/) e [EDA e qualidade](EDA_QUALIDADE_DADOS.md) |
| preparação e prevenção de leakage | contrato das 18 features, exclusões, imputação, encoding e separação dos conjuntos | [Preparação, features e leakage](PREPARACAO_FEATURES_LEAKAGE.md) |
| modelagem inicial | baseline e comparação das famílias de modelos | [Modelagem inicial](MODELAGEM_INICIAL.md) |
| otimização e seleção | validação, busca de hiperparâmetros e escolha do Random Forest | [Otimização e validação](OTIMIZACAO_VALIDACAO.md) |
| avaliação final | teste independente, métricas congeladas e análise de sensibilidade | [Avaliação e interpretabilidade](AVALIACAO_INTERPRETABILIDADE.md) |
| interpretabilidade | importância por permutação, SHAP e leitura não causal | [Avaliação e interpretabilidade](AVALIACAO_INTERPRETABILIDADE.md) |
| aplicação ao negócio | metas, perguntas analíticas e regras de resposta | [Metas e perguntas de negócio](METAS_PERGUNTAS_NEGOCIO.md) |
| responsabilidade | limitações, riscos, restrições de uso e cuidados éticos | [Limitações e ética](LIMITACOES_ETICA.md) |
| reprodução | ambientes CPU e GPU, Docker, hardware, validação, parada e reconstrução | [Guia de execução e reprodutibilidade](GUIA_EXECUCAO_REPRODUTIBILIDADE.md) |

## Referência executável

O arquivo [TC3_Pipeline_Completo_Alfabetizacao.ipynb](../notebooks/TC3_Pipeline_Completo_Alfabetizacao.ipynb) é a fonte de verdade para a execução integral, as métricas finais e os artefatos oficiais. Ele foi mantido para permitir o processamento sequencial sem intervenção entre etapas, inclusive durante execuções noturnas.

## Rastreabilidade dos notebooks

Os notebooks modulares são a forma recomendada de compreender e revisar o trabalho por responsabilidade analítica. O consolidado não possui uma chave de tarefa exclusiva porque reúne atividades associadas a várias chaves do projeto. A decisão e sua justificativa estão documentadas em [Organização interna e rastreabilidade no Jira](jira/ORGANIZACAO_INTERNA.md#notebook-consolidado-e-chave-do-projeto).
