from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    username = forms.CharField(max_length=125)
    password = forms.CharField(max_length=125,widget=forms.PasswordInput)


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
