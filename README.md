# Tech Challenge - Fase 3

Machine Learning e Inteligencia Analitica para Alfabetizacao no Brasil.

## Contexto

Este projeto faz parte do Tech Challenge da FIAP - Fase 3. O objetivo geral e utilizar dados tratados na camada Gold do projeto anterior para desenvolver analises e modelos supervisionados capazes de apoiar a compreensao da alfabetizacao infantil no Brasil.

O problema central e prever se um aluno sera classificado como alfabetizado ou nao alfabetizado a partir de variaveis educacionais, territoriais e socioeconomicas, produzindo tambem interpretacoes uteis para tomada de decisao em politicas publicas.

## Objetivo analitico

Construir uma solucao de Machine Learning que contemple:

- entendimento e auditoria da base analitica;
- analise exploratoria dos dados;
- selecao e justificativa de features;
- avaliacao de riscos de Data Leakage;
- pipeline de pre-processamento;
- treinamento e validacao de modelos supervisionados;
- avaliacao de metricas e interpretabilidade;
- comunicacao dos principais insights do projeto.

## Organizacao do projeto

A estrutura final proposta para o repositorio e:

```text
tech_challenge_3/
  dados/
    principal/
    complementar/
  notebooks/
    fase_2_entendimento_base_dados/
    fase_3_eda/
    fase_4_preparacao_dados/
    fase_5_modelagem/
    fase_6_otimizacao_avaliacao/
    fase_7_interpretacao_negocio/
    fase_8_visualizacao_resultados/
    fase_9_entrega_apresentacao/
  docs/
    data_dictionary/
    jira/
  requirements.txt
  README.md
```

Durante o desenvolvimento, a equipe pode utilizar identificadores internos para rastreabilidade entre tarefas, branches e artefatos tecnicos. A entrega final, entretanto, deve ser organizada por etapas analiticas do projeto.

As pastas de notebooks seguem as fases planejadas para o projeto, facilitando a relacao entre o cronograma de trabalho e a narrativa tecnica da entrega final.

## Organizacao colaborativa

A estrategia de organizacao interna e rastreabilidade esta documentada em `docs/jira/organizacao_interna.md`.

## Etapas tecnicas

### 1. Auditoria e entendimento da base

Validacao da Feature Table `ml_aluno`, incluindo volume, esquema, tipos, valores nulos, granularidade, target e divisao entre treino, validacao e teste.

### 2. Catalogo de variaveis

Documentacao das variaveis disponiveis na base principal e em fontes complementares, como Censo Escolar 2023 e INSE 2023.

### 3. Selecao de features

Classificacao das variaveis candidatas quanto a inclusao, exclusao, transformacao ou necessidade de investigacao adicional. Essa etapa justifica tecnicamente quais atributos fazem sentido para modelagem.

### 4. Analise de Data Leakage

Revisao das variaveis e do processo de preparacao para identificar informacoes que poderiam revelar direta ou indiretamente o target ou dados indisponiveis no momento da predicao.

### 5. Pre-processamento e modelagem

Construcao de pipeline reprodutivel com imputacao, encoding, transformacoes, treinamento e validacao de modelos supervisionados.

### 6. Avaliacao e interpretabilidade

Avaliacao de desempenho, comparacao de modelos e interpretacao das variaveis mais relevantes por tecnicas como Feature Importance e SHAP Values, quando aplicavel.

## Ambiente

As dependencias principais do projeto estao listadas em `requirements.txt`.

Para preparar o ambiente local:

```powershell
python -m venv .venv
.\.venv\Scripts\activate
python -m pip install -r requirements.txt
```

## Observacoes

- Dados brutos ou arquivos grandes devem ser mantidos fora do versionamento quando apropriado.
- Credenciais, tokens e arquivos sensiveis nao devem ser commitados.
- A entrega final deve priorizar clareza, reproducibilidade e interpretacao dos resultados.
