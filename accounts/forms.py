from django import forms
from django.contrib.auth.models import User

class SiginInUserForm(forms.Form):
    username = forms.CharField(max_length=50, widget=(forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Enter username"
    })))
    password = forms.CharField(widget=(forms.PasswordInput(attrs={
        "class": "form-control",
        "placeholder": "Enter password"
    })))
