from django import forms
from django.core.exceptions import ValidationError

from .models import Donation

input_attrs = {'class': 'border border-gray-300 rounded px-3 py-2 w-full'}


class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['title', 'description', 'category', 'location']
        widgets = {
            'title': forms.TextInput(attrs=input_attrs),
            'description': forms.Textarea({
                'class': 'rounded w-full h-32 p-2 border border-gray-300 ',
                'rows': 4,
            }),
            'category': forms.Select(attrs=input_attrs),

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Inserir uma opção vazia no início para simular placeholder
        self.fields['category'].empty_label = 'Selecione a categoria'