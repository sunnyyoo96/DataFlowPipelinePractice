#!/usr/bin/env python
# coding: utf-8

# In[3]:


from datetime import datetime, timedelta
import pendulum

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.dummy import DummyOperator


# In[5]:


with DAG(
    dag_id='dex_bash_operator_jh',
    schedule_interval='0 0 * * *', # 분 시 일 월 주
    start_date=pendulum.datetime(2025, 3, 1,tz="Asia/Seoul"),
    catchup=False,
    # dagrun_timeout=datetime.timedelta(minutes=60),
    # tags=['ChoiJaeHwanLOVE', 'example2'],
    # params={"example_key": "example_value"},
) as dag:
    bash_t1 = BashOperator(
        task_id='bash_t1',
        bash_command='echo JaeHwanZZANG',
    )
    bash_t2 = BashOperator(
        task_id='bash_t2',
        bash_command='echo $HOSTNAME,
    )
    bash_t1 >> bash_t2


# In[ ]:




