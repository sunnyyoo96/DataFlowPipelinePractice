#!/usr/bin/env python
# coding: utf-8

# In[3]:


from datetime import datetime, timedelta
import pendulum

from airflow import DAG
from airflow.operators.bash import BashOperator


# In[ ]:


with DAG(
    dag_id='dags_bash_select_fruit_jh',
    schedule_interval="0 22 * * 2#3",
    start_date=pendulum.datetime(2025, 3, 18,tz="Asia/Seoul"),
    catchup=False,
) as dag:

    t1_apple = BashOperator(
        task_id="t1_apple",
        bash_command="/root/airflow/plugins/select_fruit_jh.sh APPLE",
    )

    t1_apple


# In[ ]:





# In[ ]:





# In[ ]:




