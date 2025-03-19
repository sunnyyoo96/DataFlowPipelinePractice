#!/usr/bin/env python
# coding: utf-8

# In[1]:


from airflow import DAG
import pendulum
import datetime
from airflow.operators.email import EmailOperator


# In[4]:


with DAG (
    dag_id = "dags_email_operator_my",
    schedule= "0 20 19 * *",
    start_date = pendulum.datetime(2025, 3, 19, tz = "Asia/Seoul"),
    catchup=False,
) as dag :
    send_email_task = EmailOperator(
        task_id = 'send_email_task',
        to='minyoung3578@gmail.com',
        subject = 'Airflow 성공메일',
        html_content = "Airflow 테스트"
    )

