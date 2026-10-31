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

O particionamento facilita a avaliação detalhada pelo professor. Após a integração dos notebooks modulares na `main`, a ordem será:

1. auditoria, entendimento e integração das bases;
2. análise exploratória e qualidade dos dados;
3. preparação e contrato de features;
4. treinamento dos baselines e modelos iniciais;
5. otimização e seleção do modelo;
6. avaliação final em conjunto independente;
7. visualizações, interpretação e comunicação dos resultados.

Nos notebooks modulares, siga a organização das pastas por fase e a sequência metodológica acima. Identificadores presentes nos nomes dos arquivos são usados para rastreabilidade e não determinam, isoladamente, a ordem de execução.

Os notebooks modulares explicam cada etapa separadamente. Uma execução isolada pode produzir resultados experimentais ligeiramente diferentes. Quando houver divergência, a seleção oficial e as métricas finais são as registradas pelo pipeline consolidado e pelos artefatos aprovados.

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
- não há sobreposição de grupos na validação;
- o teste não foi usado no tuning;
- métricas e artefatos finais são legíveis e coerentes.

## 14. Comparação e equivalência entre execuções

As execuções integral e modular apresentaram pequenas diferenças numéricas, dentro do comportamento esperado para ambientes e caminhos de execução distintos. Essas variações podem decorrer do backend CPU ou GPU, das versões das bibliotecas, do paralelismo, da ordem de processamento e de operações numéricas não determinísticas.

A comparação preservou os elementos que definem a equivalência metodológica: esquema e população analisada, separação dos conjuntos, contrato das 18 features, prevenção de leakage, família do modelo selecionado e interpretação geral dos resultados. As métricas permaneceram na mesma ordem de grandeza e não alteraram as conclusões do projeto.

Esse resultado sustenta que o pipeline é executável e metodologicamente estável em mais de um percurso. A divergência, isoladamente, não prova a correção do código; a evidência de correção é formada em conjunto pelas validações de schema, splits, ausência de leakage, execução sem erros, artefatos produzidos e métricas dentro das tolerâncias esperadas.

Reprodução não exige igualdade bit a bit entre CPU e GPU. Compare contratos e métricas dentro de tolerância previamente definida. Para a entrega, os valores oficiais continuam sendo os registrados pelo notebook consolidado. Modelos Joblib não são garantidamente portáveis entre versões distintas do scikit-learn.
