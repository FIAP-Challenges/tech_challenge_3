# Guia de execução e reprodutibilidade

## Índice

- [Escolha do perfil](#1-escolha-do-perfil)
- [Requisitos de hardware](#2-requisitos-de-hardware)
- [Pré-requisitos](#3-pré-requisitos)
- [Executar em CPU](#4-executar-em-cpu)
- [Executar em GPU](#5-executar-em-gpu)
- [Parar e reconstruir CPU](#6-parar-reiniciar-e-reconstruir-cpu)
- [Parar e reconstruir GPU](#7-parar-reiniciar-e-reconstruir-gpu)
- [Encerrar todo o projeto](#8-encerrar-todo-o-projeto-docker)
- [Formas de executar os notebooks](#9-formas-de-executar-os-notebooks)
- [Dados e contratos](#10-dados-e-contratos)
- [Determinismo](#11-determinismo)
- [Registro obrigatório](#12-registro-obrigatório)
- [Checklist de sucesso](#13-checklist-de-sucesso)
- [Comparação e equivalência entre execuções](#14-comparação-e-equivalência-entre-execuções)
- [Índice geral](INDICE.md)

Este documento define como preparar, iniciar, validar, parar e reconstruir os ambientes do Tech Challenge 3. Os perfis CPU e GPU são independentes e não devem ser misturados na mesma execução.

## 1. Escolha do perfil

| Item | CPU | GPU |
|---|---|---|
| Serviço Compose | `notebook-cpu` | `notebook-gpu` |
| Dockerfile | `Dockerfile` | `Dockerfile.gpu` |
| Dependências | `requirements-cpu.txt` | `requirements-gpu.txt` |
| Kernel | `Python 3 (tc3-cpu)` | `Python 3 (tc3-gpu)` |
| Porta no host | `8888` | `8889` |
| Backend esperado | scikit-learn | RAPIDS cuML quando compatível |
| Variável principal | `TC3_USAR_GPU=0` | `TC3_USAR_GPU=1` |

Use CPU quando a prioridade for portabilidade ou quando não houver GPU NVIDIA. Use GPU para reduzir o tempo dos estimadores compatíveis e para a execução controlada do SHAP.

## 2. Requisitos de hardware

### CPU

- processador compatível com Docker;
- memória suficiente para carregar as partições e matrizes da etapa executada;
- espaço livre para imagens, dados e artefatos gerados.

### GPU

- GPU NVIDIA com driver compatível com a imagem CUDA;
- Docker com acesso à GPU;
- 6 GB de VRAM foram validados com uma RTX 3050 Laptop;
- memória RAM e espaço em disco suficientes para a imagem RAPIDS, os dados e os artefatos.

A execução registrada no notebook consolidado utilizou Python 3.12.11, scikit-learn 1.7.2, Polars 2.0.0, RAPIDS cuML, uma RTX 3050 Laptop com 6 GB de VRAM e SHAP com amostra de 100 observações. CPU e GPU podem produzir pequenas diferenças numéricas.

## 3. Pré-requisitos

Instale Git, Docker Desktop no Windows/macOS ou Docker Engine com o plugin Compose no Linux. VS Code, Python, Jupyter e Dev Containers são opcionais. Para GPU, também são necessários driver NVIDIA e suporte NVIDIA no Docker/WSL2.

Na raiz do projeto, valide:

```powershell
docker version
docker compose version
docker compose config
```

No perfil GPU:

```powershell
nvidia-smi
docker compose --profile gpu config
```

## 4. Executar em CPU

```powershell
docker compose build notebook-cpu
docker compose up -d notebook-cpu
docker compose logs -f notebook-cpu
```

Abra `http://localhost:8888` e selecione `Python 3 (tc3-cpu)`.

Valide o ambiente:

```powershell
docker compose exec notebook-cpu python --version
docker compose exec notebook-cpu python -c "import polars, sklearn, pyarrow; print(polars.__version__, sklearn.__version__, pyarrow.__version__)"
docker compose exec notebook-cpu python -c "import os; print({k: v for k, v in os.environ.items() if k.startswith('TC3_')})"
```

O backend registrado ao final deve indicar scikit-learn CPU.

## 5. Executar em GPU

Confirme o dispositivo no host e no contêiner:

```powershell
nvidia-smi
docker compose --profile gpu run --rm notebook-gpu nvidia-smi
```

Construa e inicie:

```powershell
docker compose --profile gpu build notebook-gpu
docker compose --profile gpu up -d notebook-gpu
docker compose --profile gpu logs -f notebook-gpu
```

Abra `http://localhost:8889` e selecione `Python 3 (tc3-gpu)`.

Valide o ambiente:

```powershell
docker compose --profile gpu exec notebook-gpu python --version
docker compose --profile gpu exec notebook-gpu nvidia-smi
docker compose --profile gpu exec notebook-gpu python -c "import sklearn; print(sklearn.__version__)"
```

Monitore uma execução longa com `nvidia-smi -l 2`. A presença da GPU não garante que todas as etapas sejam aceleradas. Polars, gráficos, métricas e algoritmos sem suporte continuam na CPU. A evidência válida é o backend gravado no relatório.

## 6. Parar, reiniciar e reconstruir CPU

Parar somente CPU:

```powershell
docker compose stop notebook-cpu
```

Reiniciar CPU sem reinstalar dependências:

```powershell
docker compose up -d notebook-cpu
```

Reconstruir depois de alterar `Dockerfile`, `requirements.txt` ou `requirements-cpu.txt`:

```powershell
docker compose build --no-cache notebook-cpu
docker compose up -d --force-recreate notebook-cpu
```

Consultar CPU:

```powershell
docker compose ps notebook-cpu
docker compose logs -f notebook-cpu
```

## 7. Parar, reiniciar e reconstruir GPU

Parar somente GPU:

```powershell
docker compose --profile gpu stop notebook-gpu
```

Reiniciar GPU sem reinstalar dependências:

```powershell
docker compose --profile gpu up -d notebook-gpu
```

Reconstruir depois de alterar `Dockerfile.gpu` ou `requirements-gpu.txt`:

```powershell
docker compose --profile gpu build --no-cache notebook-gpu
docker compose --profile gpu up -d --force-recreate notebook-gpu
```

Consultar GPU:

```powershell
docker compose --profile gpu ps notebook-gpu
docker compose --profile gpu logs -f notebook-gpu
```

## 8. Encerrar todo o projeto Docker

Use somente quando quiser remover os contêineres dos dois perfis e a rede compartilhada:

```powershell
docker compose --profile gpu down
```

Os arquivos permanecem no host porque a raiz é montada em `/workspace`. Não acrescente `--volumes` e não execute limpeza global do Docker sem revisar o impacto em outros projetos.

## 9. Formas de executar os notebooks

O projeto possui duas apresentações complementares do mesmo trabalho.

### Fluxo consolidado

```text
notebooks/TC3_Pipeline_Completo_Alfabetizacao.ipynb
```

Ele é a referência para reprodução integral, decisões metodológicas oficiais, métricas finais e relatórios consolidados. Execute com **Restart Kernel and Run All Cells**.

### Fluxo modular para análise acadêmica

O particionamento facilita a avaliação detalhada pelo professor. Os notebooks modulares estão integrados à `main` e seguem esta ordem:

1. auditoria, entendimento e integração das bases;
2. análise exploratória e qualidade dos dados;
3. preparação e contrato de features;
4. treinamento dos baselines e modelos iniciais;
5. otimização e seleção do modelo;
6. avaliação final em conjunto independente;
7. visualizações, interpretação e comunicação dos resultados.

Nos notebooks modulares, siga a organização das pastas por fase e a sequência metodológica acima. Identificadores presentes nos nomes dos arquivos são usados para rastreabilidade e não determinam, isoladamente, a ordem de execução.

Os notebooks modulares explicam cada etapa separadamente. Uma execução isolada pode produzir resultados experimentais ligeiramente diferentes. Quando houver divergência, a seleção oficial e as métricas finais são as registradas pelo pipeline consolidado e pelos artefatos aprovados.

### Notebooks de comunicação

No fluxo modular, execute [TC3_Visualizacoes_e_Insights.ipynb](../notebooks/TC3_Visualizacoes_e_Insights.ipynb) após o TC3-64, que gera a avaliação e as tabelas finais. No fluxo integral, execute-o após a conclusão do consolidado. Não é necessário executar o notebook gerencial antes de Insights. Use os artefatos da mesma execução de referência dos valores fixos e imagens incorporadas.

Depois de gerar os artefatos oficiais, consulte os procedimentos próprios de [Análise Gerencial do Random Forest](ANALISE_GERENCIAL_RANDOM_FOREST.md) e [Visualizações e Insights](VISUALIZACOES_E_INSIGHTS.md). O primeiro carrega o modelo serializado e depende de um ambiente compatível; o segundo apresenta métricas, textos e imagens incorporados da execução oficial e carrega os CSVs de infraestrutura e finanças disponíveis em `resultados/tabelas/`. Esses CSVs devem pertencer à mesma execução de referência dos valores incorporados. Reexecutar o notebook atualiza as visualizações que leem arquivos, mas não recalcula automaticamente os números fixos nem substitui as imagens incorporadas.

Para reexecutar Visualizações e Insights, use o ambiente atualizado dos arquivos de requirements, que declaram pandas explicitamente. No kernel escolhido, valide com `import pandas, matplotlib, IPython`. Se o ambiente foi criado antes da atualização das dependências, reinstale os requirements correspondentes ou reconstrua o contêiner conforme as instruções deste guia.

### Painel Power BI

O [Power BI](POWER_BI_ALFABETIZACAO.md) é uma etapa complementar de exploração e comunicação. A abertura do `.pbix` permite consultar os dados já importados. Para atualizar o painel, gere antes as tabelas finais pelo TC3-64 ou pelo consolidado completo, use a execução oficial de referência e ajuste os caminhos no Power Query conforme a documentação própria. As imagens e a publicação no serviço não são atualizadas automaticamente pelos notebooks.

## 10. Dados e contratos

Antes da modelagem, confirme:

- fontes necessárias em `dados/`;
- schemas e partições Hive dos Parquets;
- manifests da base e das metas;
- 18 features, target e colunas de controle;
- ausência de identificadores e leakage nas features;
- teste reservado exclusivamente para a avaliação final.

O acesso à AWS não faz parte da execução dos notebooks. As fontes herdadas devem estar disponíveis localmente conforme a documentação de linhagem.

## 11. Determinismo

A seed padrão é `42`. Ela controla amostragem por hash, splits, buscas, modelos e bootstrap quando aplicável. Seed fixa não garante igualdade binária entre máquinas.

Versões de Python, NumPy, scikit-learn, BLAS, CUDA ou RAPIDS, número de threads, ordem das partições e algoritmos distintos em CPU/GPU podem causar diferenças. Compare contratos, contagens, splits, ausência de leakage e métricas dentro de tolerância, não arquivos binários idênticos. Modelos Joblib devem ser carregados com versão compatível do scikit-learn; quando não houver compatibilidade garantida, regenere o artefato no ambiente-alvo por meio do pipeline consolidado.

## 12. Registro obrigatório

Registre em cada execução:

```powershell
python --version
python -m pip freeze
git rev-parse HEAD
git status --short
docker version
docker compose version
nvidia-smi
```

Inclua sistema operacional, arquitetura, CPU, RAM, GPU, VRAM, driver, digest da imagem, kernel, variáveis `TC3_*`, checksums dos dados, duração, seed, backend efetivo, parâmetros e alterações locais.

Relatórios esperados:

```text
resultados/relatorios/ambiente_execucao.json
resultados/relatorios/status_execucao.json
```

## 13. Checklist de sucesso

- `docker compose config` termina sem erro;
- somente o perfil desejado está ativo;
- Jupyter abre na porta correta;
- o kernel corresponde ao perfil;
- no perfil GPU, `nvidia-smi` funciona dentro do contêiner;
- as células executam em ordem e sem traceback;
- o relatório termina com estado `concluido`;
- o backend registrado corresponde ao esperado;
- manifests, schemas e 18 features conferem;
- não há sobreposição de grupos nas separações de validação agrupada da otimização; a sobreposição escolar do split oficial por aluno é diagnosticada separadamente;
- o teste não foi usado no tuning;
- métricas e artefatos finais são legíveis e coerentes.

## 14. Comparação e equivalência entre execuções

A execução modular de teste preservou as 18 features, os hiperparâmetros do modelo final, o limiar e os 581.591 registros de teste. O Random Forest permaneceu selecionado. O ROC AUC passou de 0,670483 no consolidado para 0,670605 no modular; o F1 passou de 0,639195 para 0,639193. A proximidade global não implica igualdade em cada território ou produto exploratório.

A análise de clusters selecionou três grupos no consolidado (silhouette 0,240664) e quatro no modular (0,247371). Houve diferenças localizadas: o F1 do Pará passou de 0,1185 para 0,1768 e a diferença máxima nas probabilidades médias municipais chegou a 6,92 pontos percentuais em um recorte de 2023 com 31 registros. Categorias de risco também podem mudar perto de seus limites. Esses resultados exigem ressalva; não cabe afirmar equivalência de todas as conclusões analíticas.

Backend, hardware, versões, paralelismo e ordem dos dados podem contribuir para variações. No agrupamento, a agregação sem ordenação explícita e a amostragem por posição são possíveis fontes de sensibilidade, mesmo com seed fixa. Essa hipótese não foi isolada em teste controlado. Não foi estabelecida uma tolerância formal de aprovação para todos os produtos; os números acima descrevem a comparação observada.

Para a entrega, o consolidado continua sendo a fonte de verdade, incluindo os três clusters. Preserve seus artefatos e execute testes modulares em cópias separadas, sem substituir os resultados oficiais pelos de teste. Para os notebooks de apresentação, use modelo, tabelas, métricas, imagens e textos da mesma execução de referência.

A execução sem erros demonstra viabilidade operacional, mas não prova, isoladamente, correção metodológica ou estabilidade territorial. Compare também contratos, população, splits, diagnósticos de leakage e resultados por recorte. O split oficial por aluno deve ser distinguido da validação agrupada da otimização. Modelos Joblib requerem ambiente compatível e não são garantidamente portáveis entre versões de scikit-learn.
