#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from datetime import datetime, timedelta
import pendulum
import random

from airflow import DAG
from airflow.operators.python import PythonOperator
from common.common_func_jh import get_sftp


# In[80]:


from common.common_func_jh import get_sftp


# In[ ]:


with DAG(
    dag_id='dags_python_import_func_jh',
    schedule_interval="0 22 * * *",
    start_date=pendulum.datetime(2025, 3, 19,tz="Asia/Seoul"),
    catchup=False,
) as dag:
    task_get_sftp = PythonOperator(
        task_id = 'task_get_sftp',
        python_callable = get_sftp
    )

