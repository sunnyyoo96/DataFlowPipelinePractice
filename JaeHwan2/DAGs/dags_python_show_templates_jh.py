#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from datetime import datetime, timedelta
import pendulum

from airflow import DAG
from airflow.operators.bash import BashOperator
from jinja2 import Template
from airflow.decorators import task


# In[ ]:


with DAG(
    dag_id='dags_python_show_templates_jh',
    schedule_interval="0 20 * * *",
    start_date=pendulum.datetime(2025, 3, 30,tz="Asia/Seoul"),
    catchup=True,
) as dag:

    @task(task_id='python_task')
    def show_templates(**kwargs):
        from pprint import pprint
        pprint(kwargs)

    show_templates()

