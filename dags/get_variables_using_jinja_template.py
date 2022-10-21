from airflow import DAG
from datetime import timedelta
from airflow.utils.dates import days_ago
from airflow.operators.bash import BashOperator

with DAG(
    dag_id='get_variables_using_jinja_template',
    default_args={
        'depends_on_past': False,
        'email': ['admin@example.com'],
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 1,
        'retry_delay': timedelta(minutes=5),
    },
    schedule_interval=None,
    start_date=days_ago(1),
    tags=['demo']
) as dag:
    
    t1 = BashOperator(
        task_id='print_date',
        bash_command='echo my secret variable: {{ var.value.supersecret }}',
    )