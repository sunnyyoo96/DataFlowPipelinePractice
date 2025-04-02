import pendulum
from airflow import DAG
from airflow.decorators import task

# 실제 DAG 생성
with DAG(
        dag_id='dags_python_with_macro_hswoo',  # 화면에서 보이는 이름, 파이썬 파일명과 상관없음(파일명=dag_id 통일이 좋음)
        schedule_interval='10 0 * * *',  # 분 시 일 월 주 -> 매일 0시 0분에
        start_date=pendulum.datetime(2025, 4, 2, tz="Asia/Seoul"),  # DAG가 언제부터 돌지에 대한 설정, tz 한국시간으로 변경
        catchup=False,  # ex) 현재 3/1 , start_date 1/1 -> 사이에 누락된 구간을 돌릴지에 대한 유/무, 순차대로 돌는게 아닌 한번에 실행됨
        tags=['hswoo'],  # 진짜 tag
) as dag:

    @task(
        task_id='task_using_macros',
        templates_dict={
            'start_date': '{{ (date_interval_end.in_timezone("Asia/Seoul")  + macros.datautil.relativedelta.relativedelta(months=-1, days=1)) | ds }}'
            ,
            'end_date': '{{ (data_interval_end.in_timezone("Asia/Seoul").replace( days=1) + macros.datautil.relativedelta.relativedelta(days=-1)) | ds  }}'
        }
    )
    def get_datetime_macro(**kwargs):
        template_dict = kwargs['template_dict']
        if template_dict:
            start_date = template_dict['start_date'] or 'START_DATE 없음'
            end_date = template_dict['end_date'] or 'END_DATE 없음'
            print(start_date)
            print(end_date)


    @task(
        task_id='task_direct_calc'
    )
    def get_datetime_calc(**kwargs):
        from dateutil.relativedelta import relativedelta
        data_interval_end = kwargs['data_interval_end']

        prev_month_day_first = data_interval_end.in_timezone("Asia/Seoul") + relativedelta(months=-1, day=1)
        prev_month_day_last = data_interval_end.in_timezone("Asia/Seoul").replace(day=1) + relativedelta(day=-1)

        print(prev_month_day_first.strftime('%Y-%m-%d'))
        print(prev_month_day_last.strftime('%Y-%m-%d'))


    get_datetime_macro() >> get_datetime_calc()
