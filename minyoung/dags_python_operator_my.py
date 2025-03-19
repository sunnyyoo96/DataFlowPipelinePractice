#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pendulum
from airflow import DAG
import datetime
import random
from airflow.operators.python import PythonOperator


# In[3]:


with DAG (
    dag_id = "dags_python_operator_my",
    schedule= "30 20 * * *",
    start_date = pendulum.datetime(2025, 3, 19, tz = "Asia/Seoul"),
    catchup=False
) as dag :
    def select_fruit() : 
        fruit = ['APPLE', 'BANANA', 'ORANGE', 'AVOCADO']
        rand_int = random.randint(0, 3)
        print(fruit[rand_int])

    py_t1 = PythonOperator(
        task_id = 'py_t1',
        python_callable = select_fruit
    )

    py_t1

