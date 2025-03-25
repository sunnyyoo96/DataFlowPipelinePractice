from airflow import DAG
import pendulum
import datetime
from airflow.operators.python import PythonOperator
from common.common_func import regist2
with DAG(
    dag_id="dags_python_with_op_kargs_sayoo",
    schedule= "30 6 * * 2#4",  ##
    start_date=pendulum.datetime(2025, 3, 25, tz="UTC"),
    catchup=False,
    tags=["sayoo"],
):
    regist_t2 = PythonOperator(
        task_id="regist_t2_sayoo",
        python_callable = regist2,
        op_args=["sayoo","girl","kr","Dongtan"],
        op_kwargs={
                  'email':'y4380@naver.com',
                  'address' : '유림 노르웨이 숲'
        }
    )
    # *BranchPythonOperator: task를
    # 선택적으로 실행(분기 처리)
    regist_t2

