from airflow import DAG
import pendulum
import datetime
from airflow.operators.bash import BashOperator

with DAG(
        dag_id='dags_bash_select_fruit_hswoo',
        schedule='00 22 * * 2#3',
        start_date=pendulum.datetime(2025, 3, 18, tz="Asia/Seoul"),
        catchup=False,
) as dag:
    t_orange = BashOperator(
        task_id='t_orange',
        bash_command='/root/airflow/plugins/select_fruit_hswoo.sh ORANGE',
    )
    t_orange
