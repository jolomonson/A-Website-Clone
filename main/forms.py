from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(forms.ModelForm):
    username = forms.CharField(label='Enter Username', max_length=100)
    password = forms.CharField(label='Enter Password', max_length=100, widget=forms.PasswordInput)