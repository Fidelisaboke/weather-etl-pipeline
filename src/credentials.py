def load_api_key():
    """Load API key from credentials.txt"""
    with open('/usr/local/airflow/dags/credentials.txt', 'r') as f:
        return f.read().strip()
    