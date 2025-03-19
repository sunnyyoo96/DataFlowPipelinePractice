import random

import pendulum
from airflow import DAG
from airflow.operators.python import PythonOperator

with DAG(
        dag_id='dags_python_operator_hswoo',
        schedule='0 0 * * *',
        start_date=pendulum.datetime(2025, 3, 19, tz="Asia/Seoul"),
        catchup=False,
) as dag:
    # 함수 기반 으로 실행을 하는 오퍼레이터
    def select_fruit():
        fruit = ['APPLE', 'BANANA', 'AVOCADO', 'ORANGE']
        rand_int = random.randint(0, len(fruit) -1)  # 0 ~ 3 개중 랜덤으로 실행
        print(fruit[rand_int])


    py_t1 = PythonOperator(
        task_id='py_t1',
        python_callable=select_fruit  # 어떤 함수를 실행시킬지에 대해 함수명을 작성
    )

    py_t1
