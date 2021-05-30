from django.contrib import admin
from maintenance.models import MaintenanceRequest, Engineer, Department, MaintenanceImage
# Register your models here.


@admin.register(Engineer)
class EngineerModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'license_num')


@admin.register(MaintenanceRequest)
class MaintenanceModelAdmin(admin.ModelAdmin):
    list_display = ('contract',  'request_status',   'tenant_request', 'request_date', 'request_details',
                    'completion_date', 'reference_no', 'review')


@admin.register(Department)
class DepartmentModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'desc')


@admin.register(MaintenanceImage)
class MaintenanceImageModelAdmin(admin.ModelAdmin):
    list_display = ('request', 'image', 'desc')
