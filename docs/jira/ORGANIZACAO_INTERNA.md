# Organização interna e rastreabilidade

## Índice

- [Uso de identificadores internos](#uso-de-identificadores-internos)
- [Entrega final](#entrega-final)
- [Notebook consolidado e chave do projeto](#notebook-consolidado-e-chave-do-projeto)
- [Critério adotado](#criterio-adotado)
- [Índice geral](../INDICE.md)

Durante o desenvolvimento do projeto, a equipe utilizou uma ferramenta interna de gestao de tarefas para dividir responsabilidades, acompanhar o progresso e organizar revisoes.

Essa organizacao teve como objetivo apoiar o trabalho colaborativo, mantendo rastreabilidade entre:

- etapa analitica;
- branch de desenvolvimento;
- notebook ou codigo produzido;
- revisao da equipe;
- entrega consolidada.

## Uso de identificadores internos

Alguns arquivos de trabalho podem conter identificadores internos no nome, como `TC3-41_Selecao_Features.ipynb`.

Esse padrao foi utilizado para facilitar a colaboracao durante o desenvolvimento, pois permite associar rapidamente um artefato tecnico a uma atividade planejada pela equipe.

Esses identificadores nao fazem parte da solucao analitica em si. Eles funcionam apenas como apoio de organizacao e rastreabilidade.

## Entrega final

Para a entrega final, a leitura principal deve seguir o pipeline consolidado e, para análise detalhada, os notebooks modulares organizados pelas etapas metodológicas:

- entendimento da base;
- analise exploratoria;
- engenharia e selecao de features;
- avaliacao de Data Leakage;
- pipeline de pre-processamento;
- modelagem supervisionada;
- avaliacao de resultados;
- interpretabilidade e insights.

A ferramenta de gestao utilizada pela equipe nao e requisito para reproducao do projeto e nao deve ser considerada dependencia da entrega.

## Notebook consolidado e chave do projeto

O arquivo `notebooks/TC3_Pipeline_Completo_Alfabetizacao.ipynb` não possui uma chave de tarefa própria no Jira. Ele está associado somente à chave geral do projeto porque não representa uma etapa analítica independente: é a consolidação executável do trabalho distribuído entre as tarefas e os notebooks modulares.

O particionamento por tarefas é a organização mais adequada para desenvolvimento, revisão, rastreabilidade e apresentação acadêmica. Cada notebook modular delimita uma responsabilidade e permite relacionar a implementação à respectiva atividade do projeto.

Para a execução integral, entretanto, a equipe decidiu manter também um notebook consolidado. Sua finalidade operacional foi permitir que todo o pipeline fosse executado sequencialmente, sem intervenção manual entre etapas, inclusive em execuções prolongadas durante a noite.

Por ter sido o artefato efetivamente utilizado na execução contínua validada, o notebook consolidado é a fonte de verdade para métricas finais, decisões congeladas e artefatos oficiais. Os notebooks modulares continuam sendo a referência para análise detalhada e rastreabilidade e devem permanecer metodologicamente alinhados ao consolidado.

Assim, a ausência de uma chave exclusiva não representa falta de rastreabilidade. Ela evita atribuir artificialmente uma única tarefa a um artefato transversal que reúne entregas de várias chaves do projeto.

## Criterio adotado

O criterio adotado foi separar claramente:

- **organizacao interna:** utilizada para planejamento, colaboracao e rastreabilidade da equipe;
- **entrega tecnica:** composta por notebooks, codigo, dados documentados, modelos, relatorios e README;
- **avaliacao final:** orientada pelos resultados analiticos, pela reproducibilidade e pela clareza da solucao apresentada.

Assim, a referencia a identificadores internos pode aparecer em nomes de arquivos, branches ou historico de desenvolvimento, mas a documentacao final deve explicar o projeto por suas etapas tecnicas e pelos resultados obtidos.
