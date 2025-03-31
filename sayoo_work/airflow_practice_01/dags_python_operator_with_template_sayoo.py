from airflow import DAG
import pendulum
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.decorators import task

with DAG(
    dag_id='dags_dash_with_template_sayoo',
    schedule= '10 20 * * 1#5',  ## 넷째주 목요일 8시 30분 분 시 일 월 요일
    start_date=pendulum.datetime(2025, 3, 27, tz="UTC"),
    catchup=False,
    tags=['sayoo'],
) as dag:
    def python_function(start_date, end_date, **kwargs):
        print(start_date)
        print(end_date)


    python_t1 = PythonOperator(
        task_id='python_t1',
        python_callable=python_function,
        op_kwargs= {'start_date : {{ data_interval_start | ds }}', 'end_date : {{ data_interval_end | ds }}'}
    )

    @task(task_id='python_t2')
    def python_function2(**kwargs):
        print(kwargs)
        print('ds:' +kwargs['ds'] )
        print('ts:' +kwargs['ts'] )
        print('data_interval_start:' +kwargs['data_interval_start'] )
        print('data_interval_end:' +kwargs['data_interval_end'] )
        print('task_instance:' +kwargs['ti'] )

    python_t1 >> python_function2