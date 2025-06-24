"""Tests of the weather view."""
from django.test import TestCase
from django.urls import reverse
from weather.models import User

class WeatherViewTestCase(TestCase):
    """Tests of the weather view."""

    fixtures = ['weather/tests/fixtures/default_user.json']

    def setUp(self):
        self.url = reverse('weather')
        self.user = User.objects.get(username='@johndoe')

    def test_weather_url(self):
        self.assertEqual(self.url,'/weather/')

    def test_get_weather(self):
        self.client.login(username=self.user.username, password='Password123')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'weather.html')