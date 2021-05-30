from django.db import models
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField
# Create your models here.


class Profile(AbstractUser):
    MARITAL_STATUS = (
        ("", "Select marital status"),
        ("Married", "Married"),
        ("Single", "Single")
    )
    mid_name = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(upload_to="profile_pic", null=True, blank=True)
    pcontact = models.CharField(max_length=14)
    scontact = models.CharField(max_length=14)
    marital_status = models.CharField(choices=MARITAL_STATUS, max_length=50)
    nationality = CountryField()
    is_tenant = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)

    def __str__(self):
        return self.username
