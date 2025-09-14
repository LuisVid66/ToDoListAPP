from django import forms 
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(label='Nombre de usuario', max_length=150)
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)


class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]

"""
class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
"""