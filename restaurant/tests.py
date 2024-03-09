from django.test import TestCase
from .models import Menu

# Create your tests here.
class MenuTest(TestCase):
    def setUp(self):
        self.item1 = Menu.objects.create(title='Coffee', price=2.5, menu_item_description="Ground Coffee", inventory=10)

    def test_get_item(self):
        item = Menu.objects.get(title='Coffee')
        self.assertEqual(str(item), 'Coffee: 2.50')
