#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from airflow import DAG
import pendulum
import datetime
from airflow.decorators import task


# In[ ]:


with DAG(
    dag_id = "dags_python_show_templates_my",
    schedule = "00 20 * * *",
    start_date = pendulum.datetime(2025, 4, 7, tz = "Asia/Seoul"),
    tags = ['mychoi'],
    catchup = True
) as dag :

    @task(task_id = 'python_task')
    def show_templates(**kwargs):
        from pprint import pprint
        pprint(kwargs)

    show_templates()

