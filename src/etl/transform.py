from datetime import datetime


def clean_weather_data(weather_data: list):
    """Clean and format the weather data."""
    transformed_data = []
    for city, data in weather_data:
        main = data['main']
        wind = data['wind']
        sys = data['sys']
        weather_code = data['weather'][0]['id']
        now = datetime.now()

        # Clean python dictionary of every city's weather
        transformed_data.append({
            'city': city,
            'temperature': main['temp'],
            'feelsLike': main['feels_like'],
            'minimumTemp': main['temp_min'],
            'maximumTemp': main['temp_max'],
            'pressure': main['pressure'],
            'humidity': main['humidity'],
            'windspeed': wind['speed'],
            'winddirection': wind.get('deg', 0),
            'weathercode': weather_code,
            'timeRecorded': now,
            'sunrise': datetime.fromtimestamp(sys['sunrise']),
            'sunset': datetime.fromtimestamp(sys['sunset'])
        })

    return transformed_data
