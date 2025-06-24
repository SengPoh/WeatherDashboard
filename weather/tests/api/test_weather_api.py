from django.test import TestCase
from unittest.mock import patch
from weather.api import get_weather


class WeatherAPITest(TestCase):
    """Test suite for weather api"""

    @patch('weather.api.requests.get')
    def test_get_weather_successful(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            'weather': [{'description': 'rainy'}],
            'main': {'temp': 15, 'feels_like': 10}
        }

        result = get_weather("London")

        self.assertEqual(result['description'], 'rainy')
        self.assertEqual(result['temperature'], 15)
        self.assertEqual(result['feels_like'], 10)

    @patch('weather.api.requests.get')
    def test_get_weather_fail(self, mock_get):
        mock_get.return_value.status_code = 500
        mock_get.return_value.json.return_value = {
            'error': 'Could not fetch weather data.'
        }

        result = get_weather("London")

        self.assertEqual(result['error'], 'Could not fetch weather data.')
