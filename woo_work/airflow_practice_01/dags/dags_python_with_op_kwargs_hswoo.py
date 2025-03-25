from airflow import DAG
import pendulum
import datetime
from airflow.operators.python import PythonOperator
from common.common_func import regist2

with DAG(
        dag_id='dags_python_with_op_kwargs_hswoo',
        schedule='30 20 * * *',
        start_date=pendulum.datetime(2025, 3, 25, tz='Asia/Seoul'),
        catchup=False,
        tags=['hswoo'],
) as dag:
    regist2_t1 = PythonOperator(
        task_id='regist2_t1',
        python_callable=regist2,
        op_args=['hswoo', 'man', 'kr', 'seoul'],
        op_kwargs={'email' : 'hswoo@gmail.com', 'phone': '010'}
    )

    regist2_t1
