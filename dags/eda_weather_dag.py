from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="eda_weather_dag",
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False
) as dag:

    run_eda = BashOperator(
        task_id="run_eda_weather_script",
        bash_command="python /home/adriano/analysis/eda_weather.py"
    )
