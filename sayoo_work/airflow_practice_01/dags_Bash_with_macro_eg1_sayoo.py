from airflow import DAG
import pendulum
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id='dags_Bash_with_macro_eg1_sayoo',
    schedule= '10 0 L * *', #매월 말일
    start_date=pendulum.datetime(2025, 3, 1, tz="Asia/Seoul"),
    catchup=False,
)as dag:
    bash_task_1 = BashOperator(
        task_id='bash_task_1',
        env= {
            'START_DATE': '{{  data_interval_start.in_timezone("Asia/Seoul") | ds }}',
            'END_DATE': '{{   data_interval_start.in_timezone("Asia/Seoul") + macros.dateutil.relativedelta.relativedelta(days=-1) | ds}}'
        },
        bash_command='echo "START_DATE: ${START_DATE} && END_DATE: ${END_DATE}"',
    )

datetime.now("Asia/Seoul")