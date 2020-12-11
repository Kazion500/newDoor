from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class ProfileRegistrationForm(UserCreationForm):

    MARITAL_STATUS = (
        ("", "Select marital status"),
        ("Married", "Married"),
        ("Single", "Single")
    )

    username = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control", 'placeholder': 'Enter Your username'})
    )
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={"class": "form-control", 'placeholder': 'Enter E-mail address'})
    )
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control", 'placeholder': 'Enter first name'})
    )
    mid_name = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control", 'placeholder': 'Enter  middle name'})
    )
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control", 'placeholder': 'Enter last name'})
    )
    pcontact = forms.CharField(widget=forms.NumberInput(
        attrs={"class": "form-control", 'placeholder': 'Enter p_contact'})
    )
    scontact = forms.CharField(widget=forms.NumberInput(
        attrs={"class": "form-control", 'placeholder': 'Enter s_contact'})
    )
    marital_status = forms.CharField(widget=forms.Select(
        attrs={"class": "form-control", 'placeholder': 'Enter marital status'}, choices=MARITAL_STATUS)
    )
    nationality = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control", 'placeholder': 'Enter nationality'})
    )

    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={"class": "form-control", 'placeholder': 'Enter Your Password'})
    )
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={"class": "form-control", 'placeholder': 'Confirm Your Password'})
    )
    is_tenant = forms.CharField(widget=forms.CheckboxInput(
        attrs={"class": "form-check-input"}), required=False)
    is_owner = forms.CharField(widget=forms.CheckboxInput(
        attrs={"class": "form-check-input"}), required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'mid_name',
                  'last_name', 'pcontact', 'scontact', 'marital_status', 'nationality', 'is_tenant', 'is_owner']


class SiginInUserForm(forms.Form):
    username = forms.CharField(max_length=50, widget=(forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Enter username"
    })))
    password = forms.CharField(widget=(forms.PasswordInput(attrs={
        "class": "form-control",
        "placeholder": "Enter password"
    })))
