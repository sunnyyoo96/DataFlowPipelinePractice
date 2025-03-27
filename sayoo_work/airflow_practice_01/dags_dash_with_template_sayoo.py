from airflow import DAG
import pendulum
import datetime
from airflow.operators.bash import BashOperator

with DAG(
    dag_id='dags_dash_with_template_sayoo',
    schedule= '10 20 * * 4#4',  ## 넷째주 목요일 8시 30분 분 시 일 월 요일
    start_date=pendulum.datetime(2025, 3, 27, tz="UTC"),
    catchup=False,
    tags=['sayoo'],
) as dag:
    bash_t1 = BashOperator(
        task_id='bash_t1',
        bash_command ='echo "data_interval_start:{{ data_interval_start }} data_interval_end:{{ data_interval_end }}"'
    )

    bash_t2 = BashOperator(
        task_id='bash_t2',
        env= {
            'START_DATE' : '{{ data_interval_start | ds }}',
            'END_DATE': '{{ data_interval_end | ds }}'
        },
        bash_command = 'echo {{ data_interval_start }} && {{ data_interval_end }}'
    )

    bash_t1 >> bash_t2