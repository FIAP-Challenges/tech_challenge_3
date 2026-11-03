# Problema, objetivos e escopo

## Índice

- [Problema](#problema)
- [Unidade de análise](#unidade-de-análise)
- [Objetivos técnicos](#objetivos-técnicos)
- [Critérios de sucesso](#critérios-de-sucesso)
- [Fora do escopo](#fora-do-escopo)
- [Índice geral](INDICE.md)

## Problema

O projeto estima a probabilidade de um aluno das redes estadual ou municipal ser classificado como alfabetizado a partir de variáveis territoriais, administrativas, socioeconômicas, financeiras e de infraestrutura.

O objetivo é produzir capacidade preditiva e evidências agregadas úteis para análise educacional. O modelo não estabelece causalidade e não deve ser usado para decisões individuais automatizadas.

## Unidade de análise

- unidade preditiva: registro de aluno;
- target: `alfabetizado`, binário;
- população: redes estadual e municipal;
- período principal: 2023 e 2024;
- agregações analíticas: município, UF, rede e ano.

A rede privada foi excluída por cobertura insuficiente. As variáveis explicativas são predominantemente contextuais e municipais, não características individuais anteriores à avaliação.

## Objetivos técnicos

1. auditar e integrar as fontes;
2. prevenir data leakage;
3. construir uma base de modelagem rastreável;
4. comparar modelos supervisionados sob o mesmo contrato;
5. selecionar o modelo sem consultar o teste;
6. avaliar generalização, calibração e estabilidade;
7. interpretar associações sem atribuir causalidade;
8. relacionar resultados agregados às metas oficiais.

## Critérios de sucesso

- splits e grupos sem sobreposição indevida;
- teste reservado para avaliação final;
- baseline explícito;
- métricas ROC AUC, Average Precision, Balanced Accuracy e F1;
- ambiente, seed, versões e backend registrados;
- artefatos e conclusões reproduzíveis.

## Fora do escopo

- inferência causal;
- identificação da escola real a partir de identificadores anonimizados;
- previsão temporal completa até 2030;
- decisão automática sobre alunos, escolas ou municípios.
