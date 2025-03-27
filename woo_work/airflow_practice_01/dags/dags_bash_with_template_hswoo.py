from airflow import DAG
import pendulum
import datetime
from airflow.operators.bash import BashOperator

with DAG(
        dag_id='dags.dags_bash_with_template_hswoo',
        schedule='10 0 * * *',
        start_date=pendulum.datetime(2025, 3, 27, tz="Asia/Seoul"),
        catchup=False,
        tags=['hswoo'],
) as dag:
    bash_t1 = BashOperator(
        task_id='bash_t1',
        bash_command='echo "data_interval_end: {{ data_interval_end }}"',
    )

    bash_t2 = BashOperator(
        task_id='bash_t2',
        bash_command='echo "data_interval_start: {{ data_interval_start }}"',
    )

    bash_t3 = BashOperator(
        task_id='bash_b2',
        env={
            # ds -> yyyy-mm-dd
            'START_DATE': '{{data_interval_start | ds }}',
            'END_DATE': '{{data_interval_end | ds }}',
        },
        bash_command='echo $START_DATE && echo $END_DATE'
    )

    [bash_t1, bash_t2] > bash_t3
