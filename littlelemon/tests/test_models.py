from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(Title="IceCream", Price=80, Inventory=100)
        
        anticipated_value = "IceCream : 80"
        self.assertEqual(str(item), anticipated_value, f"Expected {anticipated_value}, but got {str(item)}")