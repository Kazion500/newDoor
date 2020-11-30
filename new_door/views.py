from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum, Count
from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages

from .forms import (
    EntityModelForm,
    PropertyModelForm,
    UnitModelForm,
    CategoryTypeModelForm,
    PropertyTypeModelForm,
    OwnershipTypeModelForm,
    OccupancyTypeModelForm,
)

from .models import (
    Entity, Property,
    Unit, CategoryType,
    Profile, PropertyType,
    OccupancyType, OwnershipType
)
# Dashboard Rendering


def dashboard_view(request):
    return render(request, 'new_door/dashboard.html')


def tenant_dashboard(request):
    return render(request, 'new_door/tenant_dashboard.html')


def entity_overview(request):
    entities = Entity.objects.all()
    context = {
        'entities': entities
    }
    return render(request, 'new_door/entity_overview.html', context)


def property_overview(request):

    properties = Property.objects.all()
    number_of_units = Unit.objects.all().count()
    number_of_vacant_units = Unit.objects.filter(is_vacant=True).count()
    total_ = Unit.objects.aggregate(earnings=Sum('rent_amount'))

    context = {
        'properties': properties,
        'number_of_units': number_of_units,
        'number_of_vacant_units': number_of_vacant_units,
        'total': total_,
    }

    return render(request, 'new_door/property_overview.html', context)


def unit_overview(request):

    units = Unit.objects.all()
    total_ = Unit.objects.aggregate(earnings=Sum('rent_amount'))

    number_of_units = Unit.objects.all().count()
    number_of_vacant_units = Unit.objects.filter(is_vacant=True).count()
    units_occupied = number_of_units - number_of_vacant_units

    context = {
        'units': units,
        'units_occupied': units_occupied,
        'number_of_vacant_units': number_of_vacant_units,
        'total': total_,
    }

    return render(request, 'new_door/unit_overview.html', context)


def checklist(request):
    return render(request, 'new_door/checklist.html')


def upload_documents(request):
    return render(request, 'new_door/upload_documents.html')


def payment(request):
    return render(request, 'new_door/payment.html')


""" Add Views  """


def add_entity(request):
    entities = Entity.objects.all()

    if request.method == 'POST':
        form = EntityModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Congratulations...! Document Type successfully added.')
            return redirect('add_entity')
    else:
        form = EntityModelForm()

    context = {
        'form': form,
        'entities': entities
    }
    return render(request, 'new_door/add_entity.html', context)


def add_property(request):

    entities = Entity.objects.all()
    profiles = Profile.objects.all()
    if request.method == 'POST':
        form = PropertyModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Congratulations...! Property successfully added.')
            return redirect('add_property')
    else:
        form = PropertyModelForm(request.POST)

    context = {
        'form': form,
        'entities': entities,
        'profiles': profiles,
    }

    return render(request, 'new_door/add_property.html', context)


def add_unit(request):

    properties = Property.objects.all()
    property_types = PropertyType.objects.all()
    ownership_types = OwnershipType.objects.all()
    occupancy_types = OccupancyType.objects.all()

    if request.method == 'POST':
        form = UnitModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Congratulations...! Unit successfully added.')
            return redirect('add_unit')
    else:
        form = UnitModelForm(request.POST)

    context = {
        'form': form,
        'properties': properties,
        'property_types': property_types,
        'ownership_types': ownership_types,
        'occupancy_types': occupancy_types,
    }

    return render(request, 'new_door/add_unit.html', context)


def add_category_type(request):

    categories = CategoryType.objects.all()

    if request.method == 'POST':
        form = CategoryTypeModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Congratulations...! Category Type successfully added.')
            return redirect('add_category_type')
    else:
        form = CategoryTypeModelForm()

    context = {'form': form, 'categories': categories}

    return render(request, 'new_door/category_type.html', context)


def add_property_type(request):

    property_types = PropertyType.objects.all()
    categories = CategoryType.objects.all()

    if request.method == 'POST':
        form = PropertyTypeModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Congratulations...! Property Type successfully added.')
            return redirect('add_property_type')

    else:
        form = PropertyTypeModelForm()

    context = {
        'form': form,
        'property_types': property_types,
        'categories': categories
    }

    return render(request, 'new_door/property_type.html', context)


