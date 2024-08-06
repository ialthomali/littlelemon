from django.test import TestCase
from restaurant import models

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = models.Menu.objects.create(title='IceCream',price=80, inventory=10)
        self.assertEqual(item.__str__(),"IceCream : 80")