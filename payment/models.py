from django.db import models
from new_door.models import Unit
from app_config.models import PayModeType
from tenant.models import TenantContract

# Create your models here.


class Payment(models.Model):
    contract = models.ForeignKey(TenantContract, on_delete=models.CASCADE)
    unit = models.ForeignKey(
        Unit, on_delete=models.CASCADE, null=True, blank=True)
    pay_mode = models.ForeignKey(
        PayModeType, on_delete=models.CASCADE, null=True, blank=True)
    paid_date = models.DateTimeField(auto_now_add=True)
    next_paid_date = models.DateField(null=True, blank=True)
    amount = models.PositiveIntegerField()
    status = models.CharField(max_length=50)
    remain_amount = models.PositiveIntegerField()
    remarks = models.TextField()

    def __str__(self) -> str:
        return str(self.amount)
