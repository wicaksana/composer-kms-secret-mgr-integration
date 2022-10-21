from datetime import datetime, timedelta
from airflow import DAG 
from airflow.operators.bash import BashOperator

with DAG(
    dag_id='tutorial',
    default_args={
        'depends_on_past': False,
        'email': ['admin@example.com'],
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 1,
        'retry_delay': timedelta(minutes=5),
    },
    schedule=None,
    start_date=datetime(2022, 10, 20),
    catchup=False,
    tags=['demo']
) as dag:
    
    t1 = BashOperator(
        task_id='print_date',
        bash_command='date',
    )

    t2 = BashOperator(
        task_id='sleep',
        depends_on_past=False,
        bash_command='sleep 5',
        retries=3,
    )

    t1 >> t2

