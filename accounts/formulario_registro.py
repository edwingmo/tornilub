from django import forms
from .models import User
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox

import accounts

class formularioRegistro(forms.Form):
    class Meta:
        model = accounts
        fields = ("name", "apellido", "username", "email","password", "confirm_password")

    name = forms.CharField(max_length=15,  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'nombre', 'id':'name'}))
    apellido = forms.CharField(max_length=15,  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'apellido', 'id':'apellido'}))
    username = forms.CharField(max_length=20,  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'user123', 'id':'username'}))
    email = forms.EmailField(max_length=40,  widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'ej@gmail.com' ,'id':'email'}))
    password = forms.CharField(max_length=20,  widget=forms.PasswordInput(attrs={'class': 'form-control', 'id':'password'}))
    confirm_password = forms.CharField(max_length=20,  widget=forms.PasswordInput(attrs={'class': 'form-control', 'id':'confirm_password'}))
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)


    def clean(self):
        cleaned_data = super(formularioRegistro, self).clean() #Importante el clean es para obetener valores del formulario
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        email = cleaned_data.get('email')
        username = cleaned_data.get('username')
        name = cleaned_data.get('name')
        apellido = cleaned_data.get('apellido')
        captcha = cleaned_data.get('captcha')

        if not name.isalpha():
            raise forms.ValidationError('El nombre contiene numeros o caracteres especiales')

        if not apellido.isalpha():
            raise forms.ValidationError('El apellido contiene numeros o caracteres especiales')

        if password != confirm_password:
            raise forms.ValidationError('Password no coincide')
        
        if len(password) <= 5:
            raise forms.ValidationError('Password muy corto, debe ser de 6 o mas caracteres')

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email ya existe.')

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('El nombre de usuario ya existe.')

        if captcha == None:
            raise forms.ValidationError('Por favor completa el recapcha')


        
        