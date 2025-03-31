import pendulum
from airflow import DAG
from airflow.decorators import task
from airflow.operators.python import PythonOperator

with DAG(
        dag_id='dags.dags_python_show_templates_hswoo',
        schedule='50 20 * * *',
        start_date=pendulum.datetime(2025, 3, 31, tz="Asia/Seoul"),
        catchup=False,
        tags=['hswoo'],
) as dag:
    def python_function1(start_date, end_date, **kwargs):
        print(start_date)
        print(end_date)


    python_t1 = PythonOperator(
        task_id='python_t1',
        python_callable=python_function1,
        op_kwargs={'start_date': '{{data_interval_start | ds }}', 'end_date': '{{data_interval_end | ds }}'},
    )


    @task(task_id='python_t2')
    def python_function2(**kwargs):
        print(kwargs)
        print('ds:' + kwargs['ds'])
        print('ts:' + kwargs['ts'])
        print('data_interval_start:' + kwargs['data_interval_start'])
        print('data_interval_end:' + kwargs['data_interval_end'])
        print('task_instance:' + kwargs['ti'])


    python_t1 >> python_function2()
