from airflow import DAG
import pendulum
import datetime
from airflow.operators.empty import EmptyOperator  # EmptyOperator -> 값이 없는 작업

with DAG(
        dag_id="dags_conn_test_hswoo",
        schedule=None,
        start_date=pendulum.datetime(2025, 3, 18, tz="Asia/Seoul"),
        catchup=False,
) as dag:
    t1 = EmptyOperator(
        task_id='t1',
    )

    t2 = EmptyOperator(
        tast_id='t2',
    )

    t3 = EmptyOperator(
        tast_id='t3',
    )

    t4 = EmptyOperator(
        tast_id='t4',
    )

    t5 = EmptyOperator(
        tast_id='t5',
    )

    t6 = EmptyOperator(
        tast_id='t6',
    )

    t7 = EmptyOperator(
        tast_id='t7',
    )

    t8 = EmptyOperator(
        tast_id='t8',
    )

    t1 >> [t2, t3] >> t4
    t5 >> t4
    [t4, t7] >> t6 >> t8
