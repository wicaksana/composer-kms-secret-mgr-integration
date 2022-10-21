from datetime import timedelta
import time
from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.providers.mysql.operators.mysql import MySqlOperator

DEFAULT_ARGS = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['arif@wicaksana.id'],
    'email_on_failure': False,
    'email_on_retry': False
}

sql = f'''
    INSERT INTO test.Person(PersonID, LastName, FirstName, Address, City)
    VALUES
    ({round(time.time())}, "Name", "Random", "Random Street", "New York");
    '''

with DAG(
    dag_id="insert_record_to_mysql",
    default_args=DEFAULT_ARGS,
    start_date=days_ago(1),
    schedule_interval=None,
    dagrun_timeout=timedelta(minutes=10),
    tags=['demo']
) as dag:
    insert_record = MySqlOperator(
        task_id='insert_record_mysql',
        mysql_conn_id='mysql-conn',
        sql=sql,
    )
