from airflow.providers.postgres.hooks.postgres import PostgresHook


def load_to_postgres(data_list: list, conn_id: str):
    pg_hook = PostgresHook(postgres_conn_id=conn_id)
    conn = pg_hook.get_conn()
    cursor = conn.cursor()

    # Create a table if it doesn't exist
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS weather_data (
        city VARCHAR(255) PRIMARY KEY,
        temperature FLOAT,
        feelsLike FLOAT,
        minimumTemp FLOAT,
        maximumTemp FLOAT,
        pressure INT,
        humidity INT,
        windspeed FLOAT,
        winddirection FLOAT,
        weathercode INT,
        timeRecorded TIMESTAMP,
        sunrise TIMESTAMP,
        sunset TIMESTAMP
    );
    """)

    # Upsert operation - Insert or update
    for data in data_list:
        cursor.execute("""
        INSERT INTO weather_data (
            city, temperature, feelsLike, minimumTemp, maximumTemp,
            pressure, humidity, windspeed, winddirection, weathercode,
            timeRecorded, sunrise, sunset
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (city) DO UPDATE SET
            temperature = EXCLUDED.temperature,
            feelsLike = EXCLUDED.feelsLike,
            minimumTemp = EXCLUDED.minimumTemp,
            maximumTemp = EXCLUDED.maximumTemp,
            pressure = EXCLUDED.pressure,
            humidity = EXCLUDED.humidity,
            windspeed = EXCLUDED.windspeed,
            winddirection = EXCLUDED.winddirection,
            weathercode = EXCLUDED.weathercode,
            timeRecorded = EXCLUDED.timeRecorded,
            sunrise = EXCLUDED.sunrise,
            sunset = EXCLUDED.sunset;
        """, (
            data['city'], data['temperature'], data['feelsLike'],
            data['minimumTemp'], data['maximumTemp'], data['pressure'],
            data['humidity'], data['windspeed'], data['winddirection'],
            data['weathercode'], data['timeRecorded'], data['sunrise'],
            data['sunset']
        ))

    # Finalise transaction and close connection
    conn.commit()
    cursor.close()
    conn.close()
    