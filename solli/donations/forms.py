from django import forms
from django.core.exceptions import ValidationError

from .models import Donation

input_attrs = {'class': 'border border-gray-300 rounded px-3 py-2 w-full'}

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs=input_attrs),
            'description': forms.Textarea(attrs=input_attrs),
        }
