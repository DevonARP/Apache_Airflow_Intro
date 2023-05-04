from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.subdag import SubDagOperator
from subdags.subdag_downloads import subdag_downloads
from subdags.subdag_transforms import subdag_transforms
from groups.groups_downloads import downloads_tasks
from groups.groups_transforms import transforms_tasks
 
from datetime import datetime
 
with DAG('group_dag', start_date=datetime(2022, 1, 1), 
    schedule_interval='@daily', catchup=False) as dag:

    args = {'start_date':dag.start_date, 'schedule_interval': dag.schedule_interval, 'catchup':dag.catchup}
 
    downloads = downloads_tasks()

    transforms = transforms_tasks()
 
    check_files = BashOperator(
        task_id='check_files',
        bash_command='sleep 10'
    )

 
    downloads >> check_files >> transforms