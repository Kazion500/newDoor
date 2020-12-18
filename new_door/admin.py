from django.contrib import admin
from .models import (
    Property, Entity,
    Profile, Unit,
    UnitImage, PropertyType,
    CategoryType, OwnershipType,
    OccupancyType,TenantContract
)


@admin.register(Entity)
class EntityModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'entity_name', 'contact_no', 'address1',
                    'address2', 'city', 'pobox', 'state', 'country', 'email', 'desc')


@admin.register(Property)
class PropertyModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'property_name', 'entity', 'address1', 'address2',
                    'city', 'pobox', 'state', 'country', 'email', 'contact_no', 'location')


@admin.register(Profile)
class ProfileModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'mid_name', 'pcontact',
                    'scontact', 'marital_status', 'nationality', 'is_manager', 'is_owner', 'is_tenant')


@admin.register(Unit)
class UnitModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'property_id', 'property_type', 'flat', 'ownership_type', 'rent_amount',
                    'size', 'occupancy_type', 'bedrooms', 'bathrooms', 'parking', 'desc')


@admin.register(UnitImage)
class UnitImage(admin.ModelAdmin):
    list_display = ('id', 'unit_id', 'unit_image')


@admin.register(CategoryType)
class CategoryType(admin.ModelAdmin):
    list_display = ('id', 'cat_type', 'desc')


@admin.register(PropertyType)
class PropertyType(admin.ModelAdmin):
    list_display = ('id', 'category', 'property_type', 'desc')


@admin.register(OwnershipType)
class OwnershipType(admin.ModelAdmin):
    list_display = ('id', 'ownership_type', 'desc')


@admin.register(OccupancyType)
class OccupancyType(admin.ModelAdmin):
    list_display = ('id', 'occupancy_type', 'desc')

@admin.register(TenantContract)
class TenantContract(admin.ModelAdmin):
    list_display = ('tenant','property_id','unit_id','contract_no','start_date',
    'end_date','discount','annual_rent','security_dep','commission','installments',
    'remark','sms_notify','email_notify')


