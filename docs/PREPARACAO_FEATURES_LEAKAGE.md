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
notebooks/fase_4_preparacao/TC3_Main_Fluxo_Unificado_Fase4_Preparacao_Baseline_Metas_Chave_Escola.ipynb
```

Enquanto essa estrutura não estiver integrada à `main`, a referência executável permanece `notebooks/TC3_Pipeline_Completo_Alfabetizacao.ipynb`.

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

Separações preservam o teste e usam agrupamento por `chave_escola_ano` quando aplicável. Deve haver zero sobreposição de grupos entre treino e validação. Amostragens usam hash estável e seed 42.

## Artefatos obrigatórios

- base Parquet particionada por UF;
- manifesto com contagens, schema e features;
- catálogo de variáveis;
- decisões de inclusão/exclusão;
- baseline;
- validações de leakage e granularidade.
