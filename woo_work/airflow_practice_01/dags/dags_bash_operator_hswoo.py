import pendulum
from airflow import DAG
from airflow.operators.bash import BashOperator

# 실제 DAG 생성
with DAG(
        dag_id='dags_bash_operator_hswoo',  # 화면에서 보이는 이름, 파이썬 파일명과 상관없음(파일명=dag_id 통일이 좋음)
        schedule_interval='0 0 * * *',  # 분 시 일 월 주 -> 매일 0시 0분에
        start_date=pendulum.datetime(2025, 3, 10, tz="Asia/Seoul"),  # DAG가 언제부터 돌지에 대한 설정, tz 한국시간으로 변경
        catchup=False,  # ex) 현재 3/1 , start_date 1/1 -> 사이에 누락된 구간을 돌릴지에 대한 유/무, 순차대로 돌는게 아닌 한번에 실행됨
        # dagrun_timeout=datetime.timedelta(minutes=60), # 60분 이상 DAG이 돌면 실패
        # tags=['hswoo1', 'hswoo2'], # 진짜 tag
        # params={"example_key": "example_value"}, # task에서 실제 돌릴때 필요한 파라미터
) as dag:
    # [START howto_operator_bash]
    # task ID
    bash_t1 = BashOperator(
        task_id='bash_t1',  # 객체명과 id는 다름, 보통 task도 객체명과 동일하게 작성
        bash_command='echo  hswoo',
    )

    bash_t2 = BashOperator(
        task_id='bash_t2',  # 객체명과 id는 다름, 보통 task도 객체명과 동일하게 작성
        bash_command='echo  $HOSTNAME',  # $HOSTNAME -> LINUX 환경변수
    )

    ## 순차 실행을 위한 작성
    bash_t1 >> bash_t2
