{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "5730bfbd-944a-4a59-a4a4-da0e97b3d16c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\"><span style=\"color: #808000; text-decoration-color: #808000; font-weight: bold\">C:\\Users\\JaeHwan\\AppData\\Local\\Temp\\ipykernel_2188\\</span><span style=\"color: #808000; text-decoration-color: #808000; font-weight: bold\">2091552509.</span><span style=\"color: #808000; text-decoration-color: #808000; font-weight: bold\">py:</span><span style=\"color: #808000; text-decoration-color: #808000; font-weight: bold\">6</span><span style=\"color: #808000; text-decoration-color: #808000; font-weight: bold\"> DeprecationWarning</span><span style=\"color: #808000; text-decoration-color: #808000\">: The `airflow.operators.dummy.DummyOperator` class is deprecated. Please use `</span><span style=\"color: #808000; text-decoration-color: #808000\">'airflow.operators.empty.EmptyOperator'</span><span style=\"color: #808000; text-decoration-color: #808000\">`.</span>\n",
       "</pre>\n"
      ],
      "text/plain": [
       "\u001b[1;33mC:\\Users\\JaeHwan\\AppData\\Local\\Temp\\ipykernel_2188\\\u001b[0m\u001b[1;33m2091552509.\u001b[0m\u001b[1;33mpy:\u001b[0m\u001b[1;33m6\u001b[0m\u001b[1;33m DeprecationWarning\u001b[0m\u001b[33m: The `airflow.operators.dummy.DummyOperator` class is deprecated. Please use `\u001b[0m\u001b[33m'airflow.operators.empty.EmptyOperator'\u001b[0m\u001b[33m`.\u001b[0m\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "from datetime import datetime, timedelta\n",
    "import pendulum\n",
    "\n",
    "from airflow import DAG\n",
    "from airflow.operators.bash import BashOperator\n",
    "from airflow.operators.dummy import DummyOperator"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "614577d0-7919-4466-a733-f3846178e510",
   "metadata": {},
   "outputs": [
    {
     "ename": "IndentationError",
     "evalue": "expected an indented block (3105781448.py, line 9)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Cell \u001b[1;32mIn[5], line 9\u001b[1;36m\u001b[0m\n\u001b[1;33m    ) as dag:\u001b[0m\n\u001b[1;37m             ^\u001b[0m\n\u001b[1;31mIndentationError\u001b[0m\u001b[1;31m:\u001b[0m expected an indented block\n"
     ]
    }
   ],
   "source": [
    "with DAG(\n",
    "    dag_id='dex_bash_operator_jh',\n",
    "    schedule_interval='0 0 * * *', # 분 시 일 월 주\n",
    "    start_date=pendulum.datetime(2025, 3, 1,tz=\"Asia/Seoul\"),\n",
    "    catchup=False,\n",
    "    # dagrun_timeout=datetime.timedelta(minutes=60),\n",
    "    # tags=['ChoiJaeHwanLOVE', 'example2'],\n",
    "    # params={\"example_key\": \"example_value\"},\n",
    ") as dag:\n",
    "    bash_t1 = BashOperator(\n",
    "        task_id='bash_t1',\n",
    "        bash_command='echo JaeHwanZZANG',\n",
    "    )\n",
    "    bash_t2 = BashOperator(\n",
    "        task_id='bash_t2',\n",
    "        bash_command='echo $HOSTNAME,\n",
    "    )\n",
    "    bash_t1 >> bash_t2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3d87c16e-c574-44c8-935d-cbea56561799",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "data_flow_kernel",
   "language": "python",
   "name": "data_flow"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.21"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
