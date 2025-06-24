import requests

OPENWEATHER_API_KEY = 'd4c7e91f7aa2722e4565c1b98d1ac4fc'

def get_weather(city):
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'lat' = '4.6005',
        'lon' = '101.0758',
        'apiid' = OPENWEATHER_API_KEY
        'unit' = 'metric'
    }

    response = request.get(url, params=params)

    if response.status_code == 200:
        data = response.json
        return {
            'weather' = response.content['weather.id']
        }