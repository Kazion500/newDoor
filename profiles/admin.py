from django.contrib import admin
from profiles.models import Profile

# Register your models here.
@admin.register(Profile)
class ProfileModelAdmin(admin.ModelAdmin):
    list_display = ('username', 'mid_name', 'pcontact',
                    'scontact', 'marital_status', 'nationality', 'is_manager', 'is_tenant')

