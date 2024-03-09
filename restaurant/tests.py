from django.test import TestCase
from .models import Menu

# Create your tests here.
class MenuTest(TestCase):
    def setUp(self):
        self.item1 = Menu.objects.create(title="Coffee", price=2.50, menu_item_description="Ground Coffee", inventory=10)
        self.item2 = Menu.objects.create(title="Capreze Salad", price=12.50, menu_item_description="", inventory=10)

    def test_get_item(self):
        item = Menu.objects.get(title="Coffee")
        item_str = item.get_item()
        self.assertEqual(item_str, 'Coffee: 2.50')

    def test_items_count(self):
        items = Menu.objects.all()
        self.assertEqual(items.count(), 2)

    