from django.core import validators
from django import forms
from .models import (
    Property, Unit, PropertyType,
    CategoryType, Entity
)


class EntityModelForm(forms.ModelForm):
    class Meta:
        model = Entity
        fields = ['entity_name', 'contact_no', 'address1', 'address2',
                  'city', 'pobox', 'state', 'country', 'email', 'desc']
        widgets = {
            'entity_name': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_no': forms.TextInput(attrs={'class': 'form-control'}),
            'address1': forms.TextInput(attrs={'class': 'form-control'}),
            'address2': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'pobox': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'desc': forms.TextInput(attrs={'class': 'form-control'}),
        }


class PropertyModelForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ('owner_name', 'property_name', 'entity', 'address1',  'address2',
                  'city', 'pobox', 'state', 'country', 'email', 'contact_no', 'location')
        widgets = {
            'owner_name': forms.TextInput(attrs={'class': 'form-control'}),
            'property_name': forms.TextInput(attrs={'class': 'form-control'}),
            'entity': forms.TextInput(attrs={'class': 'form-control'}),
            'address1': forms.TextInput(attrs={'class': 'form-control'}),
            'address2': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'pobox': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_no': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
        }


class UnitModelForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = ('property_id', 'property_type', 'flat', 'owner_type', 'rent_amount', 'size',
                  'occupancy_type', 'bedrooms', 'bathrooms', 'parking', 'desc')
        widgets = {
            'property_id': forms.Select(attrs={'class': 'form-control'}),
            'property_type': forms.Select(attrs={'class': 'form-control'}),
            'flat': forms.TextInput(attrs={'class': 'form-control'}),
            'owner_type': forms.TextInput(attrs={'class': 'form-control'}),
            'rent_amount': forms.TextInput(attrs={'class': 'form-control'}),
            'size': forms.TextInput(attrs={'class': 'form-control'}),
            'occupancy_type': forms.TextInput(attrs={'class': 'form-control'}),
            'bedrooms': forms.TextInput(attrs={'class': 'form-control'}),
            'bathrooms': forms.TextInput(attrs={'class': 'form-control'}),
            'parking': forms.TextInput(attrs={'class': 'form-control'}),
            'desc': forms.TextInput(attrs={'class': 'form-control'}),
        }


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
            'category': forms.TextInput(attrs={'class': 'form-control'}),
            'property_types': forms.TextInput(attrs={'class': 'form-control'}),
            'desc': forms.TextInput(attrs={'class': 'form-control'}),
        }
# #********Forms OwnershipType Defination Start Here---31-10-2020 03.48AM- Javed Farooqui *******
# class f_OwnershipType (forms.ModelForm):
#     class Meta:
#         model = OwnershipType
#         fields = ('OwnershipType', 'desc')
#         widgets = {
#             'OwnershipType': forms.TextInput(attrs={'class':'form-control'}),
#             'desc': forms.TextInput(attrs={'class':'form-control'}),
#         }
# #********Forms OwnershipType Defination End Here---31-10-2020 03.49AM- Javed Farooqui *****************************************


# #********Forms PropertyType Defination Start Here---31-10-2020 04:45PM- Javed Farooqui *******

# #********Forms PropertyType Defination End Here---31-10-2020 04:50PM- Javed Farooqui *****************************************


# #********Forms DocumentType Defination Start Here---01-11-2020 08.19PM- Javed Farooqui *******
# class F_DocumentType (forms.ModelForm):
#     class Meta:
#         model = DocumentType
#         fields = ('DocsType', 'desc')
#         widgets = {
#             'DocsType': forms.TextInput(attrs={'class':'form-control'}),
#             'desc': forms.TextInput(attrs={'class':'form-control'}),
#         }
# #********Forms DocumentType Defination End Here---01-11-2020 08.20PM- Javed Farooqui *****************************************


# #********Forms OwnershipType Defination Start Here---02-11-2020 07.45PM- Javed Farooqui *******
# class F_PayModeType (forms.ModelForm):
#     class Meta:
#         model = PayModeType
#         fields = ('PayType', 'desc')
#         widgets = {
#             'PayType': forms.TextInput(attrs={'class':'form-control'}),
#             'desc': forms.TextInput(attrs={'class':'form-control'}),
#         }
# #********Forms OwnershipType Defination End Here---02-11-2020 07.47PM Javed Farooqui *****************************************