def add_ownership_type(request):

    ownership_types = OwnershipType.objects.all()

    if request.method == 'POST':
        form = OwnershipTypeModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Congratulations...! Ownership Type successfully added.')
            return redirect('add_ownership_type')
    else:
        form = OwnershipTypeModelForm()

    context = {
        'form': form,
        'ownership_types': ownership_types,
    }

    return render(request, 'new_door/ownership_type.html', context)


def add_occupancy_type(request):

    occupancy_types = OccupancyType.objects.all()

    if request.method == 'POST':
        form = OccupancyTypeModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Congratulations...! Ownership Type successfully added.')
            return redirect('add_occupancy_type')
    else:
        form = OccupancyTypeModelForm()

    context = {
        'form': form,
        'occupancy_types': occupancy_types,
    }

    return render(request, 'new_door/add_occupancy_type.html', context)


""" Edit Views  """


def update_entity(request, id):

    entity = get_object_or_404(Entity, pk=id)

    if request.method == "POST":
        form = EntityModelForm(request.POST, instance=entity)

        if form.is_valid():
            form.save()
            messages.success(
                request, 'Congratulations...! Entity successfully Updated.')
            return redirect('entity_overview')
    else:
        form = EntityModelForm(instance=entity)

    context = {
        'form': form,
        'entity': entity
    }

    return render(request, 'new_door/update_entity.html', context)


def update_property(request, id):
    _property = get_object_or_404(Property, pk=id)
    entities = Entity.objects.all()
    owners = Profile.objects.all()
    form = PropertyModelForm(request.POST, instance=_property)
    if form.is_valid():
        form.save()
        messages.success(
            request, 'Congratulations...! Property successfully Updated.')
        return redirect('property_overview')
    else:
        form = PropertyModelForm(instance=_property)

    context = {
        'form': form,
        'property': _property,
        'entities': entities,
        'owners': owners,
    }
    return render(request, 'new_door/update_property.html', context)

# Code refactored - 26-11-2020 9.30PM- Patrick


def update_unit(request, id):
    unit = get_object_or_404(Unit, pk=id)
    properties = Property.objects.all()
    property_types = PropertyType.objects.all()
    ownership_types = OwnershipType.objects.all()
    occupancy_types = OccupancyType.objects.all()

    if request.method == "POST":
        form = UnitModelForm(request.POST, instance=unit)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Congratulations...! Unit successfully Updated.')
            return redirect('unit_overview')
    else:
        form = UnitModelForm(instance=unit)

    context = {
        'form': form,
        'property': unit,
        'properties': properties,
        'property_types': property_types,
        'ownership_types': ownership_types,
        'occupancy_types': occupancy_types,
    }
    return render(request, 'new_door/update_unit.html', context)

# Code refactored - 26-11-2020 9.05PM- Patrick


def update_property_type(request, id):

    property_type = get_object_or_404(PropertyType, pk=id)
    categories = CategoryType.objects.all()

    if request.method == "POST":
        form = PropertyTypeModelForm(request.POST, instance=property_type)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Congratulations...! Property Type successfully Updated.')
            return redirect('add_product_type')
    else:
        form = PropertyTypeModelForm(instance=property_type)

    context = {
        "form": form,
        "categories": categories
    }

    return render(request, 'new_door/update_property_type.html', context)


# Code refactored - 26-11-2020 8.33PM- Patrick

def update_ownership_type(request, id):

    ownership_type = get_object_or_404(OwnershipType, pk=id)

    if request.method == "POST":
        form = OwnershipTypeModelForm(request.POST, instance=ownership_type)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Congratulations...! Property Type successfully Updated.')
            return redirect('add_ownership_type')
    else:
        form = OwnershipTypeModelForm(instance=ownership_type)

    context = {
        "form": form,
    }

    return render(request, 'new_door/update_ownership_type.html', context)


def update_occupancy_type(request, id):

    occupancy_type = get_object_or_404(OccupancyType, pk=id)

    if request.method == "POST":
        form = OccupancyTypeModelForm(request.POST, instance=occupancy_type)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Congratulations...! Occupancy Type successfully Updated.')
            return redirect('add_occupancy_type')
    else:
        form = OccupancyTypeModelForm(instance=occupancy_type)

    context = {
        "form": form,
    }

    return render(request, 'new_door/update_occupancy_type.html', context)


