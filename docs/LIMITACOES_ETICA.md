# Limitações, ética e uso responsável

## Índice

- [Limitações dos dados](#limitações-dos-dados)
- [Limitações do modelo](#limitações-do-modelo)
- [Riscos](#riscos)
- [Uso responsável](#uso-responsável)
- [Comunicação](#comunicação)
- [Índice geral](INDICE.md)

## Limitações dos dados

- preditores predominantemente contextuais e municipais, que não sustentam inferências ou diagnósticos individuais;
- infraestrutura agregada, não vinculada à escola frequentada;
- INSE e Censo como snapshots de 2023;
- somente dois anos de observação;
- São Paulo presente apenas em 2024;
- identificador escolar anonimizado;
- valores financeiros influenciados pelo porte do município;
- cobertura incompleta de metas municipais.

## Limitações do modelo

O desempenho observado é moderado (ROC AUC 0,6705), adequado para análises agregadas e exploratórias, mas insuficiente para classificação individual ou decisão automatizada. As probabilidades podem refletir desigualdades territoriais já presentes nos dados. Importância de feature e SHAP explicam o comportamento preditivo do modelo, não causas sociais ou pedagógicas.

## Riscos

- estigmatização de territórios;
- uso punitivo de rankings;
- interpretação causal indevida;
- decisão automatizada sobre alunos ou escolas;
- ocultação de incerteza e ausência de cobertura;
- reidentificação por cruzamento indevido de dados.

## Uso responsável

- apresentar resultados agregados;
- manter ressalvas de cobertura e incerteza;
- revisar métricas por UF, rede e ano;
- envolver especialistas educacionais;
- usar o modelo como apoio analítico, nunca como único critério;
- proteger identificadores e não tentar reidentificar escolas ou alunos.

## Comunicação

Resultados devem ser descritos como associação e capacidade preditiva. Recomendações de política pública exigem validação adicional, dados mais granulares e, para causalidade, desenho longitudinal ou quase experimental.
