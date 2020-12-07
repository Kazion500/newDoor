from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class ProfileRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-auth", 'placeholder': 'Enter Your Username'})
    )
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={"class": "form-auth", 'placeholder': 'Enter Your E-mail Address'})
    )
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={"class": "form-auth", 'placeholder': 'Enter Your Password'})
    )
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={"class": "form-auth", 'placeholder': 'Confirm Your Password'})
    )
    # country = CountryField(blank_label='(Select country)').formfield(
    #     widget=CountrySelectWidget(attrs={"class": "form-auth"})
    # )
    city = forms.CharField(widget=forms.TextInput(
        attrs={'class': "form-auth", 'placeholder': 'Enter Your city'}
    ))

    class Meta:
        model = User
        fields = ['username', 'email','city', 'password1', 'password2']


class RegisterUserForm(forms.Form):
    username = forms.CharField(max_length=50, widget=(forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Enter username"
    })))
    password = forms.CharField(widget=(forms.PasswordInput(attrs={
        "class": "form-control",
        "placeholder": "Enter password"
    })))
