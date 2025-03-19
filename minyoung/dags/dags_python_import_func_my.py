#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pendulum
from airflow import DAG
import datetime
from airflow.operators.python import PythonOperator
from common.common_func import minyoung


# In[19]:


with DAG (
    dag_id = "dags_python_import_func_my",
    schedule= "00 21 * * *",
    start_date = pendulum.datetime(2025, 3, 19, tz = "Asia/Seoul"),
    catchup=False
) as dag :

    task_get_my = PythonOperator(
        task_id = 'task_get_my',
        python_callable = minyoung
    )

