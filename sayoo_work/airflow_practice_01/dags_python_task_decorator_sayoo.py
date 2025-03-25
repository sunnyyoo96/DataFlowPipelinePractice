from __future__ import annotations

import logging
import sys
import time
from pprint import pprint

import pendulum
from airflow import DAG
from airflow.decorators import dag, task


with DAG(
    dag_id="example_python_task_decorator_sayoo",
    schedule= "30 20 * * 5#3",  ## 셋째주 금요일 8시 30분 분 시 일 월 요일
    start_date=pendulum.datetime(2025, 3, 21, tz="UTC"),
    catchup=False,
    tags=["sayoo"],
):
    # @task(task_id="python_task_1_sayoo")
    # def print_context(ds=None, **kwargs):  ## default 인자값 None , **keyword argument
    #     """
    #     *args: 일반적인 인자 나열 방식으로 호출합니다. 예: func(1, 2, 3)
    #     **kwargs: 키-값 쌍 형태로 호출합니다. 예: func(a=1, b=2, c=3)
    #     Print the Airflow context and ds variable from the context."""
    #     pprint(kwargs)
    #     print(ds)
    #     return "Whatever you return gets printed in the logs"
    #     인자 형식
    #     *args : tuple index 통해서 접근 - args[0], args[1]
    #     **kwargs : key-value 형태 Ex) name='hjkim' country='kr'
    #     kwargs.get('name') or ''    없다면 None


    @task(task_id="python_task_1_sayoo")
    def print_context(some_input):
        print(some_input)

    python_task_1_sayoo = print_context('task_decorator 실행')
