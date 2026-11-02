# Preparação, features e prevenção de leakage

## Índice

- [Notebook modular](#notebook-modular)
- [Features finais](#features-finais)
- [Exclusões por leakage](#exclusões-por-leakage)
- [Pipeline](#pipeline)
- [Splits e grupos](#splits-e-grupos)
- [Artefatos obrigatórios](#artefatos-obrigatórios)
- [Índice geral](INDICE.md)

## Notebook modular

A preparação consolidada do fluxo particionado é apresentada em:

```text
notebooks/fase_4_preparacao/TC3-49_Fluxo_Unificado_Preparacao.ipynb
```

O notebook modular está integrado à `main`. A referência oficial para execução integral permanece `notebooks/TC3_Pipeline_Completo_Alfabetizacao.ipynb`.

## Features finais

O contrato utiliza 18 features não constantes:

- `sigla_uf`, `rede`, `ano_referencia`;
- valores transformados de Bolsa Família, Fundeb, receitas e PIB per capita;
- `media_inse`;
- oito proporções municipais de infraestrutura;
- indicadores de ausência de cobertura financeira e INSE.

## Exclusões por leakage

Não entram como features:

- `proficiencia`;
- `presenca`;
- `preenchimento_caderno`;
- `caderno` e variáveis derivadas da própria avaliação;
- target ou transformações do target;
- metas oficiais;
- `id_escola`, `id_aluno` e `chave_escola_ano`.

## Pipeline

Imputação, encoding e demais transformações são ajustados apenas no treino e reaplicados à validação e ao teste. Colunas categóricas desconhecidas devem ser tratadas sem reajustar o pipeline.

## Splits e grupos

O `dataset_split` herdado da base principal separa treino, validação e teste por aluno. A preparação preserva esse split e diagnostica a sobreposição de `chave_escola_ano`; não reconstrói o teste como um conjunto de escolas inéditas. Portanto, a ausência de sobreposição escolar não pode ser atribuída ao split oficial como um todo.

Nas etapas de otimização, a separação de desenvolvimento usa `GroupShuffleSplit` e a validação cruzada usa `StratifiedGroupKFold`, com agrupamento por `chave_escola_ano`. Nesses conjuntos agrupados deve haver zero sobreposição de grupos entre treino e validação. Essa chave é anual e anonimizada, sem garantir isolamento da mesma escola real entre anos. Amostragens usam hash estável e seed 42.

## Artefatos obrigatórios

- base Parquet particionada por UF;
- manifesto com contagens, schema e features;
- catálogo de variáveis;
- decisões de inclusão/exclusão;
- baseline;
- validações de leakage e granularidade.
