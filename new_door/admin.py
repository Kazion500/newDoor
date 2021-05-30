from django.contrib import admin
from new_door.models import (
    Property, Entity,
    Profile, Unit,
    UnitImage, TenantDocument
)


@admin.register(Entity)
class EntityModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'entity_name', 'contact_no', 'address1',
                    'address2', 'city', 'po_box', 'state', 'country', 'email', 'desc')


@admin.register(Property)
class PropertyModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'property_name', 'entity', 'address1', 'address2',
                    'city', 'po_box', 'state', 'country', 'email', 'contact_no', 'location')

@admin.register(Unit)
class UnitModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'property_id', 'property_type', 'flat', 'ownership_type', 'rent_amount',
                    'size', 'occupancy_type', 'bedrooms', 'bathrooms', 'parking', 'desc')


@admin.register(UnitImage)
class UnitImage(admin.ModelAdmin):
    list_display = ('id', 'unit_id', 'unit_image')


@admin.register(TenantDocument)
class TenantDocumentModelAdmin(admin.ModelAdmin):
    list_display = ('tenant', 'doc_type', 'image', 'is_verified')
