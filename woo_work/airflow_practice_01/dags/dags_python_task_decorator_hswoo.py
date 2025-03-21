import pendulum
from airflow import DAG
from airflow.decorators import task

with DAG(
        dag_id="dags_python_task_decorator_hswoo",
        schedule="30 20 * * 5#3",
        start_date=pendulum.datetime(2025, 3, 21, tz="Asia/Seoul"),
        catchup=False,
        tags=["hswoo"]
) as dag:
    
    ## tast 에대한 순서도를 그릴 필요 없음
    @task(task_id="python_task_1")
    def print_context(some_input):
        print(some_input)


    python_task_1 = print_context("task_decorator 실행")
