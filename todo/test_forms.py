from django.test import TestCase
from .forms import ItemForm

# Create your tests here.


class ItemFormTest(TestCase):
    def test_item_name_is_required(self):
        # Test Submit a form with no name?
        form = ItemForm({'name': ''}) 
        # Form is not valid
        self.assertFalse(form.is_valid())
        # Return the error message
        self.assertIn('name', form.errors.keys())
        # Extra, is the error message that appears correct?
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_done_field_is_not_required(self):
        form = ItemForm({'name': 'Testing Done Checkbox'})
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_meta_class(self):
        form = ItemForm()
        self.assertEqual(form.Meta.fields, ['name', 'done'])