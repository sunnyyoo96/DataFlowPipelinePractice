import pendulum
from airflow import DAG
from airflow.operators.bash import BashOperator

# DAG 정의
with DAG(
        dag_id="dags_bash_select_fruit_sayoo",  # DAG ID
        schedule="00 22 * * 2#3",  # 매월 첫 번째 토요일 00:10에 실행
        start_date=pendulum.datetime(2025, 3, 18, tz="Asia/Seoul"),  # 시작 날짜 및 시간대 설정
        catchup=False  # 과거 실행 건 무시
) as dag:
    # BashOperator를 사용하여 task 정의
    t1_avocado = BashOperator(
        task_id="t1_avocado",  # Task ID
        bash_command="/root/airflow/plugins/select_fruit_sayoo.sh AVOCADO",  # 실행할 쉘 명령어
    )

    t1_avocado
