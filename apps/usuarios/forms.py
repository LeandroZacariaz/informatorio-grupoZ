from django import forms

from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class RegistroForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={
        "type":"email",
        "required": "true"
    }), label="Email")
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        "type":"text",
        "required": "true"
    }), label="Nombre")
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        "type":"text",
        "required": "true"
    }), label="Apellido")
    username =forms.CharField(widget=forms.TextInput(attrs={
        "type":"text",
        "required": "true"
    }), label="Usuario")
    password1 = forms.CharField(widget=forms.TextInput(attrs={
        "type":"password",
        "required": "true"
    }), label="Contraseña")
    password2 = forms.CharField(widget=forms.TextInput(attrs={
        "type":"password",
        "required": "true"
    }), label="Confirmar-Contraseña")

    class Meta:
        model = Usuario
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2'
        ]