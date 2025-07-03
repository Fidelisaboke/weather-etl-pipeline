# Weather ETL Data Engineering Pipeline
## Project Overview
This project contains an ETL pipeline that retrieves, transforms, and saves weather data from the OpenWeatherMap API to a PostgreSQL database.

## Installation and Setup
### Pre-requisites
- Python 3.12 or above
- Docker Version 20.10.23 or above
- [OpenWeatherMap API Key](https://openweathermap.org/api)
- [Astro CLI](https://www.astronomer.io/docs/astro/cli/install-cli/)

### Setup Instructions
- Clone the repository:
```bash
https://github.com/Fidelisaboke/weather-etl-pipeline
cd weather-etl-pipeline
```

- Create a Python virtual environment:
```bash
python3 -m venv .venv
```

- Activate the virtual environment:
```bash
source .venv/bin/activate # For Linux/macOS
.venv\Scripts\activate    # For Windows OS
```

- Install the required libraries:
```bash
pip install -r requirements.txt
```

- Install Apache Airflow and the Postgres Provider:
```bash
pip install --upgrade apache-airflow
pip install apache-airflow-providers-postgres
```

- Create a `credentials.txt` file inside the `dags/` directory. Paste your OpenWeatherMap API key in that file.

## Basic Usage
- Start the Astro project:
```bash
astro dev start --verbosity debug
```
This opens an Apache Airflow dashboard at http://localhost:8080

- Ensure you set up a PostgreSQL connection on the dashboard:
1. Go to Admin &rarr; Connections &rarr; Add Connection
2. Set the following properties:
- Connection ID: `postgres_default`
- Connection Type: `postgres`
- Host: copy the name of the postgres container created by the project
- Login: set the postgres username (default: `postgres`)
- Password: set the postgres password (default: `postgres`)
- Port: the port running postgres (default: `5432`)
- Schema: `postgres`
3. Click on `Save` after filling in the details.

## Acknowledgements
- I would like to thank [@stilinsk](https://github.com/stilinsk) and [Phoenix KE Analytics](https://phoenixkeanalytics.com/) for the ETL Data Engineering pipeline session. I got to build my very first data pipeline, based on the knowledge I gained from the session.