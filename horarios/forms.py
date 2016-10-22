from django.contrib.auth.forms import AuthenticationForm 
from django import forms


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Usuario", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Clave", max_length=30, 
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))

