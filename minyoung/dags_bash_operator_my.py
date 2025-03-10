from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.dummy import DummyOperator

with DAG(
    dag_id='dags_bash_operator_my',
    schedule_interval='0 0 * * *',
    start_date=datetime(2021, 1, 1),
    catchup=False,
    dagrun_timeout=timedelta(minutes=60),
) as dag:
     bash_t1 = BashOperator(
        task_id='bash_t1',
        bash_command='echo whoami',
    )

     bash_t2 = BashOperator(
        task_id='bash_t2',
        bash_command='echo $HOSTNAME',
    
     )

    bash_t1 >> bash_t2