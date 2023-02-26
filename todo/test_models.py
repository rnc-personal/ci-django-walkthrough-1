from django.test import TestCase
from .models import Item

# Create your tests here.


class ItemModelTest(TestCase):

    def test_done_defaults_to_false(self):
        item = Item.objects.create(name='test item')
        self.assertFalse(item.done)

    def test_item_string_method_returns_name(self):
        item = Item.objects.create(name='test item')
        self.assertEqual(str(item), 'test item')
