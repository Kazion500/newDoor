from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# *********Class Entity Defination Start Here---30-10-2020 11.35PM- Javed Farooqui *******

# *********Class User Defination Start Here---11-11-2020 10:10PM- Javed *******


class Profile(models.Model):
    MARITAL_STATUS = (
        ("Married", "Married"),
        ("Single", "Single")
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # user_id = models.CharField(max_length=20,)
    # user_password = models.CharField(max_length=20, )
    first_name = models.CharField(max_length=50,)
    mid_name = models.CharField(max_length=50, )
    last_name = models.CharField(max_length=50, )
    email = models.CharField(max_length=254, )
    pcontact = models.CharField(max_length=254,)
    scontact = models.CharField(max_length=254, )
    marry_status = models.CharField(choices=MARITAL_STATUS, max_length=50)
    nationality = models.CharField(max_length=254,)
    roll_id = models.CharField(max_length=254,)
    is_tenant = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
# *********Class User Defination End Here---11-11-2020 10:10PM- Javed *******


class Entity(models.Model):
    entity_name = models.CharField(max_length=50, )
    contact_no = models.CharField(max_length=20, )
    address1 = models.CharField(max_length=250, )
    address2 = models.CharField(max_length=250, )
    city = models.CharField(max_length=50,)
    pobox = models.CharField(max_length=20, )
    state = models.CharField(max_length=50, )
    country = models.CharField(max_length=50, )
    email = models.EmailField(max_length=30, )
    desc = models.CharField(max_length=550,)

    def __str__(self):
        return self.entity_name
# *********Class Entity Defination End Here---31-10-2020 12.40AM- Javed Farooqui ********************************************


# *********Class Property Defination Start Here---31-10-2020 12.43AM- Javed Farooqui *******
class Property(models.Model):
    owner_name = models.ForeignKey(Profile, on_delete=models.CASCADE)
    property_name = models.CharField(max_length=20, )
    entity = models.ForeignKey(
        Entity, on_delete=models.CASCADE, )
    address1 = models.CharField(max_length=250,)
    address2 = models.CharField(max_length=250, )
    city = models.CharField(max_length=50,)
    pobox = models.CharField(max_length=20,)
    state = models.CharField(max_length=50, )
    country = models.CharField(max_length=50,)
    email = models.CharField(max_length=30, )
    contact_no = models.CharField(max_length=30, )
    location = models.CharField(max_length=254,)

    def __str__(self):
        return self.property_name


# *********Class CategoryType Defination Start Here---31-10-2020 02.25AM- Javed Farooqui *******
class PropertyType(models.Model):
    category_id = models.ForeignKey('CategoryType', on_delete=models.CASCADE)
    property_type = models.CharField(max_length=50,)
    desc = models.CharField(max_length=550,)

    def __str__(self):
        return self.property_type


class OwnershipType(models.Model):
    ownership_type = models.CharField(max_length=50,)
    desc = models.CharField(max_length=550,)


class OccupancyType(models.Model):
    occupancy_type = models.CharField(max_length=50, )
    desc = models.CharField(max_length=550,)


class Unit(models.Model):
    property_id = models.ForeignKey(
        Property, on_delete=models.CASCADE, )
    property_type = models.ForeignKey(
        PropertyType, on_delete=models.CASCADE, )
    flat = models.CharField(max_length=250, )
    pwner_type = models.ForeignKey(
        OwnershipType, on_delete=models.CASCADE, )
    rent_amount = models.CharField(max_length=50, )
    size = models.CharField(max_length=20,)
    occupancy_type = models.ForeignKey(
        OccupancyType, on_delete=models.CASCADE, )
    bedrooms = models.CharField(max_length=50, )
    bathrooms = models.CharField(max_length=30,)
    parking = models.CharField(max_length=30, )
    desc = models.CharField(max_length=550, )
    # image= models.ImageField(upload_to = "pictures")


class UnitImage(models.Model):
    unit_id = models.ForeignKey('Unit', on_delete=models.CASCADE,)
    unit_image = models.ImageField(upload_to="pictures", )


class CategoryType(models.Model):
    cat_type = models.CharField(max_length=50,)
    desc = models.CharField(max_length=550, )


class DocumentType(models.Model):
    docs_type = models.CharField(max_length=50,)
    desc = models.CharField(max_length=550, )


class PayModeType(models.Model):
    pay_type = models.CharField(max_length=50,)
    desc = models.CharField(max_length=550, )


class StatusReqType(models.Model):
    str_qty = models.CharField(max_length=50, )
    desc = models.CharField(max_length=550, )


class TenantReqType(models.Model):
    tenant_req_type = models.CharField(max_length=50, )
    desc = models.CharField(max_length=550, )


class ContractReqType(models.Model):
    contract_req_type = models.CharField(max_length=50, )
    desc = models.CharField(max_length=550, )


class DocumentsType(models.Model):
    documents_type = models.CharField(max_length=50,)
    desc = models.CharField(max_length=550,)


class TenantContract(models.Model):
    property_id = models.ForeignKey(
        Property, on_delete=models.CASCADE, )
    unit_id = models.ForeignKey('Unit', on_delete=models.CASCADE,)
    contract_no = models.CharField(max_length=50,)
    start_date = models.DateField(max_length=50, )
    end_date = models.CharField(max_length=50, )
    discount = models.CharField(max_length=50,)
    annual_rent = models.CharField(max_length=50,)
    security_dep = models.CharField(max_length=50, )
    commission = models.CharField(max_length=50, )
    installments = models.CharField(max_length=50,)
    remark = models.CharField(max_length=550,)
    sms_notify = models.BooleanField(default='False')
    email_notify = models.BooleanField(default='False')
