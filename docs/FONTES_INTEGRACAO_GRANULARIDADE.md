# Fontes, integração e granularidade

## Índice

- [Fontes utilizadas](#fontes-utilizadas)
- [Regras temporais](#regras-temporais)
- [Granularidade](#granularidade)
- [Chaves de integração](#chaves-de-integração)
- [Cobertura](#cobertura)
- [Índice geral](INDICE.md)

## Fontes utilizadas

| Fonte | Granularidade de origem | Uso |
|---|---|---|
| Feature Table `ml_aluno` | aluno/avaliação | target, chaves e contexto educacional |
| Censo Escolar 2023 | escola | infraestrutura agregada por município |
| INSE 2023 | escola/município | contexto socioeconômico |
| Bolsa Família | município/ano | contexto de transferência de renda |
| Fundeb | município/ano | contexto financeiro educacional |
| Receitas municipais | município/ano | contexto fiscal |
| PIB municipal | município/ano | PIB per capita com defasagem |
| Metas de alfabetização | Brasil, UF e município/ano | comparação posterior à modelagem |

## Regras temporais

- Bolsa Família, Fundeb e receitas: correspondência anual exata em 2023–2024;
- PIB: 2022 para registros de 2023 e 2023 para registros de 2024;
- INSE e Censo Escolar: snapshot contextual de 2023 aplicado aos dois anos;
- metas: referência analítica posterior, nunca feature.

## Granularidade

As fontes complementares não estão disponíveis no nível individual. Indicadores escolares são agregados para o município antes da integração. Portanto, infraestrutura e INSE representam contexto municipal, não a escola frequentada diretamente pelo aluno.

`id_escola` é anonimizado e não permite ligação pública segura com `CO_ENTIDADE`. `chave_escola_ano` existe para rastreabilidade e validação agrupada, mas não é feature.

## Chaves de integração

- código do município normalizado;
- ano de referência;
- rede de ensino quando aplicável;
- sigla da UF como controle territorial.

Toda integração deve preservar contagens, cobertura e indicadores de ausência. Duplicidades na dimensão complementar precisam ser resolvidas antes do join para evitar multiplicação de alunos.

## Cobertura

São Paulo aparece apenas em 2024 na base principal. Existem municípios sem correspondência de meta municipal; eles devem permanecer identificados, sem imputação silenciosa de metas estaduais ou nacionais.
