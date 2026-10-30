# Aquisição e linhagem das fontes

## Índice

- [Princípio](#princípio)
- [Camadas](#camadas)
- [Organização das fontes originais](#organização-das-fontes-originais)
- [Fontes](#fontes)
- [Aquisição](#aquisição)
- [Integridade](#integridade)
- [Regras](#regras)
- [Índice geral](INDICE.md)

## Princípio

Toda fonte deve ter origem, período, granularidade, método de obtenção, checksum quando aplicável e transformação registrados. Fontes originais permanecem imutáveis; produtos derivados são gravados em camadas separadas.

## Camadas

| Camada | Conteúdo |
|---|---|
| `dados/fontes_originais/` | entradas preservadas sem transformação |
| `dados/dados_processados/` | extrações, consolidações, partições e manifests |
| `dados/dados_analiticos/` | previsões e produtos destinados às análises |
| `resultados/` | métricas, tabelas, figuras e relatórios finais |
| `modelos/` | pipelines e modelos serializados |

## Organização das fontes originais

As entradas preservadas em `dados/fontes_originais/` são organizadas nas subpastas `principal/`, `complementar/` e `origem_publica/`, de acordo com sua procedência no projeto. Esses arquivos não devem receber transformações nem ser substituídos por produtos derivados.

Para cada fonte, registre procedência, data de aquisição, período, licença, tamanho e checksum SHA-256. Credenciais, tokens e outros dados de acesso não devem acompanhar os arquivos. Bases consolidadas, recortes, conversões de formato e demais produtos regeneráveis pertencem às camadas de processamento descritas acima.

## Fontes

- Feature Table Gold `ml_aluno` herdada da etapa anterior;
- Censo Escolar 2023;
- INSE 2023;
- Bolsa Família 2023–2024;
- Fundeb 2023–2024;
- receitas municipais 2023–2024;
- PIB municipal 2022–2023;
- metas oficiais de alfabetização.

## Aquisição

O acesso à AWS não integra os notebooks oficiais. A Feature Table e demais produtos herdados devem estar presentes localmente. Fontes públicas podem ser obtidas pelo script documentado do projeto quando disponível.

## Integridade

Para cada arquivo relevante, preserve:

- URL ou sistema de origem;
- data de obtenção;
- nome e tamanho;
- checksum SHA-256;
- período e cobertura;
- licença ou condição de uso;
- transformação aplicada;
- produto derivado correspondente.

## Regras

- não sobrescrever fontes originais;
- não misturar arquivos temporários e oficiais;
- não versionar credenciais;
- registrar joins, filtros e perdas de cobertura;
- preservar manifests junto aos produtos processados;
- documentar mudanças de versão das fontes.
