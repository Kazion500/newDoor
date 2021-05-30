from django.contrib import admin
from app_config.models import CategoryType, DocumentType, OccupancyType, OwnershipType, PropertyType

# Register your models here.


@admin.register(CategoryType)
class CategoryTypeModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'cat_type', 'desc')


@admin.register(PropertyType)
class PropertyTypeModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'property_type', 'desc')


@admin.register(OwnershipType)
class OwnershipTypeModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'ownership_type', 'desc')


@admin.register(OccupancyType)
class OccupancyTypeModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'occupancy_type', 'desc')


@admin.register(DocumentType)
class DocumentTypeModelAdmin(admin.ModelAdmin):
    list_display = ('docs_type', 'desc', 'num_of_doc')
