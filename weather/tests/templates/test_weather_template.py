from django.test import TestCase
from django.urls import reverse
from weather.models import User

class WeatherTemplateTest(TestCase):
    """Tests of the weather template."""

    fixtures = ['weather/tests/fixtures/default_user.json']
    def setUp(self):
        self.url = reverse('weather')
        self.user = User.objects.get(username='@johndoe')


    def test_javascript_included(self):
        self.client.login(username=self.user.username, password='Password123')
        response = self.client.get(self.url)
        self.assertContains(response, 'function getWeather()')
        self.assertContains(response, 'fetch(`/api/weather/?city=${encodeURIComponent(city)}`)')
