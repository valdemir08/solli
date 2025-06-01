from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from .models import User
from .utils import validate_cnpj

input_attrs = {'class': 'border border-gray-300 rounded px-3 py-2 w-full'}


class CustomUserForm(UserCreationForm):
    # os campos password1 e password2 vêm do UserCreationForm.
    # não é possível estilizar esses campos via Meta.widgets,
    # então eles são redefinidos aqui para aplicar a estilização personalizada.

    password1 = forms.CharField(
        label='Senha',
        strip=False,
        widget=forms.PasswordInput(
            attrs={'class': 'border border-gray-300 rounded px-3 py-2 w-full', 'autocomplete': 'new-password'}),
        help_text='Use uma senha com no mínimo 8 caracteres.'
    )
    password2 = forms.CharField(
        label='Confirme a Senha',
        strip=False,
        widget=forms.PasswordInput(
            attrs={'class': 'border border-gray-300 rounded px-3 py-2 w-full', 'autocomplete': 'new-password'}),
        help_text='Digite a mesma senha para confirmação.'
    )

    cnpj = forms.CharField(
        label='CNPJ',
        max_length=20,
        widget=forms.TextInput(attrs=input_attrs),
        required=False
    )

    class Meta:
        model = User
        fields = ['full_name', 'email','cnpj','password1', 'password2']

        widgets = {
            'full_name': forms.TextInput(attrs=input_attrs),
            'email': forms.EmailInput(attrs=input_attrs),

        }

    def clean_cnpj(self):
        cnpj = self.cleaned_data.get('cnpj', '').strip()

        # Se usuário marcou ser empresa (cnpj preenchido), valida o CNPJ
        if cnpj:
            if not validate_cnpj(cnpj):
                raise ValidationError("CNPJ inválido.")
        return cnpj

    def save(self, commit=True):
        user = super().save(commit=False)

        # Define o username como o email
        user.username = user.email

        # Define is_company como True se cnpj foi informado
        user.is_company = bool(self.cleaned_data.get('cnpj'))

        # Salva o cnpj só se for empresa
        if user.is_company:
            user.cnpj = self.cleaned_data['cnpj']
        else:
            user.cnpj = ''  # ou None, se preferir

        if commit:
            user.save()
        return user