""" Delete Views """

# Code refactored - 26-11-2020 11.33PM- Patrick


def delete_entity(request, id):
    entity = get_object_or_404(Entity, pk=id)
    entity.delete()
    messages.success(
        request, 'Congratulations...! Entity successfully Deleted.')
    return redirect('entity_overview')

# Code refactored - 27-11-2020 5.30PM- Patrick


def delete_property(request, id):
    _property = Property.objects.get(pk=id)
    _property.delete()
    messages.success(
        request, 'Congratulations...! Property successfully Deleted.')
    return redirect('property_overview')


def delete_unit(request, id):
    unit = Unit.objects.get(pk=id)
    unit.delete()
    messages.success(
        request, 'Congratulations...! Unit successfully Deleted.')
    return redirect('unit_overview')


def delete_category_type(request, id):
    category_type = CategoryType.objects.get(pk=id)
    category_type.delete()
    messages.success(
        request, 'Congratulations...! Category Type successfully Deleted.')
    return redirect('add_category_type')

# Code refactored - 27-11-2020 11.45PM- Patrick


def delete_property_type(request, id):
    property_type = PropertyType.objects.get(pk=id)
    property_type.delete()
    messages.success(
        request, 'Congratulations...! Property Type successfully Deleted.')
    return redirect('add_property_type')


def delete_ownership_type(request, id):
    ownership_type = OwnershipType.objects.get(pk=id)
    ownership_type.delete()
    messages.success(
        request, 'Congratulations...! Ownership Type successfully Deleted.')
    return redirect('add_ownership_type')


def delete_occupancy_type(request, id):
    occupancy_type = OccupancyType.objects.get(pk=id)
    occupancy_type.delete()
    messages.success(
        request, 'Congratulations...! Occupancy Type successfully Deleted.')
    return redirect('add_occupancy_type')


""" Display Detail Views """


def view_entity(request, id):

    entity = get_object_or_404(Entity, pk=id)
    form = EntityModelForm(instance=entity)

    context = {
        'form': form,
        'entity': entity
    }

    return render(request, 'new_door/view_entity.html', context)

# Code refactored - 28-11-2020 5.30PM- Patrick


def view_property(request, id):

    _property = get_object_or_404(Property, pk=id)
    entities = Entity.objects.all()
    owners = Profile.objects.all()

    form = PropertyModelForm(instance=_property)

    context = {
        'form': form,
        'property': _property,
        'entities': entities,
        'owners': owners,
    }

    return render(request, 'new_door/view_property.html', context)


def view_unit(request, id):

    unit = get_object_or_404(Unit, pk=id)
    properties = Property.objects.all()
    property_types = PropertyType.objects.all()
    ownership_types = OwnershipType.objects.all()
    occupancy_types = OccupancyType.objects.all()

    form = UnitModelForm(instance=unit)

    context = {
        'form': form,
        'property': unit,
        'properties': properties,
        'property_types': property_types,
        'ownership_types': ownership_types,
        'occupancy_types': occupancy_types,
    }

    return render(request, 'new_door/view_unit.html', context)


def view_property_type(request, id):

    property_type = get_object_or_404(PropertyType, pk=id)
    categories = CategoryType.objects.all()

    form = PropertyTypeModelForm(instance=property_type)

    context = {
        "form": form,
        "categories": categories
    }

    return render(request, 'new_door/view_property_type.html', context)


# Code refactored - 28-11-2020 9.53PM- Patrick

def view_ownership_type(request, id):

    ownership_type = get_object_or_404(OwnershipType, pk=id)
    form = OwnershipTypeModelForm(instance=ownership_type)

    context = {
        "form": form,
    }

    return render(request, 'new_door/view_ownership_type.html', context)


def view_occupancy_type(request, id):

    occupancy_type = get_object_or_404(OccupancyType, pk=id)
    form = OccupancyTypeModelForm(instance=occupancy_type)

    context = {
        "form": form,
    }

    return render(request, 'new_door/view_occupancy_type.html', context)




""" Propery Unit Views """

# Code refactored - 28-11-2020 11.53PM- Patrick


