#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from datetime import datetime, timedelta
import pendulum

from airflow import DAG
from airflow.operators.email import EmailOperator


# In[ ]:


with DAG(
    dag_id='dags_email_operator_jh',
    schedule_interval="0 20 1 * *",
    start_date=pendulum.datetime(2025, 3, 19,tz="Asia/Seoul"),
    catchup=False,
) as dag:
    send_email_task = EmailOperator(
        task_id = "send_email_task",
        to = "cjh35201@gmail.com",
        subject = "Airflow 성공메일",
        html_content = "Airflow 작업이 완료되었습니다."
    )


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




