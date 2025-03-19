import pendulum
from airflow import DAG
from airflow.operators.email import EmailOperator

# DAG 정의
with DAG(
        dag_id="dags_bash_select_fruit_sayoo",  # DAG ID
        schedule="0 8 1 * *",
        start_date=pendulum.datetime(2025, 3, 18, tz="Asia/Seoul"),  # 시작 날짜 및 시간대 설정
        catchup=False  # 과거 실행 건 무시
) as dag:
    # EmailOperator 사용하여 task 정의
    send_email_task_sayoo = EmailOperator(
        task_id="send_email_task_sayoo",  # Task ID
        to="yoo4380@gmail.com",
        subject="Airflow 성공메일",
        html_content='Airflow 작업이 완료되었습니다.'
    )