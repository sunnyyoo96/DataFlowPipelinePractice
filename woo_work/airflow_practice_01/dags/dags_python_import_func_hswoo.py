import pendulum
from airflow import DAG
from airflow.operators.python import PythonOperator
# airflow 에서는 plugins 폴더를 빼고 이하경로로 써야 에러없이 잘 받아들임
# from plugins. common.common_func_hswoo import get_sftp
from  common.common_func_hswoo import get_sftp

with DAG(
        dag_id='dags_python_import_func_hswoo',
        schedule='30 6 * * *',
        start_date=pendulum.datetime(2025, 3, 19, tz="Asia/Seoul"),
        catchup=False,
) as dag:
    task_get_sftp = PythonOperator(
        task_id='task_get_sftp',
        python_callable=get_sftp,
    )

    task_get_sftp
