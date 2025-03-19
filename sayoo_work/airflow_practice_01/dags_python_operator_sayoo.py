from airflow import DAG
from airflow.operators.python import PythonOperator
import pendulum
import random
# dag_id 파일명과 일치시키는 것이 좋음 - dag 명
# schedule_interval - 분 시 일 월
# 캐치업 변수 - 캐치 업 : DAG가 내부적으로 백필을 수행하는 경우 캐치 업을 해제

with DAG(
    dag_id='dags_python_operator_sayoo',
    schedule_interval='30 6 * * *',
    start_date=pendulum.datetime(2025, 3, 19, tz="Asia/Seoul"),
    catchup=False,
    tags=['sa']
) as dag:
    def select_fruit():
        fruit = ['APPLE', 'ORANGE', 'BANANA', 'AVOCADO', 'MANGO']
        random_int = random.randint(0, len(fruit)-1)
        print(fruit[random_int])


    select_fruit_sayoo_t1 = PythonOperator(
        task_id='select_fruit_sayoo_t1',
        python_callable=select_fruit,
    )

    select_fruit_sayoo_t1