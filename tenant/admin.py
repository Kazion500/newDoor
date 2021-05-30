from tenant.models import TenantContract
from django.contrib import admin

# Register your models here.


@admin.register(TenantContract)
class TenantContractModelAdmin(admin.ModelAdmin):
    list_display = ( 'property_id', 'unit_id', 'contract_status', 'contract_request', 'contract_no', 'start_date',
                    'end_date', 'discount', 'annual_rent', 'security_dep', 'commission', 'installments',
                    'remark', 'sms_notify', 'email_notify')
