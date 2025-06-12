from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate

from .models import User
from .utils import validate_cnpj

input_attrs = {'class': 'border border-gray-300 rounded px-3 py-2 w-full'}


class CustomUserCreationForm(UserCreationForm):
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

    is_company = forms.BooleanField(
        required=False,
        label='É uma empresa?',
        widget=forms.CheckboxInput(attrs={'class': 'mr-2'})
    )

    class Meta:
        model = User
        fields = ['full_name', 'email','is_company' ,'cnpj','password1', 'password2']

        widgets = {
            'full_name': forms.TextInput(attrs=input_attrs),
            'email': forms.EmailInput(attrs=input_attrs),

        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        print("Validando email:", email)
        if User.objects.filter(email=email).exists():
            raise ValidationError('Este email já está cadastrado.')
        return email

    def clean_cnpj(self):
        cnpj = self.cleaned_data.get('cnpj')
        is_company = self.cleaned_data.get('is_company')

        if is_company:
            if not cnpj:
                raise ValidationError('CNPJ é obrigatório para empresas.')
            cnpj_numbers = ''.join(filter(str.isdigit, cnpj))

            if not validate_cnpj(cnpj_numbers):
                raise ValidationError('CNPJ inválido.')

            if User.objects.filter(cnpj=cnpj_numbers).exists():
                raise ValidationError('Este CNPJ já está cadastrado.')

            return cnpj_numbers
        else:
            return None

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)

        # Define o username como o email
        user.username = user.email

        # Define is_company como True se cnpj foi informado
        user.is_company = bool(self.cleaned_data.get('cnpj'))

        cnpj = self.cleaned_data.get('cnpj')

        # Salva o cnpj só se for empresa
        if user.is_company:
            user.cnpj = cnpj
        else:
            user.cnpj = None

        if commit:
            user.save()
        return user


class CustomUserLoginForm(forms.Form):
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={
            'class': 'border border-gray-300 rounded px-3 py-2 w-full',
            'placeholder': 'Digite seu email'
        })
    )
    password = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={
            'class': 'border border-gray-300 rounded px-3 py-2 w-full',
            'placeholder': 'Digite sua senha'
        })
    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if email and password:
            user = authenticate(username=email, password=password)
            if user is None:
                raise ValidationError("Email ou senha inválidos.")
            if not user.is_active:
                raise ValidationError("Essa conta está desativada.")
            cleaned_data['user'] = user

        return cleaned_data
