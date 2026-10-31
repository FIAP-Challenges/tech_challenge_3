# Análise exploratória e qualidade dos dados

## Índice

- [Objetivos da EDA](#objetivos-da-eda)
- [Fluxo modular](#fluxo-modular)
- [Controles de qualidade](#controles-de-qualidade)
- [Restrições interpretativas](#restrições-interpretativas)
- [Evidência e artefatos](#evidência-e-artefatos)
- [Índice geral](INDICE.md)

## Objetivos da EDA

- compreender distribuição e balanceamento do target;
- verificar nulos, duplicidades e outliers;
- comparar município, UF, rede, série e ano;
- avaliar relações entre variáveis;
- identificar restrições temporais e de cobertura;
- orientar transformações sem consultar o teste.

## Fluxo modular

| Notebook | Análise |
|---|---|
| TC3-43 | distribuição do target |
| TC3-44 | distribuição das features |
| TC3-45 | nulos, duplicidades e outliers |
| TC3-46 | relações entre variáveis |
| TC3-47 | diferenças por município, UF, rede e série |
| TC3-48 | relações temporais |

## Controles de qualidade

- schema e tipos coerentes;
- target restrito a valores válidos;
- chaves de controle presentes;
- partições Hive lidas preservando `sigla_uf`;
- contagens antes e depois dos joins;
- cobertura complementar explicitada;
- valores financeiros transformados somente após auditoria;
- resultados separados por ano quando a cobertura não é comparável.

## Restrições interpretativas

Existem somente dois anos, portanto não há série histórica longa. São Paulo não deve ser usado em comparações 2023–2024. INSE e Censo são snapshots de 2023; sua repetição em 2024 não representa evolução temporal.

Outliers financeiros podem refletir porte municipal. Transformações logarítmicas reduzem assimetria, mas não convertem valores totais em investimento por aluno.

## Evidência e artefatos

Tabelas ficam em `resultados/tabelas/` e figuras em `resultados/figuras/`. Todo gráfico final deve informar universo, período, unidade, tratamento de ausências e limitação relevante.
