from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        # This takes the field definitions / types from the model
        fields = ['name', 'done']
        # Here we are just picking out the fields that we want to use