def prepopulated_field_unit(request, id):
    _property = Property.objects.get(pk=id)
    unit = Unit.objects.filter(property_id=_property.pk).first
    print(_property.unit_set.filter(property_id=_property.pk))

    if request.method == 'POST':
        form = UnitModelForm(request.POST,instance=_property)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Congratulations...! Unit successfully added.')
            return redirect('add_unit')
    else:
        form = UnitModelForm(request.POST, instance=_property)

    context = {
        'form': form,
        # 'unit': unit,
        # 'property_types': property_types,
        # 'ownership_types': ownership_types,
        # 'occupancy_types': occupancy_types,
    }

    return render(request, 'new_door/add_property_unit.html', context)


def property_unit_overview(request, id):
    _property = get_object_or_404(Property, pk=id)
    units = Unit.objects.filter(property_id=_property.pk)
    number_of_units = Unit.objects.filter(property_id=_property).count()
    number_of_vacant_units = Unit.objects.filter(is_vacant=True).count()
    units_occupied = number_of_units - number_of_vacant_units

    context = {
        'property': _property,
        'units': units,
        'number_of_units': number_of_units,
        'number_of_vacant_units': number_of_vacant_units,
        'units_occupied': units_occupied
    }

    return render(request, 'new_door/property_unit_overview.html', context)


# # *********Class Documents_Type Defination Start Here---04-11-2020 10.15PM- Javed Farooqui *************************************
# def Documents_Type(request):
#     if request.method == 'POST':
#         ADDOCTY = F_DocumentsType(request.POST)
#         if ADDOCTY.is_valid():
#             DCT = ADDOCTY.cleaned_data['DocumentsType']
#             DCTDSC = ADDOCTY.cleaned_data['desc']
#             ADDOCTY = DocumentsType(DocumentsType=DCT, desc=DCTDSC)
#             ADDOCTY.save()
#             messages.success(
#                 request, 'Congratulations...! Documents Type successfully added.')
#     else:
#         ADDOCTY = F_DocumentsType()
#     DOT = DocumentsType.objects.all()
#     return render(request, 'Documents_Type.html', {'form': ADDOCTY, 'ADDT': DOT})
# # *********Class Documents_Type Defination End Here---04-11-2020 10.39PM- Javed Farooqui *******

# # ********** Delete Documents_Type Action button start here: 04-11-2020 10.15PM Javed Farooqui***************************


# def Delete_DocumentsType(request, id):
#     TRQ = DocumentsType.objects.get(pk=id)
#     TRQ.delete()
#     messages.success(
#         request, 'Congratulations...! Documents Type successfully Deleted.')
#     DOT = DocumentsType.objects.all()
#     return render(request, 'Documents_Type.html', {'ADDT': DOT})
# # ********** Delete Documents_Type Action button end here: 04-11-2020 10.39PM Javed Farooqui***************************

# # ********** View Documents_Type Action button start here: 05-11-2020 12.30PM Javed Farooqui**********


# def View_DocumentsType(request, id):
#     pi = DocumentsType.objects.get(pk=id)
#     ADDOCTY = F_DocumentsType(request.POST, instance=pi)
#     if ADDOCTY.is_valid():
#         ADDOCTY.save()
#         messages.success(
#             request, 'Congratulations...! Documents Type successfully Updated.')
#     else:
#         pi = DocumentsType.objects.get(pk=id)
#         ADDOCTY = F_DocumentsType(instance=pi)
#     return render(request, 'View_Documents_Type.html', {'pi': pi})
# # ********** View Documents_Type Action button end here: 05-11-2020 12.39PM Javed Farooqui*********************************

# # ********** Update Documents_Type Action button start here: 04-11-2020 10.15PM Javed Farooqui**********


# def Update_DocumentsType(request, id):
#     pi = DocumentsType.objects.get(pk=id)
#     ADDOCTY = F_DocumentsType(request.POST, instance=pi)
#     if ADDOCTY.is_valid():
#         ADDOCTY.save()
#         messages.success(
#             request, 'Congratulations...! Documents Type successfully Updated.')
#     else:
#         pi = DocumentsType.objects.get(pk=id)
#         ADDOCTY = F_DocumentsType(instance=pi)
#     return render(request, 'Update_Documents_Type.html', {'pi': pi})
# # ********** Update Documents_Type Action button end here: 04-11-2020 10.39PM Javed Farooqui*********************************


