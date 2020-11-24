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
    contact_no = models.CharField(max_length=20, default='')
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
    owner_name = models.ForeignKey(Profile,on_delete=models.CASCADE)
    property_name = models.CharField(max_length=20, )
    entity = models.ForeignKey(
        'Entity', on_delete=models.CASCADE, )
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


class Unit(models.Model):
    property_id = models.ForeignKey(
        'Property', on_delete=models.CASCADE, )
    property_type = models.ForeignKey(
        'PropertyType', on_delete=models.CASCADE, )
    flat = models.CharField(max_length=250, )
    pwner_type = models.ForeignKey(
        'OwnershipType', on_delete=models.CASCADE, )
    rent_amount = models.CharField(max_length=50, )
    size = models.CharField(max_length=20,)
    occupancy_type = models.ForeignKey(
        'OccupancyType', on_delete=models.CASCADE, )
    bedrooms = models.CharField(max_length=50, )
    bathrooms = models.CharField(max_length=30,)
    parking = models.CharField(max_length=30, )
    desc = models.CharField(max_length=550, )
    # image= models.ImageField(upload_to = "pictures")
# *********Class Property Defination End Here---31-10-2020 01.21AM- Javed Farooqui ********************************************

# *********Class Unit_Image Defination Start Here---- Faraz Farooqui *******


class UnitImage(models.Model):
    unit_id = models.ForeignKey('Unit', on_delete=models.CASCADE,)
    unit_image = models.ImageField(upload_to="pictures", )
# *********Class Unit_Image Defination End Here---- Faraz Farooqui ********************************************


# *********Class CategoryType Defination Start Here---31-10-2020 02.25AM- Javed Farooqui *******
class CategoryType(models.Model):
    cat_type = models.CharField(max_length=50,)
    desc = models.CharField(max_length=550, )
# *********Class CategoryType Defination End Here---31-10-2020 02.40AM- Javed Farooqui ********************************************


# *********Class OwnershipType Defination Start Here---31-10-2020 03.46AM- Javed Farooqui *******
class OwnershipType(models.Model):
    ownership_type = models.CharField(max_length=50,)
    desc = models.CharField(max_length=550,)
# *********Class OwnershipType Defination End Here---31-10-2020 04.48AM- Javed Farooqui ********************************************


# *********Class CategoryType Defination Start Here---31-10-2020 02.25AM- Javed Farooqui *******
class PropertyType(models.Model):
    category_id = models.ForeignKey('CategoryType', on_delete=models.CASCADE)
    property_type = models.CharField(max_length=50,)
    desc = models.CharField(max_length=550,)
# *********Class CategoryType Defination End Here---31-10-2020 02.40AM- Javed Farooqui ********************************************


# *********Class DocumentType Defination Start Here---01-11-2020 08.15PM- Javed Farooqui *******
class DocumentType(models.Model):
    docs_type = models.CharField(max_length=50,)
    desc = models.CharField(max_length=550, )
# *********Class DocumentType Defination End Here---01-11-2020 08.16PM- Javed Farooqui ********************************************


# *********Class Payment_Mode_Type Defination Start Here---02-11-2020 07.41PM- Javed Farooqui *******
class PayModeType(models.Model):
    pay_type = models.CharField(max_length=50,)
    desc = models.CharField(max_length=550, default='')
# *********Class Payment_Mode_Type Defination End Here---02-11-2020 07.43AM- Javed Farooqui ********************************************


# *********Class Status_Request_Type Defination Start Here---02-11-2020 09.46PM- Javed Farooqui *******
class StatusReqType(models.Model):
    str_qty = models.CharField(max_length=50, default='')
    desc = models.CharField(max_length=550, default='')
# *********Class Status_Request_Type Defination End Here---02-11-2020 09.48AM- Javed Farooqui ********************************************


# *********Class Tenant_Request_Type Defination Start Here---04-11-2020 08.24PM- Javed Farooqui *******
class TenantReqType(models.Model):
    tenant_req_type = models.CharField(max_length=50, default='')
    desc = models.CharField(max_length=550, default='')
# *********Class Tenant_Request_Type Defination End Here---04-11-2020 08.25PM- Javed Farooqui ********************************************


# *********Class Contract_Request_Type Defination Start Here---04-11-2020 09.00PM- Javed Farooqui *******
class ContractReqType(models.Model):
    contract_req_type = models.CharField(max_length=50, default='')
    desc = models.CharField(max_length=550, default='')
# *********Class Contract_Request_Type Defination End Here---04-11-2020 09.00PM- Javed Farooqui ********************************************


# *********Class Documents_Type Defination Start Here---04-11-2020 10.25PM- Javed Farooqui *******
class DocumentsType(models.Model):
    documents_type = models.CharField(max_length=50,)
    desc = models.CharField(max_length=550,)
# *********Class Documents_Type Defination End Here---04-11-2020 10.26PM- Javed Farooqui ********************************************


# *********Class OccupancyType Defination Start Here---06-11-2020 02.47PM- Faraz Farooqui *******
class OccupancyType(models.Model):
    occupancy_type = models.CharField(max_length=50, )
    desc = models.CharField(max_length=550,)
# *********Class OccupancyType Defination End Here---06-11-2020  02.47PM- Faraz Farooqui ********************************************


# *********Class Tenant_Contract Defination Start Here---08-11-2020 10.10PM- Faraz Farooqui *******
class TenantContract(models.Model):
    property_id = models.ForeignKey(
        'Property', on_delete=models.CASCADE, )
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
# *********Class Tenant_Contract Defination End Here---10-11-2020 10.15PM- Faraz Farooqui ********************************************

# *********Class Tenant Defination Start Here---21-11-2020 03:10PM- Javed *******


# class Tenant(models.Model):
#     user_id = models.CharField(max_length=20, default='')
#     user_password = models.CharField(max_length=20, default='')
#     usr_f_name = models.CharField(max_length=254, default='')
#     usr_m_name = models.CharField(max_length=254, default='')
#     usr_l_name = models.CharField(max_length=254, default='')
#     email = models.CharField(max_length=254, default='')
#     pcontact = models.CharField(max_length=254, default='')
#     scontact = models.CharField(max_length=254, default='')
#     marry_status = models.CharField(max_length=254, default='')
#     nationality = models.CharField(max_length=254, default='')
#     rollid = models.CharField(max_length=254, default='')
# *********Class User Defination End Here---11-11-2020 10:10PM- Javed *******
