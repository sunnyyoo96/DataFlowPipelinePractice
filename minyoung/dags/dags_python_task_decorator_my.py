#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pendulum
from airflow import DAG
import datetime
import random
from airflow.decorators import task


# In[5]:


with DAG(
    dag_id = "dags_python_task_decorator_my",
    schedule= "30 20 * * 5#3",  #분시일월요일
    start_date = pendulum.datetime(2025, 3, 21, tz = "Asia/Seoul"),
    catchup=False
) as dag :
    @task(task_id = "python_task_1")
    def print_context(some_input):  
        #ds=None=>default값이 None이다.
        ##**kwargs: 키-값 쌍 형태로 호출합니다.
        print(some_input)

    python_task_1 = print_context('task_decorator 실행')

