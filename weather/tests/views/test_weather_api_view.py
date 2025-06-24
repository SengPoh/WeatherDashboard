"""Tests of the weather view."""
from django.test import TestCase
from django.urls import reverse
from unittest.mock import patch
from weather.views import weather_api

class WeatherViewTestCase(TestCase):
    """Tests of the weather api view."""


    def setUp(self):
        self.url = reverse('weather_api')

    def test_weather_url(self):
        self.assertEqual(self.url,'/api/weather/')

    @patch('weather.api.get_weather')
    def test_weather_api_successful(self, mock_get_weather):
        mock_get_weather.return_value = {
            'description': 'rainy',
            'temperature': '10',
            'feels_like': '15',
        }

        response = self.client.get(self.url, params={'city': 'London'})
        self.assertEqual(response.status_code, 200)
        self.assertJsonEqual(
            response.content, 
            {
                'description': 'rainy',
                'temperature': '10',
                'feels_like': '15',
            })