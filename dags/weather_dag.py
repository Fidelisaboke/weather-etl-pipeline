# Standard libraries
import requests
from datetime import datetime, timedelta

# Apache Airflow components
from airflow import DAG
from airflow.decorators import task

# Source modules from src folder
from src.constants import CITIES, POSTGRES_CONN_ID, BASE_URL
from src.credentials import load_api_key
from src.etl.extract import fetch_weather_data
from src.etl.transform import clean_weather_data
from src.etl.load import load_to_postgres

API_KEY = load_api_key()

# Default DAG parameters
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 7, 1),
    'retries': 3,
    'retry_delay': timedelta(minutes=5)
}

# DAG Definition
with DAG(
    dag_id='weather_etl_pipeline',
    default_args=default_args,
    schedule='@daily',
    catchup=False
) as dag:
    
    @task()
    def extract_weather_data():
        return fetch_weather_data(CITIES, BASE_URL, API_KEY)
    
    @task()
    def transform_weather_data(city_data_list):
        return clean_weather_data(city_data_list)
    
    @task()
    def load_weather_data(data_list):
        return load_to_postgres(data_list, POSTGRES_CONN_ID)
    
    # Orchestrator
    extracted = extract_weather_data()
    transformed = transform_weather_data(extracted)
    load_weather_data(transformed)
