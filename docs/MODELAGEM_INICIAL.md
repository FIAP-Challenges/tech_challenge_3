# Modelagem inicial

## Índice

- [Objetivo](#objetivo)
- [Ordem modular](#ordem-modular)
- [Baseline](#baseline)
- [Protocolo](#protocolo)
- [Interpretação](#interpretação)
- [Saídas](#saídas)
- [Índice geral](INDICE.md)

## Objetivo

Comparar famílias de modelos sob o mesmo contrato de dados, métricas, seed e splits antes da otimização.

## Ordem modular

1. TC3-52 — baseline;
2. TC3-53 — Regressão Logística;
3. TC3-54 — KNN;
4. TC3-55 — SVM linear;
5. TC3-56 — Árvore de Decisão;
6. TC3-57 — Random Forest;
7. TC3-58 — Gradient Boosting;
8. TC3-59 — consolidação dos resultados.

## Baseline

O baseline Dummy estabelece a referência mínima. Um modelo só agrega valor preditivo quando supera essa referência de forma consistente, sem leakage e sob o mesmo conjunto de avaliação.

## Protocolo

- mesmo conjunto de features;
- amostragem determinística quando necessária;
- pipeline ajustado somente com treino;
- métricas ROC AUC, Average Precision, Balanced Accuracy e F1;
- tempo de treino e inferência registrados;
- comparação de treino e validação para diagnosticar overfitting.

## Interpretação

Resultados dessa fase são experimentais. Eles selecionam candidatos à otimização, não definem o modelo final. Diferenças de uma execução modular isolada não substituem as decisões congeladas no pipeline consolidado.

## Saídas

JSONs e tabelas comparativas ficam em `dados/modelagem/resultados/` e `resultados/metricas/fase_5/`, conforme o fluxo executado.
