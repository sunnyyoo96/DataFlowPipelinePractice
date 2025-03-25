#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from airflow import DAG
import pendulum
import datetime
from airflow.operators.python import PythonOperator
from common.common_func import regist2


# In[ ]:


with DAG(
    dag_id = "dags_python_with_op_kwargs_my",
    schedule = "10 21 * * *",
    start_date = pendulum.datetime(2025, 3, 25, tz="Asia/Seoul"),
    tags = ['mychoi'],
    catchup=False
) as dag:

    regist2_t1 = PythonOperator(
        task_id = 'regist2_t1',
        python_callable = regist2,
        op_args = ['mychoi', 'woman', 'kr', 'seoul'],
        op_kwargs = {'email' : 'choimy3578@naver.com', 'phone' : '010-9472-3078'}
    )

    regist2_t1

