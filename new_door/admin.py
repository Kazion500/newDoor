from django.contrib import admin
from .models import (
    Property, Entity
)


@admin.register(Entity)
class EntityModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'entity_name', 'contact_no', 'address1',
                    'address2', 'city', 'pobox', 'state', 'country', 'email', 'desc')


@admin.register(Property)
class PropertyModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner_name', 'property_name', 'entity', 'address1', 'address2',
                    'city', 'pobox', 'state', 'country', 'email', 'contact_no', 'location')

# @admin.register (Unit)
# class A_Unit(admin.ModelAdmin):
#     list_display = ('id', 'PropID', 'PrtTypID', 'flat', 'OwnerTypeID', 'rent_amount', 'size', 'OccupancyTypeID', 'bedrooms', 'bathrooms', 'parking', 'desc')

# @admin.register (UnitImage)
# class A_UnitImage(admin.ModelAdmin):
#     list_display = ('id', 'unit_id', 'unit_image')

#     #*************Master Table Category_Type*************
# @admin.register (CategoryType)
# class A_CategoryType(admin.ModelAdmin):
#     list_display = ('id', 'CatType', 'desc')

#     #*************Master Table Ownership_Type*************
# @admin.register (OwnershipType)
# class A_OwnershipType(admin.ModelAdmin):
#     list_display = ('id', 'OwnershipType', 'desc')

#     #*************Master Table Property_Type*************
# @admin.register (PropertyType)
# class A_PropertyType(admin.ModelAdmin):
#     list_display = ('id', 'CatId', 'PrtType', 'desc')

#     #*************Master Table Document_Type*************
# @admin.register (DocumentType)
# class A_DocumentType(admin.ModelAdmin):
#     list_display = ('DocsType', 'desc')

#     #*************Master Table PayMode_Type*************
# @admin.register (PayModeType)
# class A_PayModeType(admin.ModelAdmin):
#     list_display = ('id', 'PayType', 'desc')

#     #*************Master Table StatusReq_Type*************
# @admin.register (StatusReqType)
# class A_StatusReqType(admin.ModelAdmin):
#     list_display = ('id', 'StRqty', 'desc')

#     #*************Master Table Tenant_Request_Type*************
# @admin.register (TenantReqType)
# class A_TenantReqType(admin.ModelAdmin):
#     list_display = ('id', 'TenantReqType', 'desc')

#     #*************Master Table Contract_Request_Type*************
# @admin.register (ContractReqType)
# class A_ContractReqType(admin.ModelAdmin):
#     list_display = ('id', 'ContractReqType', 'desc')

#     #*************Master Table Documents_Type*************
# @admin.register (DocumentsType)
# class A_DocumentsType(admin.ModelAdmin):
#     list_display = ('id', 'DocumentsType', 'desc')

#     #*************Master Table Documents_Type*************
# @admin.register (OccupancyType)
# class A_OccupancyType(admin.ModelAdmin):
#     list_display = ('id', 'OccupancyType', 'desc')

#     #*************Master Table Documents_Type*************
# @admin.register (TenantContract)
# class A_TenantContract(admin.ModelAdmin):
#     list_display = ('id', 'PropID', 'UnitID', 'ContractNo', 'StartDate', 'EndDate', 'Discount', 'AnnualRent', 'SecurityDep', 'Commission', 'Installments', 'Remark', 'SMSNotify', 'EmailNotify')

#     #*************Master Table User*************
# @admin.register (User)
# class A_User(admin.ModelAdmin):
#     list_display = ('id', 'user_id', 'user_password', 'usr_f_name', 'usr_m_name', 'usr_l_name', 'email', 'pcontact', 'scontact', 'marry_status', 'nationality', 'rollid')

#     #*************Master Table Tenant*************
# @admin.register (Tenant)
# class A_Tenant(admin.ModelAdmin):
#     list_display = ('id', 'user_id', 'user_password', 'usr_f_name', 'usr_m_name', 'usr_l_name', 'email', 'pcontact', 'scontact', 'marry_status', 'nationality', 'rollid')
