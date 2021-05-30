from profiles.models import Profile
from django import forms

from app_config.models import (
    PropertyType, CategoryType, OwnershipType,
    OccupancyType, ContractReqType,
    TenantReqType, StatusReqType,
    DocumentType, PayModeType,

)


class CategoryTypeModelForm(forms.ModelForm):
    class Meta:
        model = CategoryType
        fields = ('cat_type', 'desc')
        widgets = {
            'cat_type': forms.TextInput(attrs={'class': 'form-control'}),
            'desc': forms.TextInput(attrs={'class': 'form-control'}),
        }


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
