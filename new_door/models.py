from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField


class Profile(models.Model):
    MARITAL_STATUS = (
        ("", "Select marital status"),
        ("Married", "Married"),
        ("Single", "Single")
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mid_name = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(upload_to="profile_pic", null=True, blank=True)
    pcontact = models.CharField(max_length=254)
    scontact = models.CharField(max_length=254)
    marital_status = models.CharField(choices=MARITAL_STATUS, max_length=50)
    nationality = CountryField()
    is_tenant = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    is_owner = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class Entity(models.Model):
    manager = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    entity_name = models.CharField(max_length=50, unique=True)
    contact_no = models.CharField(max_length=20, unique=True)
    address1 = models.CharField(max_length=250, )
    address2 = models.CharField(max_length=250, null=True, blank=True)
    city = models.CharField(max_length=50,)
    pobox = models.CharField(max_length=20, )
    state = models.CharField(max_length=50, )
    country = CountryField()
    email = models.EmailField(max_length=30, unique=True)
    desc = models.TextField(max_length=550, null=True, blank=True)

    def __str__(self):
        return self.entity_name


class Property(models.Model):
    owner_name = models.ForeignKey(Profile, on_delete=models.CASCADE)
    entity = models.ForeignKey(
        Entity, on_delete=models.CASCADE, )
    property_name = models.CharField(max_length=20)
    address1 = models.CharField(max_length=250)
    address2 = models.CharField(max_length=250, null=True, blank=True)
    city = models.CharField(max_length=50)
    pobox = models.CharField(max_length=20)
    state = models.CharField(max_length=50)
    country = CountryField()
    email = models.EmailField(max_length=30, unique=True)
    contact_no = models.CharField(max_length=30, unique=True)
    location = models.CharField(max_length=254)

    def __str__(self):
        return self.property_name


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

# Need to add user instance


class Unit(models.Model):
    property_id = models.ForeignKey(
        Property, on_delete=models.CASCADE)
    property_type = models.ForeignKey(
        PropertyType, on_delete=models.CASCADE, )
    flat = models.CharField(max_length=250)
    ownership_type = models.ForeignKey(
        OwnershipType, on_delete=models.CASCADE, )
    rent_amount = models.DecimalField(max_digits=8, decimal_places=2)
    size = models.PositiveIntegerField()
    occupancy_type = models.ForeignKey(
        OccupancyType, on_delete=models.CASCADE, )
    bedrooms = models.PositiveIntegerField()
    bathrooms = models.PositiveIntegerField()
    parking = models.CharField(max_length=30, )
    desc = models.TextField(max_length=550,  null=True, blank=True)
    # image= models.ImageField(upload_to = "pictures")

    def __str__(self):
        return str(self.pk)


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


# Image models
class UnitImage(models.Model):
    unit_id = models.ForeignKey(Unit, on_delete=models.CASCADE,)
    unit_image = models.ImageField(upload_to="unit",)


class UploadDocument(models.Model):
    tenant = models.ForeignKey(Profile, on_delete=models.CASCADE)
    doc_type = models.ForeignKey(DocumentType, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='documents/', null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    desc = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.doc_type)


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
