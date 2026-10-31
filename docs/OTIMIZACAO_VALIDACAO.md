# Otimização, validação e seleção

## Índice

- [Finalistas](#finalistas)
- [Protocolo](#protocolo)
- [Resultado de validação](#resultado-de-validação)
- [Congelamento](#congelamento)
- [Artefato oficial](#artefato-oficial)
- [Saídas](#saídas)
- [Índice geral](INDICE.md)

## Finalistas

Foram otimizados sob protocolo comum:

- Regressão Logística — TC3-60;
- Random Forest — TC3-61;
- Gradient Boosting — TC3-62.

TC3-63 consolida a comparação e registra a seleção antes do acesso ao teste.

## Protocolo

- seed 42;
- amostra e features equivalentes;
- validação cruzada agrupada;
- teste completamente isolado;
- orçamento de busca comparável;
- métricas e gaps de generalização registrados.

## Resultado de validação

| Modelo | ROC AUC | Average Precision | Balanced Accuracy | F1 |
|---|---:|---:|---:|---:|
| Random Forest | 0,65646 | 0,66565 | 0,61082 | 0,63460 |
| Gradient Boosting | 0,65578 | 0,66546 | 0,61036 | 0,62493 |
| Regressão Logística | 0,59168 | 0,59902 | 0,56047 | 0,57453 |

Random Forest e Gradient Boosting ficaram em empate técnico pelo critério estabelecido. O Random Forest foi selecionado por validação cruzada agrupada, menor gap treino–validação, F1 ligeiramente superior e decisão registrada antes do teste.

## Congelamento

Depois da seleção, algoritmo, features, hiperparâmetros e protocolo devem permanecer congelados. O teste não pode ser usado para retornar ao tuning.

## Artefato oficial

O modelo oficial é o Random Forest selecionado antes do acesso ao teste. O pipeline e o modelo serializados em `modelos/random_forest/` são produtos regeneráveis: sua referência metodológica permanece o notebook consolidado, juntamente com as fontes, configurações e versões registradas na execução.

## Saídas

Resultados ficam em `dados/modelagem/fase_6_resultados/` e `resultados/metricas/fase_6/`.