# # ******************************************************************************************************************************


# # *********Class Occupancy_Type Defination Start Here---07-11-2020 01.15PM- Javed Farooqui *************************************
# def Occupancy_Type(request):
#     if request.method == 'POST':
#         OCPTYP = F_OccupancyType(request.POST)
#         if OCPTYP.is_valid():
#             OPT = OCPTYP.cleaned_data['OccupancyType']
#             OPTDSC = OCPTYP.cleaned_data['desc']
#             OCPTYP = OccupancyType(OccupancyType=OPT, desc=OPTDSC)
#             OCPTYP.save()
#             messages.success(
#                 request, 'Congratulations...! Occupancy Type successfully added.')
#     else:
#         OCPTYP = F_OccupancyType()
#     OPTY = OccupancyType.objects.all()
#     return render(request, 'Occupancy_Type.html', {'form': OCPTYP, 'OPTY': OPTY})
# # *********Class Occupancy_Type Defination End Here---04-11-2020 10.39PM- Javed Farooqui *******

# # ********** Delete Occupancy_Type Action button start here: 04-11-2020 10.15PM Javed Farooqui***************************


# def Delete_OccupancyType(request, id):
#     TRQ = OccupancyType.objects.get(pk=id)
#     TRQ.delete()
#     messages.success(
#         request, 'Congratulations...! Occupancy Type successfully Deleted.')
#     OPTY = OccupancyType.objects.all()
#     return render(request, 'Occupancy_Type.html', {'OPTY': OPTY})
# # ********** Delete Occupancy_Type Action button end here: 04-11-2020 10.39PM Javed Farooqui***************************

# # ********** View Occupancy_Type Action button start here: 05-11-2020 12.30PM Javed Farooqui**********


# def View_OccupancyType(request, id):
#     pi = OccupancyType.objects.get(pk=id)
#     OCPTYP = F_OccupancyType(request.POST, instance=pi)
#     if OCPTYP.is_valid():
#         OCPTYP.save()
#         messages.success(
#             request, 'Congratulations...! Occupancy Type successfully Updated.')
#     else:
#         pi = OccupancyType.objects.get(pk=id)
#         OCPTYP = F_OccupancyType(instance=pi)
#     return render(request, 'View_Occupancy_Type.html', {'pi': pi})
# # ********** View Occupancy_Type Action button end here: 05-11-2020 12.39PM Javed Farooqui*********************************

# # ********** Update Occupancy_Type Action button start here: 04-11-2020 10.15PM Javed Farooqui**********


# def Update_OccupancyType(request, id):
#     pi = OccupancyType.objects.get(pk=id)
#     OCPTYP = F_OccupancyType(request.POST, instance=pi)
#     if OCPTYP.is_valid():
#         OCPTYP.save()
#         messages.success(
#             request, 'Congratulations...! Occupancy Type successfully Updated.')
#     else:
#         pi = OccupancyType.objects.get(pk=id)
#         OCPTYP = F_OccupancyType(instance=pi)
#     return render(request, 'Update_Occupancy_Type.html', {'pi': pi})
# # ********** Update Occupancy_Type Action button end here: 04-11-2020 10.39PM Javed Farooqui*********************************


# # ************************************************************************************************************************

# # ********** Update Add_Tenant Action button start here: 21-11-2020 03:10PM Javed Farooqui**********

# # ********** Update Add_Tenant Action button end here: 21-11-2020 03:35PM Javed Farooqui**********

# # ********** Update Tenant_Contract Action button start here: 20-11-2020 03:10PM Javed Farooqui**********


