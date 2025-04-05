FROM apache/airflow:2.10.4

USER root

# Instalar las dependencias del sistema si son necesarias
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Cambiar al usuario airflow para instalar los paquetes de Python
USER airflow

# Instalar los paquetes de Python
RUN pip install --no-cache-dir \
    pandas \
    pyarrow \
    psycopg2-binary \
    s3fs \
    pyyaml \
    pydantic \
    sqlalchemy \
    boto3 \
    pyminio \
    papermill \
    ipykernel \
    nbformat