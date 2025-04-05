from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator
import papermill as pm
import os
import sys

#sys.path.append(os.path.abspath("."))  # Agregar la raíz del proyecto

# Configuración del DAG
TAGS = ['ETL']
DAG_ID = "Datos colombia"
DAG_DESCRIPTION = "Ejecuta un Notebook Jupyter"
DAG_SCHEDULE = "0 9 * * *"  # Ejecuta todos los días a las 9 AM

default_args = {
    "start_date": datetime(2024, 4, 24),
}

def execute_notebook():
    input_notebook = f"/opt/notebooks/ETL_EEUU.ipynb"
    output_notebook = f"/opt/notebooks/ETL_EEUU_output_{datetime.now().strftime('%Y%m%d_%H%M%S')}.ipynb"
    
    pm.execute_notebook(
        input_notebook,
        output_notebook
    )

# Definición del DAG
dag = DAG(
    dag_id=DAG_ID,
    description=DAG_DESCRIPTION,
    catchup=False,
    schedule_interval=DAG_SCHEDULE,
    max_active_runs=1,
    dagrun_timeout=timedelta(hours=55),
    default_args=default_args,
    tags=TAGS
)

with dag as dag:
    start_task = EmptyOperator(task_id="inicia_proceso")
    end_task = EmptyOperator(task_id="finaliza_proceso")
    
    notebook_task = PythonOperator(
        task_id="execute_notebook",
        python_callable=execute_notebook,
    )
    
    # Dependencias
    start_task >> notebook_task >> end_task
