


indicador_municipal
file: base_dados_fundeb_indicador_municipal_2023_2024.csv
fonte: basedosdados.br_fnde_fundeb.indicador_municipal

Descrição
Indicadores legais e educacionais dos municípios, calculados pelo FNDE a partir das declarações bimestrais no SIOPE. 
Uma linha por município, bimestre e indicador.

| Nome do campo       | Tipo     | Modo     | Descrição                                      |
|---------------------|----------|----------|------------------------------------------------|
| ano                 | INTEGER  | NULLABLE | Ano do exercício financeiro declarado          |
| sigla_uf            | STRING   | NULLABLE | Sigla da unidade federativa do ente declarante |
| id_municipio        | STRING   | NULLABLE | Código IBGE de 7 dígitos do município declarante |
| valor_real          | FLOAT    | NULLABLE | Valor do indicador, quando expresso em reais   |




municipio_receitas_orcamentarias
file: base_de_dados_municipio_receitas_orcamentarias_2023_2024.csv
fonte: basedosdados.br_me_siconfi.municipio_receitas_orcamentarias

Descrição
Tabela de receitas orçamentárias a nível de município.


| Nome do campo   | Tipo    | Modo     | Descrição                          |
|-----------------|---------|----------|------------------------------------|
| ano             | INTEGER | NULLABLE | Ano                                |
| sigla_uf        | STRING  | NULLABLE | Sigla da unidade da federação      |
| id_municipio    | STRING  | NULLABLE | ID Município - IBGE 7 Dígitos      |
| valor           | FLOAT   | NULLABLE | Valor                              |



PIB_Municipios
file: base_de_dados_PIB_Municipios_ 2022_2023.csv
fonte: https://www.ibge.gov.br/estatisticas/economicas/contas-nacionais/9088-produto-interno-bruto-dos-municipios.html?=&t=downloads&utm_source=landing&utm_medium=explica&utm_campaign=pib

Descrição
É o valor total de todos os bens e serviços finais produzidos no município naquele ano.

| Nome do campo | Tipo | Modo | Descrição |
| ------------- | ---- | ---- | --------- |
| Ano | INTEGER | NULLABLE | Ano |
| UF | STRING | NULLABLE | Sigla da unidade da federação |
| Nome UF | STRING | NULLABLE | Nome da unidade da federação |
| Código do Município | INTEGER | NULLABLE | Código municipio |
| Nome do Município | STRING | NULLABLE | Nome municipio |
| Produto Interno Bruto, a preços correntes | FLOAT | NULLABLE | O valor está aos preços do próprio ano (preços nominais) |
| Produto Interno Bruto per capita, a preços correntes | FLOAT | NULLABLE | O valor está aos preços do próprio ano (preços nominais) |


bolsa_familia
file: base_dados_bolsa_familia_2023_2024.csv
fonte: basedosdados.br_cgu_beneficios_cidadao.novo_bolsa_familia

Descrição
Números do Novo Bolsa Família

| Nome do campo | Tipo | Modo | Descrição |
| ------------- | ---- | ---- | --------- |
| ano_referencia | INTEGER | NULLABLE | Ano da folha de pagamento |
| id_municipio | STRING | NULLABLE | ID Município - IBGE 7 Dígitos |
| sigla_uf | STRING | NULLABLE | Sigla da Unidade Federativa do beneficiário |
| valor_parcela | FLOAT | NULLABLE | Valor da parcela do benefício |