# This is a sample Python script.

# Press Alt+Shift+X to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator
import pendulum

# dag_id 파일명과 일치시키는 것이 좋음 - dag 명
# schedule_interval - 분 시 일 월
# 캐치업 변수 - 캐치 업 : DAG가 내부적으로 백필을 수행하는 경우 캐치 업을 해제

with DAG(
    dag_id='dags_bash_operator_sayoo',
    schedule_interval='0 0 * * *',
    start_date=pendulum.datetime(2025, 3, 11, tz="Asia/Seoul"),
    catchup=False,
    tags=['sa']
) as dag:
    bash_t1 = BashOperator(
        task_id='bash_t1',
        bash_command='echo sayoo',
    )

    bash_t2 = BashOperator(
        task_id='bash_t2',
        bash_command='echo sayoo2',
    )
    bash_t1 >> bash_t2

# Press the green button in the gutter to run the script.
# if __name__ == "__main__":
#     dag.cli()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
