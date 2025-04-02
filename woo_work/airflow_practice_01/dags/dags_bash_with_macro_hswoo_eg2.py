import pendulum
from airflow import DAG
from airflow.operators.bash import BashOperator

# 실제 DAG 생성
with DAG(
        dag_id='dags_bash_with_macro_hswoo_eg2',  # 화면에서 보이는 이름, 파이썬 파일명과 상관없음(파일명=dag_id 통일이 좋음)
        schedule_interval='2 0 L * 6#2',  # 분 시 일 월 주 -> 매일 0시 0분에
        start_date=pendulum.datetime(2025, 3, 10, tz="Asia/Seoul"),  # DAG가 언제부터 돌지에 대한 설정, tz 한국시간으로 변경
        catchup=False,  # ex) 현재 3/1 , start_date 1/1 -> 사이에 누락된 구간을 돌릴지에 대한 유/무, 순차대로 돌는게 아닌 한번에 실행됨
        tags=['hswoo1'],  # 진짜 tag
) as dag:
    # START_DATE: 2주전 월요일, END_DATE: 2주전 토요일
    bash_task_1 = BashOperator(
        task_id='bash_task_1',
        env={
            # template에서 선언한 날짜는 .in_timezone("Asia/Seoul")이 추가됨
            'START_DATE': '{{ (date_interval_start.in_timezone("Asia/Seoul") - macros.dateutil.relativedelta.relativedelta(days=19)) | ds }}',
            # marcos.dateutil -> import dateutil
            'END_DATE': '{{ (date_interval_end.in_timezone("Asia/Seoul") - macros.dateutil.relativedelta.relativedelta(days=14)) | ds }}'
        },
        bash_command='echo "START_DATE: $START_DATE" && echo "END_DATE: $END_DATE"',
    )

    bash_task_1
