from django import forms
from .models import Location, BaseEntryCategory
from core.models import Image

input_attrs = {'class': 'border border-gray-300 rounded px-3 py-2 w-full'}

class LocationForm(forms.ModelForm):
    #city = forms.ChoiceField(choices=[], widget=forms.Select(attrs=input_attrs))
    city = forms.ModelChoiceField(
        queryset=Location.objects.none(),
        widget=forms.Select(attrs=input_attrs),
        empty_label="Selecione uma cidade"
    )
    class Meta:
        model = Location
        fields = ['estate', 'city']
        widgets = {
            'estate': forms.Select(attrs=input_attrs),

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['estate'].choices = [('', 'Selecione um estado')] + list(self.fields['estate'].choices)[1:]

        if 'estate' in self.data:
            estate = self.data.get('estate')
            self.fields['city'].queryset = Location.objects.filter(estate=estate).order_by('city')
            self.fields['city'].widget.attrs.pop('disabled', None)  # habilita o select
        else:
            self.fields['city'].queryset = Location.objects.none()
            self.fields['city'].widget.attrs['disabled'] = True

    def save(self, commit=True):
        instance = super().save(commit=False)
        # city é o objeto Location selecionado no form, então basta fazer:
        instance = self.cleaned_data['city']  # essa é a Location correta

        # Aqui você retorna a Location, pois o form não está criando a Donation ainda
        # A associação com Donation deve acontecer na view que usa esse form
        return instance


class BaseEntryCategoryForm(forms.ModelForm):
    class Meta:
        model = BaseEntryCategory
        fields = ['name']
        widgets = {
            'name': forms.Select(attrs=input_attrs),
        }


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image']
        widgets = {
            'image': forms.ClearableFileInput(attrs=input_attrs),
        }
