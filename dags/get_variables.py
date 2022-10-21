from datetime import timedelta
from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python import PythonOperator
from airflow.models import Variable


DEFAULT_ARGS = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['arif@wicaksana.id'],
    'email_on_failure': False,
    'email_on_retry': False
}

def get_variable_fn(**kwargs):
    my_var = Variable.get('my-secret', default_var='Undefined')
    print('My variable name: ', my_var)
    return my_var


with DAG(
    dag_id="get_variables_from_Secret_Manager",
    default_args=DEFAULT_ARGS,
    start_date=days_ago(1),
    schedule_interval=None,
    dagrun_timeout=timedelta(minutes=10),
    tags=['demo']
) as dag:
    get_variable = PythonOperator(
        task_id='get_variable',
        python_callable=get_variable_fn,
        show_return_value_in_logs=True,
    )