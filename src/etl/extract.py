import requests


def fetch_weather_data(cities: list, base_url: str, api_key: str) -> list:
    """Get the weather data from the API endpoint."""
    weather_data = []
    for city in cities:
        # Query parameters
        params = {
            'q': city,
            'appid': api_key,
            'units': 'metric'
        }
        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            data = response.json()
            weather_data.append((city, data))
        else:
            raise Exception(f"Faled to fetch data for {city}. Status code: {response.status_code}")
        
    return weather_data