# def Tenant_Contract(request):
#     if request.method == 'POST':
#         ADTNTCONTR = F_TenantContract(request.POST)
#         if ADTNTCONTR.is_valid():
#             PROPID = ADTNTCONTR.cleaned_data['PropID']
#             UNITID = ADTNTCONTR.cleaned_data['UnitID']
#             CONTRACTNO = ADTNTCONTR.cleaned_data['ContractNo']
#             STARTDATE = ADTNTCONTR.cleaned_data['StartDate']
#             ENDDATE = ADTNTCONTR.cleaned_data['EndDate']
#             DISCOUNT = ADTNTCONTR.cleaned_data['Discount']
#             ANNUALRENT = ADTNTCONTR.cleaned_data['AnnualRent']
#             SECURITYDEP = ADTNTCONTR.cleaned_data['SecurityDep']
#             COMMISSION = ADTNTCONTR.cleaned_data['Commission']
#             EMI = ADTNTCONTR.cleaned_data['Installments']
#             REMARK = ADTNTCONTR.cleaned_data['Remark']
#             SMSNOTIFY = ADTNTCONTR.cleaned_data['SMSNotify']
#             EMAILNOTIFY = ADTNTCONTR.cleaned_data['EmailNotify']
#             ADTNTCONTR = TenantContract(PropID=PROPID, UnitID=UNITID, ContractNo=CONTRACTNO, StartDate=STARTDATE, EndDate=ENDDATE, Discount=DISCOUNT,
#                                         AnnualRent=ANNUALRENT, SecurityDep=SECURITYDEP, Commission=COMMISSION, Installments=EMI, Remark=REMARK, SMSNotify=SMSNOTIFY, EmailNotify=EMAILNOTIFY)
#             ADTNTCONTR.save()
#             messages.success(
#                 request, 'Congratulations...! Occupancy Type successfully added.')
#     else:
#         ADTNTCONTR = F_TenantContract()
#     TNTCTRT = TenantContract.objects.all()
#     UNT = Unit.objects.all()
#     PRT = Property.objects.all()
#     return render(request, 'Tenant_Contract.html', {'form': ADTNTCONTR, 'TNTCTRT': TNTCTRT, 'ADUNIT': UNT, 'ADPRPRTY': PRT})
# # ********** Update Tenant_Contract Action button end here: 21-11-2020 03:35PM Javed Farooqui**********

# # **********************************************************************************************************************


# def Add_User(request):
#     if request.method == "POST":
#         OCPTYP = F_User(request.POST)
#         if OCPTYP.is_valid():
#             userid = OCPTYP.cleaned_data['user_id']
#             userpwrd = OCPTYP.cleaned_data['user_password']
#             usrfsnm = OCPTYP.cleaned_data['usr_f_name']
#             usrmdnm = OCPTYP.cleaned_data['usr_m_name']
#             usrlsnm = OCPTYP.cleaned_data['usr_l_name']
#             email = OCPTYP.cleaned_data['email']
#             pcont = OCPTYP.cleaned_data['pcontact']
#             scont = OCPTYP.cleaned_data['scontact']
#             marital = OCPTYP.cleaned_data['marry_status']
#             national = OCPTYP.cleaned_data['nationality']
#             roll = OCPTYP.cleaned_data['rollid']
#             Usr = User(user_id=userid, user_password=userpwrd, usr_f_name=usrfsnm, usr_m_name=usrmdnm, usr_l_name=usrlsnm,
#                        email=email, pcontact=pcont, scontact=scont, marry_status=marital, nationality=national, rollid=roll)
#         Usr.save()
#         messages.success(
#             request, 'Congratulations...! User successfully added.')
#     else:
#         OCPTYP = F_User()
#     OPTY = User.objects.all()
#     return render(request, 'Add_User.html')

# # ******************************************************


# # ********** Update Review_Documents Action button start here: 20-11-2020 10.15PM Javed Farooqui**********
# def Review_Documents(request):
#     # pi = TenantContract.objects.get(pk=id)
#     # ADTNTCONTR = F_TenantContract(request.POST, instance=pi)
#     # if ADTNTCONTR.is_valid():
#     #         ADTNTCONTR.save()
#     #         messages.success(
#     #         request, 'Congratulations...! Occupancy Type successfully Updated.')
#     # else:
#     #     pi = TenantContract.objects.get(pk=id)
#     #     ADTNTCONTR = F_TenantContract(instance=pi)
#     return render(request, 'Review_Documents.html')
# # ********** Update Review_Documents Action button end here: 20-11-2020 12.39AM Javed Farooqui************

# # ********** Update Upload_Documents Action button start here: 21-11-2020 04.00PM Mohd Saad**********


# # ********** Update Upload_Documents Action button end here: 21-11-2020 12.39AM Javed Farooqui************
