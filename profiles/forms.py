from django import forms
from django.contrib.auth.forms import UserCreationForm
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from profiles.models import Profile



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
        attrs={"class": "form-control", 'placeholder': 'Enter  middle name'}), required=False)
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control", 'placeholder': 'Enter last name'})
    )
    pcontact = forms.CharField(widget=forms.NumberInput(
        attrs={"class": "form-control", 'placeholder': 'Enter primary contact'})
    )
    scontact = forms.CharField(widget=forms.NumberInput(
        attrs={"class": "form-control", 'placeholder': 'Enter secondary contact'})
    )
    marital_status = forms.CharField(widget=forms.Select(
        attrs={"class": "form-control", 'placeholder': 'Enter marital status'}, choices=MARITAL_STATUS)
    )
    nationality = CountryField(blank_label='Select your nationality').formfield(
        widget=CountrySelectWidget(attrs={"class": "form-control"}),
    )
    image = forms.ImageField(widget=forms.FileInput(
        attrs={"class": "form-control"})
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
        attrs={"class": "form-check-input", "id": "is_owner"}), required=False)

    def clean_scontact(self):
        scontact_ = self.cleaned_data.get('scontact')
        pcontact_ = self.cleaned_data.get('pcontact')

        try:
            if scontact_ == pcontact_:
                raise forms.ValidationError(
                    f'Secondary contact can\'t be the same as Primary contact {pcontact_}')

            if len(str(scontact_)) != 10:
                raise forms.ValidationError(
                    f'Phone number should be 10')
            profile_obj = Profile.objects.get(scontact=scontact_)
            if scontact_ == profile_obj.scontact:
                raise forms.ValidationError(
                    'Secondary contact is already in use')
        except Profile.DoesNotExist:
            return scontact_

    def clean_pcontact(self):
        pcontact_ = self.cleaned_data.get('pcontact')
        try:
            if len(str(pcontact_)) != 10:
                raise forms.ValidationError(
                    f'Phone number should be 10')
            profile_obj = Profile.objects.get(pcontact=pcontact_)

            if pcontact_ == profile_obj.pcontact:
                raise forms.ValidationError(
                    'Primary contact is already in use')
        except Profile.DoesNotExist:
            return pcontact_

    def clean_username(self):
        username_ = self.cleaned_data.get('username')
        try:
            user_obj = Profile.objects.get(username=username_)

            if username_ == user_obj.username:
                raise forms.ValidationError('Username is already in use')
        except Profile.DoesNotExist:
            return username_

    class Meta:
        model = Profile
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'mid_name', 'image',
                  'last_name', 'pcontact', 'scontact', 'marital_status', 'nationality', 'is_tenant', 'is_owner']
