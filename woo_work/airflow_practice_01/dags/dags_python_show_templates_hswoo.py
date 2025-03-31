import pendulum
from airflow import DAG
from airflow.decorators import task

with DAG(
        dag_id='dags.dags_python_show_templates_hswoo',
        schedule='45 19 * * *',
        start_date=pendulum.datetime(2025, 3, 30, tz="Asia/Seoul"),
        catchup=True,
        tags=['hswoo'],
) as dag:

    @task(task_id='python_task')
    def show_templates(**kwargs):
        from pprint import pprint
        pprint(kwargs)

    show_templates()
