#!/usr/bin/env python
# coding: utf-8

# In[5]:


from datetime import datetime, timedelta
import pendulum

from airflow import DAG
from airflow.decorators import task
# from airflow.operators.bash import BashOperator   


# In[7]:


with DAG(
    dag_id="dags_python_task_decorator_jh",
    schedule="30 20 * * 5#3", # 분 시 일 월 요일
    start_date=pendulum.datetime(2025, 3, 21, tz="Asia/Seoul"),
    catchup=False,
    tags=["jh_choi"],
) as dag:
    @task(task_id="python_task_1")
    def print_context(some_input):
        print(some_input)

    # *kwargs: 일반적인 인자 나열 방식으로 호출합니다. 예: func(1, 2, 3)
    # **kwargs: 키-값 쌍 형태로 호출합니다. 예: func(a=1, b=2, c=3)    
    
    python_task_1 = print_context("task_decorator 실행")        
        

