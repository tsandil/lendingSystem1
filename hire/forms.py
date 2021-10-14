from django import forms
from hire.models import ItemforHire

class HireForm(forms.ModelForm):
    class Meta:
        model = ItemforHire
        exclude = []

