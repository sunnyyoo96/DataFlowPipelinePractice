from airflow import DAG
import pendulum
import datetime
from airflow.operators.python import PythonOperator
from common.common_func import regist

with DAG(
        dag_id='dags_python_with_op_args_hswoo',
        schedule='30 20 * * *',
        start_date=pendulum.datetime(2025, 3, 25, tz='Asia/Seoul'),
        catchup=False,
        tags=['hswoo'],
) as dag:
    regist_t1 = PythonOperator(
        task_id='regist_t1',
        python_callable=regist,
        op_args=['hswoo', 'man', 'kr', 'seoul']
    )

    regist_t1
