from django.test import TestCase
from restaurant.models import Menu
from rest_framework.test import APIClient
from rest_framework import status
from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        # Add a few test instances of the Menu model in the setup
        Menu.objects.create(Title="Dish1", Price=10, Inventory=20)
        Menu.objects.create(Title="Dish2", Price=15, Inventory=25)
        Menu.objects.create(Title="Dish3", Price=20, Inventory=30)

    def test_getall(self):
        # Retrieve all Menu objects
        client = APIClient()
        response = client.get('/restaurant/booking/menu/') 

        # Check if the request was successful (status code 200)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Serialize the Menu objects
        serialized_data = MenuSerializer(Menu.objects.all(), many=True).data

        # Check if the extracted data equals the expected serialized data
        self.assertEqual(response.data, serialized_data)