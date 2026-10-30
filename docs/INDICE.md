# Índice da documentação técnica

## Índice

- [Documentos principais](#documentos-principais)
- [Execução](#execução)
- [Complementos](#complementos)
- [Documentação das pastas](#documentação-das-pastas)
- [Referências executáveis](#referências-executáveis)
- [Página inicial do projeto](../README.md)

Esta pasta reúne a narrativa acadêmica, os contratos metodológicos e os procedimentos operacionais do Tech Challenge 3.

## Documentos principais

| Documento | Conteúdo |
|---|---|
| [Problema, objetivos e escopo](PROBLEMA_OBJETIVOS_ESCOPO.md) | problema, população, target, objetivos e limites |
| [Fontes, integração e granularidade](FONTES_INTEGRACAO_GRANULARIDADE.md) | fontes, chaves, regras temporais e cobertura |
| [EDA e qualidade](EDA_QUALIDADE_DADOS.md) | análises exploratórias e controles de qualidade |
| [Preparação, features e leakage](PREPARACAO_FEATURES_LEAKAGE.md) | contrato das 18 features, exclusões e splits |
| [Modelagem inicial](MODELAGEM_INICIAL.md) | baseline e comparação das famílias de modelos |
| [Otimização e validação](OTIMIZACAO_VALIDACAO.md) | finalistas, protocolo e seleção do Random Forest |
| [Avaliação e interpretabilidade](AVALIACAO_INTERPRETABILIDADE.md) | teste independente, métricas e explicabilidade |
| [Metas e negócio](METAS_PERGUNTAS_NEGOCIO.md) | metas oficiais e regras de resposta |
| [Limitações e ética](LIMITACOES_ETICA.md) | riscos, restrições e uso responsável |
| [Aquisição e linhagem](AQUISICAO_LINHAGEM_FONTES.md) | camadas, fontes, integridade e proveniência |

## Execução

- [Guia de execução e reprodutibilidade](GUIA_EXECUCAO_REPRODUTIBILIDADE.md) — CPU, GPU, Docker, hardware, ordem dos notebooks, parada e reconstrução separadas.

## Complementos

- [Guia de navegação e evidências](GUIA_NAVEGACAO_EVIDENCIAS.md)
- [Catálogo de variáveis da `ml_aluno`](dados/CATALOGO_VARIAVEIS_ML_ALUNO.md)
- [Dicionário das bases complementares](dados/DICIONARIO_BASES_COMPLEMENTARES.md)
- [Organização interna e rastreabilidade no Jira](jira/ORGANIZACAO_INTERNA.md)

## Documentação das pastas

- [Organização e integridade das fontes originais](AQUISICAO_LINHAGEM_FONTES.md#organização-das-fontes-originais)
- [Resultados e artefatos analíticos](resultados/RESULTADOS_ARTEFATOS_ANALITICOS.md)

## Referências executáveis

- consolidado: `notebooks/TC3_Pipeline_Completo_Alfabetizacao.ipynb`;
- modular: notebooks organizados por fase metodológica para análise detalhada;
- resultados oficiais: `resultados/`;
- ambiente e status: `resultados/relatorios/`.