# #********Forms Status_Request_Type Defination Start Here---02-11-2020 09.49PM- Javed Farooqui *******
# class F_StatusReqType (forms.ModelForm):
#     class Meta:
#         model = StatusReqType
#         fields = ('StRqty', 'desc')
#         widgets = {
#             'StRqty': forms.TextInput(attrs={'class':'form-control'}),
#             'desc': forms.TextInput(attrs={'class':'form-control'}),
#         }
# #********Forms Status_Request_Type Defination End Here---02-11-2020 09.50PM- Javed Farooqui *****************************************


# #********Forms Tenant_Request_Type Defination Start Here---04-11-2020 08.27PM- Javed Farooqui *******
# class F_TenantReqType (forms.ModelForm):
#     class Meta:
#         model = TenantReqType
#         fields = ('TenantReqType', 'desc')
#         widgets = {
#             'TenantReqType': forms.TextInput(attrs={'class':'form-control'}),
#             'desc': forms.TextInput(attrs={'class':'form-control'}),
#         }
# #********Forms Tenant_Request_Type Defination End Here---04-11-2020 08.28PM- Javed Farooqui *****************************************


# #********Forms Contract_Request_Type Defination Start Here---04-11-2020 09.02PM- Javed Farooqui *******
# class F_ContractReqType (forms.ModelForm):
#     class Meta:
#         model = ContractReqType
#         fields = ('ContractReqType', 'desc')
#         widgets = {
#             'ContractReqType': forms.TextInput(attrs={'class':'form-control'}),
#             'desc': forms.TextInput(attrs={'class':'form-control'}),
#         }
# #********Forms Contract_Request_Type Defination End Here---04-11-2020 09.03PM- Javed Farooqui *****************************************


# #********Forms Documents_Type Defination Start Here---04-11-2020 10:27PM- Javed Farooqui *******
# class F_DocumentsType (forms.ModelForm):
#     class Meta:
#         model = DocumentsType
#         fields = ('DocumentsType', 'desc')
#         widgets = {
#             'DocumentsType': forms.TextInput(attrs={'class':'form-control'}),
#             'desc': forms.TextInput(attrs={'class':'form-control'}),
#         }
# #********Forms Documents_Type Defination End Here---04-11-2020 10:28PM- Javed Farooqui *****************************************


# #********Forms Documents_Type Defination Start Here---07-11-2020 01:34PM- Javed Farooqui *******
# class F_OccupancyType (forms.ModelForm):
#     class Meta:
#         model = OccupancyType
#         fields = ('OccupancyType', 'desc')
#         widgets = {
#             'OccupancyType': forms.TextInput(attrs={'class':'form-control'}),
#             'desc': forms.TextInput(attrs={'class':'form-control'}),
#         }
# #********Forms Documents_Type Defination End Here---07-11-2020 01:37PM- Javed Farooqui *****************************************


# #********Forms Tenant_Contract Defination Start Here---08-11-2020 10:50PM- Javed Farooqui *******
# class F_TenantContract (forms.ModelForm):
#     class Meta:
#         model = TenantContract
#         fields = ('PropID', 'UnitID', 'ContractNo', 'StartDate', 'EndDate', 'Discount', 'AnnualRent', 'SecurityDep', 'Commission', 'Installments', 'Remark', 'SMSNotify', 'EmailNotify')
#         widgets = {
#             'PropID': forms.TextInput(attrs={'class':'form-control'}),
#             'UnitID': forms.TextInput(attrs={'class':'form-control'}),
#             'ContractNo': forms.TextInput(attrs={'class':'form-control'}),
#             'StartDate': forms.TextInput(attrs={'class':'form-control'}),
#             'EndDate': forms.TextInput(attrs={'class':'form-control'}),
#             'Discount': forms.TextInput(attrs={'class':'form-control'}),
#             'AnnualRent': forms.TextInput(attrs={'class':'form-control'}),
#             'SecurityDep': forms.TextInput(attrs={'class':'form-control'}),
#             'Commission': forms.TextInput(attrs={'class':'form-control'}),
#             'Installments': forms.TextInput(attrs={'class':'form-control'}),
#             'Remark': forms.TextInput(attrs={'class':'form-control'}),
#             'SMSNotify': forms.BooleanField(initial='False'),
#             'EmailNotify': forms.BooleanField(initial='False'),
#         }
# #********Forms Tenant_Contract Defination End Here---08-11-2020 10:50PM- Javed Farooqui ************************************

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
#             'email': forms.TextInput(attrs={'class': 'form-control'}),
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
# #********Forms Tenant_Contract Defination End Here---08-11-2020 10:50PM- Javed Farooqui ************************************

# #********Forms Tenant_Contract Defination Start Here---08-11-2020 10:50PM- Javed Farooqui *******

# #********Forms Tenant_Contract Defination End Here---08-11-2020 10:50PM- Javed Farooqui ************************************
