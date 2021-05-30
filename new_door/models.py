from django.db import models
from django.contrib.auth import get_user_model
from django_countries.fields import CountryField
from app_config.models import DocumentType, OccupancyType, OwnershipType, PropertyType

Profile = get_user_model()

class Entity(models.Model):
    manager = models.OneToOneField(Profile, on_delete=models.CASCADE, null=True, blank=True)
    entity_name = models.CharField(max_length=50, unique=True)
    contact_no = models.CharField(max_length=20, unique=True)
    address1 = models.CharField(max_length=250, )
    address2 = models.CharField(max_length=250, null=True, blank=True)
    city = models.CharField(max_length=50,)
    po_box = models.CharField(max_length=20, )
    state = models.CharField(max_length=50, )
    country = CountryField()
    email = models.EmailField(max_length=30, unique=True)
    desc = models.TextField(max_length=550, null=True, blank=True)

    def __str__(self):
        return f'{self.entity_name}'


class Property(models.Model):
    owner_name = models.CharField(max_length=30)
    entity = models.ForeignKey(
        Entity, on_delete=models.CASCADE, )
    property_name = models.CharField(max_length=20)
    address1 = models.CharField(max_length=250)
    address2 = models.CharField(max_length=250, null=True, blank=True)
    city = models.CharField(max_length=50)
    po_box = models.CharField(max_length=20)
    state = models.CharField(max_length=50)
    country = CountryField()
    email = models.EmailField(max_length=30, unique=True)
    contact_no = models.CharField(max_length=30, unique=True)
    location = models.CharField(max_length=254)

    def __str__(self):
        return f'{self.property_name}'


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
        return f'{self.pk}'


class UnitImage(models.Model):
    unit_id = models.ForeignKey(Unit, on_delete=models.CASCADE,)
    unit_image = models.ImageField(upload_to="unit",)


class TenantDocument(models.Model):
    tenant = models.ForeignKey(Profile, on_delete=models.CASCADE)
    doc_type = models.ForeignKey(DocumentType, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='documents/', null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    desc = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.is_verified}'
