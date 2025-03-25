#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from datetime import datetime, timedelta
import pendulum

from airflow import DAG
from airflow.operators.python import PythonOperator
from common.common_func import regist2


# In[ ]:


with DAG(
    dag_id='dags_python_with_op_args_two_jh',
    schedule_interval="30 22 * * *",
    start_date=pendulum.datetime(2025, 3, 25,tz="Asia/Seoul"),
    catchup=False,
) as dag:
    regist_t2_1 = PythonOperator(
        task_id = 'regist_t2_1',
        python_callable = regist2,
        op_args = ['jhchoi','man','kr','seoul'],
        op_kargs = {'email' : 'cjh8523@naver.com','phone':'010-2598-3520'}
    )

    regist_t2


# In[ ]:




