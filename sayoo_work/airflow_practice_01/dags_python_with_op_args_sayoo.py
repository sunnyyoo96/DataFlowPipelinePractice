from airflow import DAG
import pendulum
import datetime
from airflow.operators.python import PythonOperator
from common.common_func import regist
with DAG(
    dag_id="dags_python_with_pi_args_sayoo",
    schedule= "30 6 * * 2#4",  ##
    start_date=pendulum.datetime(2025, 3, 25, tz="UTC"),
    catchup=False,
    tags=["sayoo"],
):
    regist_t1 = PythonOperator(
        task_id="regist_t1_sayoo",
        python_callable=regist,
        op_args=['sayoo','girl','kr','Dongtan']
    )
    # *BranchPythonOperator: task를
    # 선택적으로 실행(분기 처리)
    regist_t1

