import requests

OPENWEATHER_API_KEY = 'd4c7e91f7aa2722e4565c1b98d1ac4fc'

def get_weather():
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'lat': 4.6005,
        'lon': 101.0758,
        'appid': OPENWEATHER_API_KEY,
        'units': 'metric'
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        return {
            'description': data['weather'][0]['description'],
            'temperature': data['main']['temp'],
            'feels_like': data['main']['feels_like'],
        }
    else:
        return {'error': 'Could not fetch weather data.'}