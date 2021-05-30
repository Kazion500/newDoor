from django.db import models
from profiles.models import Profile
from new_door.models import Property, Unit
from app_config.models import ContractReqType, StatusReqType

# Create your models here.


class TenantContract(models.Model):
    tenant = models.ForeignKey(Profile, on_delete=models.CASCADE)
    property_id = models.ForeignKey(
        Property, on_delete=models.CASCADE, null=True, blank=True)
    unit = models.OneToOneField(Unit, on_delete=models.CASCADE,)
    contract_status = models.OneToOneField(
        StatusReqType, on_delete=models.CASCADE, null=True, blank=True)
    contract_request = models.OneToOneField(
        ContractReqType, on_delete=models.CASCADE, null=True, blank=True)
    contract_no = models.CharField(
        max_length=50, unique=True, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    discount = models.PositiveIntegerField(null=True, blank=True, default=0)
    annual_rent = models.PositiveIntegerField(null=True, blank=True)
    security_dep = models.PositiveIntegerField(null=True, blank=True)
    commission = models.PositiveIntegerField(null=True, blank=True)
    installments = models.PositiveIntegerField(null=True, blank=True)
    remark = models.TextField(max_length=550, null=True, blank=True)
    sms_notify = models.BooleanField(default='False')
    email_notify = models.BooleanField(default='False')

    def __str__(self) -> str:
        return f'{self.unit}'
