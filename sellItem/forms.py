from django import forms
from sellItem.models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        exclude = []

