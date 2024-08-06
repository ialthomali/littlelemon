from django.test import TestCase
from restaurant import models, serializers
from rest_framework.test import APIClient
from rest_framework import status



class MenuViewTest(TestCase):

    def setUp(self):
        # Create test instances of the Menu model
        self.client = APIClient()
        self.burger = models.Menu.objects.create(title='Burger',price=5, inventory=10)
        self.fries = models.Menu.objects.create(title='Fries',price=1, inventory=10)
        self.pepsi = models.Menu.objects.create(title='Pepsi',price=2, inventory=10)
        self.url = '/restaurant/menu/'  # Adjust the URL if different in your project

    def test_getall(self):
        response = self.client.get(self.url)
        
        expected_data = serializers.MenuSerializer(models.Menu.objects.all(), many=True).data
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_data)