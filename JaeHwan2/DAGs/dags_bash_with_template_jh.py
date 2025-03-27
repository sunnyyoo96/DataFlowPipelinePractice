#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from datetime import datetime, timedelta
import pendulum

from airflow import DAG
from airflow.operators.bash import BashOperator


# In[4]:


from jinja2 import Template


# In[ ]:


with DAG(
    dag_id='dags_bash_with_template_jh',
    schedule_interval="0 22 * * *",
    start_date=pendulum.datetime(2025, 3, 27,tz="Asia/Seoul"),
    catchup=False,
) as dag:

    bash_t1 = BashOperator(
        task_id = "bash_t1",
        bash_command = 'echo "data_interval_end : {{data_interval_end}}"'
    )

    bash_t2 = BashOperator(
        task_id = "bash_t2",
        env={'START_DATE' : '{{data_interval_start | ds}}',
             'END_DATA' : '{{data_interval_end | ds}}' },
        bash_command = 'echo $START_DATE && echo $END_DATE'
    )

    bash_t1 >> bash_t2


# In[ ]:




