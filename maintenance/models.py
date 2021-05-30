from django.db import models
from django.contrib.auth import get_user_model
from tenant.models import TenantContract
from app_config.models import StatusReqType, TenantReqType

# Create your models here.
Profile = get_user_model()


class Engineer(models.Model):
    user = models.OneToOneField(
        Profile, on_delete=models.SET_NULL, null=True, blank=True)
    license_num = models.CharField(max_length=10)


class Department(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField()

    def __str__(self) -> str:
        return f'{self.name}'


class MaintenanceRequest(models.Model):
    contract = models.ForeignKey(TenantContract, on_delete=models.CASCADE)
    request_status = models.ForeignKey(StatusReqType, on_delete=models.CASCADE)
    tenant_request = models.ForeignKey(TenantReqType, on_delete=models.CASCADE)
    request_date = models.DateTimeField(auto_now_add=True)
    request_details = models.TextField()
    completion_date = models.DateTimeField(auto_now_add=True)
    reference_no = models.CharField(max_length=10)
    review = models.TextField()

    def __str__(self) -> str:
        return f'{self.tenant_request.str_req}'


class MaintenanceImage(models.Model):
    request = models.ForeignKey(MaintenanceRequest, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='documents', null=True, blank=True)
    desc = models.TextField()

    def __str__(self) -> str:
        return f'{self.name}'
