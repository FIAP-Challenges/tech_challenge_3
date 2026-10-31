# Avaliação final e interpretabilidade

## Índice

- [Referência modular](#referência-modular)
- [Ambiente validado](#ambiente-validado)
- [Resultado no teste independente](#resultado-no-teste-independente)
- [Interpretabilidade](#interpretabilidade)
- [Artefatos](#artefatos)
- [Índice geral](INDICE.md)

## Referência modular

```text
notebooks/fase_7_avaliacao_independente/Modelo_Final_Random_Forest.ipynb
```

Na base `origin/main`, o mesmo fluxo está incorporado ao notebook consolidado até que o particionamento seja integrado.

## Ambiente validado

- Python 3.12.11;
- scikit-learn 1.7.2;
- Polars 2.0.0;
- RAPIDS cuML;
- NVIDIA GeForce RTX 3050 Laptop com 6 GB de VRAM;
- seed 42;
- SHAP executado em 100 observações.

## Resultado no teste independente

| Métrica | Valor |
|---|---:|
| ROC AUC | 0,67048 |
| Average Precision | 0,68410 |
| Balanced Accuracy | 0,61962 |
| F1 | 0,63919 |

O teste contém 581.591 registros. O desempenho é moderado e adequado para análise agregada, não para decisões individuais automatizadas.

Uma segunda execução apresentou pequenas diferenças numéricas, sem alterar a seleção do modelo, a ordem de grandeza das métricas ou as conclusões analíticas. Esse comportamento é compatível com as tolerâncias documentadas na [comparação entre execuções](GUIA_EXECUCAO_REPRODUTIBILIDADE.md#14-comparação-e-equivalência-entre-execuções). Os valores da tabela acima, provenientes da execução consolidada validada, permanecem como resultados oficiais.

## Interpretabilidade

Importância por permutação, SHAP e análise de sensibilidade ajudam a descrever o comportamento do modelo. As variáveis mais relevantes são sinais preditivos contextuais; não demonstram causa.

A sensibilidade com e sem `sigla_uf` mede dependência territorial. Pequenas mudanças de métrica não autorizam interpretação causal da UF.

## Artefatos

- pipeline/modelo serializado;
- métricas finais em JSON;
- previsões agregadas por município;
- métricas por UF, rede e ano;
- importância por permutação;
- figuras de curvas, calibração e interpretação;
- relatório do ambiente e status da execução.
