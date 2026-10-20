FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    TC3_USAR_GPU=0 \
    TC3_EXECUTAR_SHAP=0

WORKDIR /workspace
RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential libgomp1 \
    && rm -rf /var/lib/apt/lists/*
COPY requirements-cpu.txt requirements.txt ./
RUN python -m pip install --no-cache-dir --upgrade pip \
    && python -m pip install --no-cache-dir -r requirements-cpu.txt
RUN python -m ipykernel install \
    --sys-prefix \
    --name tc3-cpu \
    --display-name "Python 3 (tc3-cpu)"

COPY . /workspace
EXPOSE 8888
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--ServerApp.token="]
