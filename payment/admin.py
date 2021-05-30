from payment.models import Payment
from django.contrib import admin

# Register your models here.


@admin.register(Payment)
class PaymentModelAdmin(admin.ModelAdmin):
    list_display = ('contract', 'unit', 'pay_mode', 'paid_date',
                    'amount', 'status', 'remain_amount', 'remarks')
