#!/usr/bin/env python
# coding: utf-8

# In[7]:


from datetime import datetime, timedelta
import pendulum

from airflow import DAG
from airflow.operators.bash import BashOperator
from dateutil import relativedelta


# In[ ]:


with DAG(
    dag_id='dags_bash_with_macros_jh',
    schedule_interval="50 20 L * *",
    start_date=pendulum.datetime(2025, 4, 2,tz="Asia/Seoul"),
    catchup=False,
) as dag:
    #Start Date : 전월 말일, End Date : 1일전
    bash_task_1 = BashOperator(
        task_id = 'bash_task_1',
        env = {'START_DATE': '{{data_interval_start}}',
              'END_DATE':'{{ data_interval_end + relativedelta.relativedelta(days=-1)}}'},
        bash_command = 'echo "Start_Date:$START_DATE" && echo "END_DATE : $END_DATE"'
    )


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




