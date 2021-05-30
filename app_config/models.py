from profiles.models import Profile
from django.db import models

# Create your models here.


class CategoryType(models.Model):
    cat_type = models.CharField(max_length=50, unique=True)
    desc = models.CharField(max_length=550,  null=True, blank=True)

    def __str__(self):
        return self.cat_type


class PropertyType(models.Model):
    category = models.ForeignKey(CategoryType, on_delete=models.CASCADE)
    property_type = models.CharField(max_length=100, unique=True)
    desc = models.TextField(max_length=550, null=True, blank=True)

    def __str__(self):
        return self.property_type


class OwnershipType(models.Model):
    ownership_type = models.CharField(max_length=50, unique=True)
    desc = models.TextField(max_length=550, null=True, blank=True)

    def __str__(self):
        return self.ownership_type


class OccupancyType(models.Model):
    occupancy_type = models.CharField(max_length=50, unique=True)
    desc = models.TextField(max_length=550, null=True, blank=True)

    def __str__(self):
        return self.occupancy_type


class DocumentType(models.Model):
    docs_type = models.CharField(max_length=50,)
    num_of_doc = models.IntegerField(default=2)
    desc = models.TextField(max_length=550,  null=True, blank=True)

    def __str__(self):
        return str(self.docs_type)


class PayModeType(models.Model):
    pay_type = models.CharField(max_length=50)
    desc = models.TextField(max_length=550,  null=True, blank=True)

    def __str__(self):
        return str(self.pay_type)


class StatusReqType(models.Model):
    str_req = models.CharField(max_length=50, )
    desc = models.TextField(max_length=550,  null=True, blank=True)

    def __str__(self):
        return str(self.str_req)


class TenantReqType(models.Model):
    tenant_req_type = models.CharField(max_length=50, )
    desc = models.TextField(max_length=550,  null=True, blank=True)


class ContractReqType(models.Model):
    tenant = models.ForeignKey(Profile, on_delete=models.CASCADE)
    contract_req = models.CharField(max_length=50)
    desc = models.TextField(max_length=550, null=True, blank=True)
