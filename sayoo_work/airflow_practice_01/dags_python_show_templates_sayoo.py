from airflow import DAG
import pendulum
from airflow.decorators import task

# dag_id 파일명과 일치시키는 것이 좋음 - dag 명
# schedule_interval - 분 시 일 월
# 캐치업 변수 - 캐치 업 : DAG가 내부적으로 백필을 수행하는 경우 캐치 업을 해제

with DAG(
    dag_id='dags_python_show_templates_sayoo',
    schedule_interval='30 19 * * *',
    start_date=pendulum.datetime(2025, 3, 31, tz="Asia/Seoul"),
    catchup=True,
    tags=['sa']
) as dag:

    @task(task_id = 'python task')
    def show_templates(**kwargs):
       from pprint import pprint
       pprint(kwargs)

    show_templates()