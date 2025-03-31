#!/usr/bin/env python
# coding: utf-8

# In[1]:


from airflow import DAG
import pendulum
import datetime
from airflow.operators.python import PythonOperator
from airflow.decorators import task


# In[6]:


with DAG(
    dag_id = "dags_python_template_my",
    schedule = "00 21 * * *",
    start_date = pendulum.datetime(2025, 3, 31, tz = "Asia/Seoul"),
    catchup = False,
    tags = ['mychoi']
) as dag :
    def python_function1(start_date, end_date, **kwargs):
        print(start_date)
        print(end_date)

    python_t1 = PythonOperator(
        task_id = 'python_t1',
        python_callable = python_function1,
        op_kwargs = {'start_date' : '{[data_interval_start | ds}}', 'end_date' : '{{data_interval_end | ds}}'}
    )

    @task(task_id = 'python_t2')
    def python_function2(**kwargs):
        print(kwargs)
        print('ds : ' + kwargs['ds'])
        print('ts : ' + kwargs['ts'])
        print('data_interval_start : ' +str(kwargs['data_interval_start']))
        print('data_interval_end : ' +str(kwargs['data_interval_end']))
        print('task_instance : ', str(kwargs['t1']))

    python_t1 >> python_function2()


# In[ ]:




