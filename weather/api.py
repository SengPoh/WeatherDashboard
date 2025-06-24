import requests

OPENWEATHER_API_KEY = 'd4c7e91f7aa2722e4565c1b98d1ac4fc'

def get_weather(city):
    url = 'https://api.openweathermap.org/data/2.5/weather'

    city_data = get_coord(city)
    if 'error' in city_data:
        return {'error': city_data['error']}

    print(city_data)
    params = {
        'lat': city_data['lat'],
        'lon': city_data['lon'],
        'appid': OPENWEATHER_API_KEY,
        'units': 'metric'
    }

    print(params)

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        return {
            'city': city_data,
            'description': data['weather'][0]['description'],
            'temperature': data['main']['temp'],
            'feels_like': data['main']['feels_like'],
        }
    else:
        return {'error': f'Could not fetch weather data for {city}.'}

def get_coord(city):
    url = "http://api.openweathermap.org/geo/1.0/direct"
    params = {
        'q': city,
        'appid': OPENWEATHER_API_KEY
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        city_data = data[0]
        result = {
            'name': city_data['name'],
            'country': city_data['country'],
            'lat': city_data['lat'],
            'lon': city_data['lon'],
        }
        if 'state' in city_data:
            result['state'] = city_data['state']

        return result
    else:
        return {'error': f'Could not find {city}'}