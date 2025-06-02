from django import forms
from .models import Location
from core.models import Image

input_attrs = {'class': 'border border-gray-300 rounded px-3 py-2 w-full'}

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['estate', 'city']
        widgets = {
            'estate': forms.Select(attrs=input_attrs),
            'city': forms.TextInput(attrs=input_attrs),
        }

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image']
        widgets = {
            'image': forms.ClearableFileInput(attrs=input_attrs),
        }
