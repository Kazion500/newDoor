from django.core import validators
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from .models import (
    Property, Entity,
    Profile, Unit,
    UnitImage, PropertyType,
    CategoryType, OwnershipType,
    OccupancyType, TenantContract,
    ContractReqType, TenantReqType,
    StatusReqType, DocumentType,
    PayModeType,
)


class EntityModelForm(forms.ModelForm):
    country = CountryField(blank_label='Select country').formfield(
        widget=CountrySelectWidget(attrs={"class": "form-control"}),
    )
    contact_no = forms.CharField(max_length=100, help_text="Include country code e.g (+260)", widget=(
        forms.NumberInput(attrs={'class': 'form-control'})))

    class Meta:
        model = Entity
        fields = '__all__'
        exclude = ['id']
        widgets = {
            'entity_name': forms.TextInput(attrs={'class': 'form-control'}),
            'address1': forms.TextInput(attrs={'class': 'form-control'}),
            'address2': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'pobox': forms.NumberInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'desc': forms.TextInput(attrs={'class': 'form-control'}),
        }


class PropertyModelForm(forms.ModelForm):
    owner_name = forms.ModelChoiceField(Profile.objects.all(
    ), empty_label="Select owner name", widget=(forms.Select(attrs={'class': 'form-control'})))
    entity = forms.ModelChoiceField(Entity.objects.all(
    ), empty_label="Select entity name", widget=(forms.Select(attrs={'class': 'form-control'})))
    country = CountryField(blank_label='Select country').formfield(
        widget=CountrySelectWidget(attrs={"class": "form-control"}),
        # required=False
    )
    contact_no = forms.CharField(help_text="Include country code e.g (+260)", widget=(
        forms.NumberInput(attrs={'class': 'form-control'})))

    class Meta:
        model = Property
        fields = '__all__'
        exclude = ['id']
        widgets = {
            'property_name': forms.TextInput(attrs={'class': 'form-control'}),
            'address1': forms.TextInput(attrs={'class': 'form-control'}),
            'address2': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'pobox': forms.NumberInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
        }

# Code refactored - 26-11-2020 11.03PM- Patrick


class UnitModelForm(forms.ModelForm):
    property_id = forms.ModelChoiceField(Property.objects.all(
    ), empty_label="Select property", widget=(forms.Select(attrs={'class': 'form-control'})))
    property_type = forms.ModelChoiceField(PropertyType.objects.all(
    ), empty_label="Select property type", widget=(forms.Select(attrs={'class': 'form-control'})))
    ownership_type = forms.ModelChoiceField(OwnershipType.objects.all(
    ), empty_label="Select ownership type", widget=(forms.Select(attrs={'class': 'form-control'})))
    occupancy_type = forms.ModelChoiceField(OccupancyType.objects.all(
    ), empty_label="Select occupancy type", widget=(forms.Select(attrs={'class': 'form-control'})))

    class Meta:
        model = Unit
        fields = '__all__'
        exclude = ['id']
        widgets = {
            'flat': forms.TextInput(attrs={'class': 'form-control'}),
            'rent_amount': forms.TextInput(attrs={'class': 'form-control'}),
            'size': forms.TextInput(attrs={'class': 'form-control'}),
            'bedrooms': forms.TextInput(attrs={'class': 'form-control'}),
            'bathrooms': forms.TextInput(attrs={'class': 'form-control'}),
            'parking': forms.TextInput(attrs={'class': 'form-control'}),
            'desc': forms.TextInput(attrs={'class': 'form-control'}),
        }

# Code refactored - 26-11-2020 8.32PM- Patrick


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


class CategoryTypeModelForm(forms.ModelForm):
    class Meta:
        model = CategoryType
        fields = ('cat_type', 'desc')
        widgets = {
            'cat_type': forms.TextInput(attrs={'class': 'form-control'}),
            'desc': forms.TextInput(attrs={'class': 'form-control'}),
        }

# Code refactored - 26-11-2020 7.03PM- Patrick


class PropertyTypeModelForm(forms.ModelForm):
    class Meta:
        model = PropertyType
        fields = ('category', 'property_type', 'desc')
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'property_type': forms.TextInput(attrs={'class': 'form-control'}),
            'desc': forms.TextInput(attrs={'class': 'form-control'}),
        }


# Code refactored - 27-11-2020 6.48PM- Patrick
class OwnershipTypeModelForm(forms.ModelForm):
    class Meta:
        model = OwnershipType
        fields = ('ownership_type', 'desc')
        widgets = {
            'ownership_type': forms.TextInput(attrs={'class': 'form-control'}),
            'desc': forms.TextInput(attrs={'class': 'form-control'}),
        }


class OccupancyTypeModelForm(forms.ModelForm):
    class Meta:
        model = OccupancyType
        fields = ('occupancy_type', 'desc')
        widgets = {
            'occupancy_type': forms.TextInput(attrs={'class': 'form-control'}),
            'desc': forms.TextInput(attrs={'class': 'form-control'}),
        }


