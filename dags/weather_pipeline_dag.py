from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

from scripts import extract_historical, extract_current
from scripts import clean_historical, clean_current, merge_data

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
    task_id="clean_historical",
    python_callable=clean_historical.clean_historical,
    dag=dag,
)

t4 = PythonOperator(
    task_id="clean_current",
    python_callable=clean_current.clean_current,
    dag=dag,
)

t5 = PythonOperator(
    task_id="merge_data",
    python_callable=merge_data.merge_data,
    dag=dag,
)

t1 >> t2 >> [t3, t4] >> t5
