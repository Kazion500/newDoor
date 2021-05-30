from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

from app_config.models import DocumentType, OccupancyType, OwnershipType, PropertyType
from profiles.models import Profile
from new_door.models import Property, Entity, TenantDocument, Unit


class EntityModelForm(forms.ModelForm):
    country = CountryField(blank_label='Select country').formfield(
        widget=CountrySelectWidget(attrs={"class": "form-control"}),
    )
    contact_no = forms.CharField(max_length=14, help_text="Include country code e.g (+260)", widget=(
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
            'po_box': forms.NumberInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'desc': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_contact_no(self):
        phone_no = 10
        contact_no = self.cleaned_data['contact_no']
        if len(str(contact_no)) != phone_no:
            raise forms.ValidationError(
                f'Phone number should have {phone_no} numbers only')
        return contact_no


class PropertyModelForm(forms.ModelForm):
    entity = forms.ModelChoiceField(Entity.objects.all(),
                                    empty_label="Select entity name", widget=(forms.Select(attrs={'class': 'form-control'})))
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
            'owner_name': forms.TextInput(attrs={'class': 'form-control'}),
            'address1': forms.TextInput(attrs={'class': 'form-control'}),
            'address2': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'po_box': forms.NumberInput(attrs={'class': 'form-control'}),
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
            'rent_amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'size': forms.NumberInput(attrs={'class': 'form-control'}),
            'bedrooms': forms.NumberInput(attrs={'class': 'form-control'}),
            'bathrooms': forms.NumberInput(attrs={'class': 'form-control'}),
            'parking': forms.TextInput(attrs={'class': 'form-control'}),
            'desc': forms.TextInput(attrs={'class': 'form-control'}),

        }


class UploadDocumentModelForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={"multiple": True}))
    tenant = forms.ModelChoiceField(Profile.objects.all(
    ), widget=forms.Select(attrs={'class': 'form-control'}), empty_label="Select Tenant")
    doc_type = forms.ModelChoiceField(DocumentType.objects.all(
    ), widget=forms.Select(attrs={'class': 'form-control'}), empty_label="Select document type")
    desc = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control'}), required=False)

    class Meta:
        model = TenantDocument
        fields = ('tenant', 'doc_type', 'image', 'is_verified', 'desc')
