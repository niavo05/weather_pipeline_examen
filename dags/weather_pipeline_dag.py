from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

import extract_historical
import extract_current
import clean_and_merge

default_args = {"start_date": datetime(2024, 1, 1), "catchup": False}
dag = DAG("weather_pipeline", schedule="@daily", default_args=default_args)

t1 = PythonOperator(
    task_id="extract_historical",
    python_callable=extract_historical.extract_historical,
    dag=dag,
)

t2 = PythonOperator(
    task_id="extract_current",
    python_callable=extract_current.extract_current,
    dag=dag,
)

t3 = PythonOperator(
    task_id="clean_and_merge",
    python_callable=clean_and_merge.clean_and_merge,
    dag=dag,
)

t1 >> t2 >> t3
