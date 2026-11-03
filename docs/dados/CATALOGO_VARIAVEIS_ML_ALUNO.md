# Catálogo de variáveis da `ml_aluno`

## Índice

- [Finalidade](#finalidade)
- [Origem e responsabilidade](#origem-e-responsabilidade)
- [Consumidores no pipeline](#consumidores-no-pipeline)
- [Estrutura do CSV](#estrutura-do-csv)
- [Regras de manutenção](#regras-de-manutenção)
- [Referências](#referências)

## Finalidade

O arquivo operacional [ml_aluno_catalogo_variaveis.csv](../data_dictionary/ml_aluno_catalogo_variaveis.csv) é um contrato de metadados da tabela analítica `ml_aluno`. Ele descreve as variáveis disponíveis, mas não contém observações de alunos nem substitui a base de modelagem.

O catálogo é usado para apoiar duas decisões anteriores ao treinamento:

- classificação das variáveis entre identificadores, atributos territoriais, desempenho, amostragem, modelagem e controle técnico;
- associação das variáveis às decisões de seleção de features e à avaliação de risco de *data leakage*.

## Origem e responsabilidade

O conteúdo foi curado a partir do esquema da `ml_aluno` no contexto da etapa TC3-40 — Catálogo de Variáveis. O próprio TC3-41 identifica o CSV como saída conceitual dessa etapa.

O arquivo está versionado no caminho original `docs/data_dictionary/ml_aluno_catalogo_variaveis.csv` porque TC3-41 e TC3-42 dependem diretamente desse contrato. A versão atual possui 19 registros, um por variável da `ml_aluno`.

Nome, caminho, cabeçalho e nomes das variáveis devem ser preservados. Uma alteração estrutural exige mudança coordenada nos notebooks consumidores e nova validação integral do pipeline.

Importante: o notebook modular [TC3-40_Catalogo_Variaveis.ipynb](../../notebooks/fase_2_entendimento_base_dados/TC3-40_Catalogo_Variaveis.ipynb) inventaria fontes e exporta outro catálogo de revisão, mas não regenera automaticamente este CSV específico. Portanto, mudanças no esquema da `ml_aluno` exigem revisão explícita deste arquivo.

## Consumidores no pipeline

- [TC3-41_Selecao_Features.ipynb](../../notebooks/fase_2_entendimento_base_dados/TC3-41_Selecao_Features.ipynb): lê o CSV e combina seus metadados com as decisões de inclusão, exclusão ou avaliação das features.
- [TC3-42_Data_Leakage.ipynb](../../notebooks/fase_2_entendimento_base_dados/TC3-42_Data_Leakage.ipynb): lê o CSV e combina as variáveis com a matriz de riscos de vazamento.
- [TC3_Pipeline_Completo_Alfabetizacao.ipynb](../../notebooks/TC3_Pipeline_Completo_Alfabetizacao.ipynb): incorpora as duas utilizações anteriores no fluxo consolidado.

A remoção ou renomeação do CSV sem atualização desses notebooks interrompe a execução com `FileNotFoundError`.

## Estrutura do CSV

| Coluna | Função |
|---|---|
| `Variável` | nome exato da coluna na `ml_aluno` e chave das junções de metadados |
| `Tipo` | tipo lógico esperado da variável |
| `Fonte` | conjunto de dados de origem; atualmente `ml_aluno` |
| `Descrição` | significado funcional da variável |
| `Categoria` | papel da variável no pipeline analítico |

## Regras de manutenção

Ao alterar o esquema da `ml_aluno`:

1. adicionar, remover ou atualizar o registro correspondente no CSV;
2. manter `Variável` idêntica ao nome da coluna, incluindo maiúsculas, minúsculas e acentos;
3. revisar as matrizes de decisão do TC3-41 e de risco do TC3-42;
4. executar as validações de junção `one_to_one` dos notebooks;
5. atualizar esta página quando a origem, a função ou os consumidores mudarem.

O CSV deve permanecer em UTF-8, com cabeçalho e separador por vírgula.

## Referências

- [Índice geral da documentação](../INDICE.md)
- [Preparação, features e prevenção de leakage](../PREPARACAO_FEATURES_LEAKAGE.md)
- [Dicionário das bases complementares](DICIONARIO_BASES_COMPLEMENTARES.md)