class TenantContractModelForm(forms.ModelForm):
    class Meta:
        model = TenantContract
        fields = '__all__'
        exclude = ['id']

        widgets = {
            'tenant': forms.Select(attrs={'class': 'form-control'}),
            'property_id': forms.Select(attrs={'class': 'form-control'}),
            'unit_id': forms.Select(attrs={'class': 'form-control'}),
            'contract_no': forms.TextInput(attrs={'class': 'form-control'}),
            'start_date': forms.TextInput(attrs={'class': 'form-control'}),
            'end_date': forms.TextInput(attrs={'class': 'form-control'}),
            'discount': forms.TextInput(attrs={'class': 'form-control'}),
            'annual_rent': forms.TextInput(attrs={'class': 'form-control'}),
            'security_dep': forms.TextInput(attrs={'class': 'form-control'}),
            'commission': forms.TextInput(attrs={'class': 'form-control'}),
            'installments': forms.TextInput(attrs={'class': 'form-control'}),
            'remark': forms.TextInput(attrs={'class': 'form-control'}),
            'sms_notify': forms.CheckboxInput(attrs={'class': 'form-control'},),
            'email_notify': forms.CheckboxInput(attrs={'class': 'form-control'}),
        }


class ContractReqTypeModelForm(forms.ModelForm):
    tenant = forms.ModelChoiceField(Profile.objects.filter(
        is_tenant=True), empty_label='Select Tenant', widget=(forms.Select(attrs={'class': 'form-control'})))

    class Meta:
        model = ContractReqType
        fields = '__all__'
        exclude = ['id']
        widgets = {
            'contract_req': forms.TextInput(attrs={'class': 'form-control'}),
            'desc': forms.TextInput(attrs={'class': 'form-control'}),
        }


class TenantReqTypeModelForm(forms.ModelForm):
    class Meta:
        model = TenantReqType
        fields = ('tenant_req_type', 'desc')
        widgets = {
            'tenant_req_type': forms.TextInput(attrs={'class': 'form-control'}),
            'desc': forms.TextInput(attrs={'class': 'form-control'}),
        }


class StatusReqTypeModelForm(forms.ModelForm):
    class Meta:
        model = StatusReqType
        fields = ('str_req', 'desc')
        widgets = {
            'str_req': forms.TextInput(attrs={'class': 'form-control'}),
            'desc': forms.TextInput(attrs={'class': 'form-control'}),
        }


class DocumentTypeModelForm(forms.ModelForm):
    class Meta:
        model = DocumentType
        fields = ('docs_type', 'desc')
        widgets = {
            'docs_type': forms.TextInput(attrs={'class': 'form-control'}),
            'desc': forms.TextInput(attrs={'class': 'form-control'}),
        }


class PayModeTypeModelForm(forms.ModelForm):
    class Meta:
        model = PayModeType
        fields = ('pay_type', 'desc')
        widgets = {
            'pay_type': forms.TextInput(attrs={'class': 'form-control'}),
            'desc': forms.TextInput(attrs={'class': 'form-control'}),
        }


# class TenantModelForm(forms.ModelForm):
#     class Meta:
#         model = Tenant
#         fields = ('user_id', 'user_password', 'usr_f_name', 'usr_m_name', 'usr_l_name',
#                   'email', 'pcontact', 'scontact', 'marry_status', 'nationality', 'rollid')
#         widgets = {
#             'user_id': forms.TextInput(attrs={'class': 'form-control'}),
#             'user_password': forms.TextInput(attrs={'class': 'form-control'}),
#             'usr_f_name': forms.TextInput(attrs={'class': 'form-control'}),
#             'usr_m_name': forms.TextInput(attrs={'class': 'form-control'}),
#             'usr_l_name': forms.TextInput(attrs={'class': 'form-control'}),
#             'email': forms.EmailInput(attrs={'class': 'form-control'}),
#             'pcontact': forms.TextInput(attrs={'class': 'form-control'}),
#             'scontact': forms.TextInput(attrs={'class': 'form-control'}),
#             'marry_status': forms.TextInput(attrs={'class': 'form-control'}),
#             'nationality': forms.TextInput(attrs={'class': 'form-control'}),
#             'rollid': forms.TextInput(attrs={'class': 'form-control'}),
#         }


# #********Forms Tenant_Contract Defination Start Here---08-11-2020 10:50PM- Javed Farooqui *******
# class F_User (forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('user_id', 'user_password', 'usr_f_name', 'usr_m_name', 'usr_l_name', 'email', 'pcontact', 'scontact', 'marry_status', 'nationality', 'rollid')
#         widgets = {
#             'user_id': forms.TextInput(attrs={'class':'form-control'}),
#             'user_password': forms.TextInput(attrs={'class':'form-control'}),
#             'usr_f_name': forms.TextInput(attrs={'class':'form-control'}),
#             'usr_m_name': forms.TextInput(attrs={'class':'form-control'}),
#             'usr_l_name': forms.TextInput(attrs={'class':'form-control'}),
#             'email': forms.TextInput(attrs={'class':'form-control'}),
#             'pcontact': forms.TextInput(attrs={'class':'form-control'}),
#             'scontact': forms.TextInput(attrs={'class':'form-control'}),
#             'marry_status': forms.TextInput(attrs={'class':'form-control'}),
#             'nationality': forms.TextInput(attrs={'class':'form-control'}),
#             'rollid': forms.TextInput(attrs={'class':'form-control'}),
#         }
