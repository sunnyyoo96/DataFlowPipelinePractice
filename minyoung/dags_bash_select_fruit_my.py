#!/usr/bin/env python
# coding: utf-8

# In[2]:


from airflow import DAG
import pendulum
import datetime
from airflow.operators.bash import BashOperator


# In[3]:


with DAG (
    dag_id = "dags_bash_select_fruit_my",
    schedule= "00 22 * * 2#3",
    start_date = pendulum.datetime(2025, 3, 18, tz = "Asia/Seoul"),
    catchup=False
) as dag :

    t1_grape = BashOperator(
        task_id = "t1_grape",
        bash_command = "/root/airflow/plugins/select_fruit_my.sh GRAPE",
    )

    t1_grape
    

