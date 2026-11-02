# Power BI — Alfabetização

## Índice

- [Objetivo](#objetivo)
- [Arquivos e fontes de dados](#arquivos-e-fontes-de-dados)
- [Organização do relatório](#organização-do-relatório)
- [Indicadores, medidas e filtros](#indicadores-medidas-e-filtros)
- [Estrutura de entrega](#estrutura-de-entrega)
- [Abertura e atualização em outro computador](#abertura-e-atualização-em-outro-computador)
- [Publicação e validações](#publicação-e-validações)
- [Limitações e interpretação](#limitações-e-interpretação)
- [Considerações finais](#considerações-finais)

## Objetivo

O relatório interativo organiza e apresenta indicadores relacionados à alfabetização, ao acompanhamento de metas educacionais, à infraestrutura escolar e ao contexto socioeconômico dos municípios. Seu objetivo é facilitar a exploração visual dos resultados consolidados do projeto e apoiar a interpretação das análises.

O relatório complementa as análises desenvolvidas em Python e não realiza treinamento de modelos de aprendizado de máquina. Para atualizar suas fontes, primeiro gere os artefatos finais pelo TC3-64 no fluxo modular ou pelo pipeline consolidado completo. Para a entrega oficial, use as tabelas da execução consolidada, fonte de verdade do projeto; não misture tabelas de testes modulares com indicadores oficiais. Consultar o arquivo já salvo não exige reexecutar notebooks.

## Arquivos e fontes de dados

**Relatório:** [TC3_Alfabetizacao.pbix](power_BI/TC3_Alfabetizacao.pbix)

Consulte o [índice técnico](INDICE.md) para o percurso completo e o [README principal](../README.md) para a visão geral do projeto.

**Diretório de origem das tabelas:** `resultados/tabelas/`

Arquivos CSV identificados como fontes do relatório:

- `03_inse_por_faixa_ano.csv`
- `09_municipios_clusters.csv`
- `11_risco_municipal_metas_2024_2030.csv`

Os CSVs são resultados exportados de etapas anteriores do pipeline analítico. As regras de preparação, integração e classificação dos dados devem ser consultadas nos respectivos artefatos do projeto.

As conexões das consultas foram ajustadas para os arquivos utilizados na versão final do relatório. Em outro computador, a atualização das consultas pode exigir a configuração dos caminhos locais no Power Query.

## Organização do relatório

O relatório contém cinco páginas:

### 1. Panorama da alfabetização

Apresenta indicadores gerais, incluindo quantidade de registros, número de municípios distintos e indicador de alfabetização, com possibilidades de análise por período e recortes territoriais disponíveis.

### 2. Municípios e metas

Reúne indicadores de cobertura das metas e de classificação de risco municipal para o período de 2024 a 2030. As categorias e condições de classificação são provenientes das tabelas consolidadas; o relatório não redefine esses critérios.

### 3. Infraestrutura escolar

Apresenta visualizações relacionadas a bibliotecas ou salas de leitura, laboratórios de informática, acesso à internet e banda larga, permitindo observar padrões associados aos indicadores de alfabetização.

### 4. Contexto socioeconômico

Explora informações do Índice de Nível Socioeconômico (INSE), suas relações com indicadores de alfabetização e comparações entre valores observados e estimados, conforme os campos disponíveis nas visualizações.

### 5. Síntese dos resultados

Consolida indicadores e conclusões principais, acompanhados dos cuidados necessários à interpretação dos resultados.

## Indicadores, medidas e filtros

### Contagem de municípios distintos

A seguinte medida DAX foi conferida no relatório:

```dax
Municípios analisados =
DISTINCTCOUNT(Panorama_Municipal[id_municipio])
```

A função `DISTINCTCOUNT` contabiliza identificadores únicos de municípios no contexto de filtros vigente. Assim, o número de municípios analisados não deve ser confundido com a quantidade total de registros.

Os demais indicadores dependem das medidas, agregações, relações e filtros configurados no arquivo `.pbix`. Suas fórmulas não são reproduzidas aqui porque não foram individualmente conferidas.

### Cuidados com a comparação de números

Ao confrontar indicadores de diferentes páginas ou outros artefatos do projeto, é necessário observar:

- O período e os filtros ativos;
- A unidade de análise (registro, município ou outro agrupamento);
- A cobertura dos dados e os valores ausentes;
- O método de agregação;
- A distinção entre indicadores observados, estimativas e classificações de risco.

Resultados apresentados em contextos de filtro distintos não são necessariamente comparáveis de forma direta.

## Estrutura de entrega

```text
docs/
├── POWER_BI_ALFABETIZACAO.md
└── power_BI/
    ├── TC3_Alfabetizacao.pbix
    └── imagens/
        ├── 01_panorama_da_alfabetização.png
        ├── 02_municipios_e_metas.png
        ├── 03_infraestrutura_escolar.png
        ├── 04_contexto_socioeconômico.png
        └── 05_síntese_dos_resultados.png
```

As imagens permitem consultar uma representação estática das páginas diretamente no repositório. O arquivo `.pbix` mantém o relatório interativo.

- [Panorama da alfabetização](power_BI/imagens/01_panorama_da_alfabetização.png)
- [Municípios e metas](power_BI/imagens/02_municipios_e_metas.png)
- [Infraestrutura escolar](power_BI/imagens/03_infraestrutura_escolar.png)
- [Contexto socioeconômico](power_BI/imagens/04_contexto_socioeconômico.png)
- [Síntese dos resultados](power_BI/imagens/05_síntese_dos_resultados.png)

O `.pbix` e as imagens são artefatos de apresentação mantidos separadamente dos notebooks. Atualizar os CSVs não atualiza automaticamente os dados importados do relatório, as capturas ou a versão publicada; esses produtos precisam ser atualizados e conferidos antes de uma nova entrega.

## Abertura e atualização em outro computador

1. Obter o repositório, preservando sua estrutura de diretórios.
2. Abrir `docs/power_BI/TC3_Alfabetizacao.pbix` no Microsoft Power BI Desktop.
3. Navegar pelas cinco páginas para consultar os dados já importados e salvos no arquivo.
4. **Somente se desejar atualizar os dados**, verificar a disponibilidade dos CSVs em `resultados/tabelas/`.
5. Se necessário, abrir o Power Query e ajustar os caminhos das fontes para a cópia local do repositório.
6. Aplicar as alterações e atualizar o modelo, conferindo se as consultas foram concluídas sem erros.

**Observação:** a abertura e a visualização dos dados importados já armazenados no `.pbix` normalmente não exigem o acesso imediato aos CSVs originais. Esses arquivos são necessários para a atualização das fontes.

## Publicação e validações

Na versão preparada para entrega, a documentação recebida da equipe registra as seguintes validações:

- Existência e navegação pelas cinco páginas;
- Reabertura do arquivo `.pbix` com carregamento normal das visualizações;
- Conferência dos caminhos das fontes de dados;
- Verificação da medida de contagem distinta de municípios;
- Publicação no Power BI Service;
- Abertura e navegação pelo relatório publicado em janela anônima do navegador.

O endereço de publicação pode ser disponibilizado separadamente na apresentação ou no repositório, conforme a organização adotada pela equipe.

## Limitações e interpretação

- Os resultados dependem da qualidade, da cobertura e da granularidade dos dados consolidados.
- Diferenças entre anos ou municípios podem refletir mudanças de composição e disponibilidade das informações.
- Associações entre infraestrutura, contexto socioeconômico e alfabetização não demonstram causalidade.
- Estimativas de modelos preditivos não representam garantias de resultados futuros.
- Classificações de risco e metas devem ser interpretadas conforme as regras definidas nas etapas anteriores do pipeline.
- A reprodução integral de uma atualização depende da disponibilidade das fontes e da configuração correta dos caminhos locais.

## Considerações finais

O relatório Power BI transforma resultados consolidados em uma interface visual para explorar indicadores, identificar padrões e comunicar achados relevantes. Sua utilização deve respeitar o contexto dos filtros, a origem dos dados e as limitações metodológicas descritas nesta documentação.
