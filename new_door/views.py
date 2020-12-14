from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum, Count
from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required


from .forms import (
    EntityModelForm,
    PropertyModelForm,
    UnitModelForm,
    CategoryTypeModelForm,
    PropertyTypeModelForm,
    OwnershipTypeModelForm,
    OccupancyTypeModelForm,
    TenantContractModelForm,
    ContractReqTypeModelForm,
    TenantReqTypeModelForm,
    StatusReqTypeModelForm,
    DocumentTypeModelForm,
    PayModeTypeModelForm,
    ProfileRegistrationForm
)

from .models import (
    Entity, Property,
    Unit, CategoryType,
    Profile, PropertyType,
    OccupancyType, OwnershipType,
    DocumentType, PayModeType,
    StatusReqType, TenantReqType,
    ContractReqType, TenantContract,
)
# Dashboard Rendering


@login_required
def dashboard_view(request):
    if request.user.profile.is_tenant:
        return redirect('tenant_dashboard')

    total_num_units = Unit.objects.all().count()
    vacant_units = Unit.objects.filter(occupancy_type__occupancy_type__iexact="vacant").count()

    context = {
        'total_num_units':total_num_units,
        'vacant_units':vacant_units
    }
    return render(request, 'new_door/dashboard.html',context)


@login_required
def tenant_dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, 'new_door/tenant_dashboard.html')


@login_required
def entity_overview(request):
    entities = Entity.objects.all()
    context = {
        'entities': entities
    }
    return render(request, 'new_door/entity_overview.html', context)


@login_required
def property_overview(request, entity):
    entity = get_object_or_404(Entity, entity_name=entity)
    properties = Property.objects.filter(entity__entity_name=entity)
    number_of_units = Unit.objects.filter(
        property_id__entity__entity_name=entity).count()
    number_of_vacant_units = Unit.objects.filter(
        occupancy_type__occupancy_type__iexact="vacant",
        property_id__entity__entity_name=entity).count()

    number_of_occupied_units = Unit.objects.filter(
        occupancy_type__occupancy_type__iexact="occupied",
        property_id__entity__entity_name=entity).count()

    percentage = number_of_occupied_units / number_of_units * 100

    context = {
        'entity': entity,
        'properties': properties,
        'number_of_units': number_of_units,
        'number_of_occupied_units': number_of_occupied_units,
        'number_of_vacant_units': number_of_vacant_units,
        'percentage': int(percentage),
    }

    return render(request, 'new_door/property_overview.html', context)


@login_required
def property_all_overview(request):
    properties = Property.objects.all()
    number_of_units = Unit.objects.all().count()
    number_of_vacant_units = Unit.objects.filter(
        occupancy_type__occupancy_type__iexact="vacant").count()

    number_of_occupied_units = Unit.objects.filter(
        occupancy_type__occupancy_type__iexact="occupied").count()

    percentage = number_of_occupied_units / number_of_units * 100

    context = {
        'properties': properties,
        'number_of_units': number_of_units,
        'number_of_occupied_units': number_of_occupied_units,
        'number_of_vacant_units': number_of_vacant_units,
        'percentage': int(percentage),
    }


    return render(request, 'new_door/property_all_overview.html', context)


@login_required
def unit_overview(request):

    units = Unit.objects.all()

    number_of_vacant_units = Unit.objects.filter(
        occupancy_type__occupancy_type__iexact="vacant").count()
    number_of_occupied_units = Unit.objects.filter(
        occupancy_type__occupancy_type__iexact="occupied").count()

    if number_of_occupied_units is None:
        number_of_occupied_units = 0

    context = {
        'units': units,
        'number_of_occupied_units': number_of_occupied_units,
        'number_of_vacant_units': number_of_vacant_units,
    }

    return render(request, 'new_door/unit_overview.html', context)


@login_required
def checklist(request):
    return render(request, 'new_door/checklist.html')


@login_required
def upload_documents(request):
    return render(request, 'new_door/upload_documents.html')


@login_required
def payment(request):
    return render(request, 'new_door/add_payment.html')


""" Add Views  """


@login_required
def add_entity(request):
    entities = Entity.objects.all()

    if request.method == 'POST':
        form = EntityModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Congratulations...! Entity type successfully added.')
            return redirect('add_entity')
        else:
            messages.info(request, 'Entity already exits')
            return redirect('add_entity')
    else:
        form = EntityModelForm()

    context = {
        'form': form,
        'entities': entities
    }
    return render(request, 'new_door/add_entity.html', context)


@login_required
def add_property(request, entity):
    entity = get_object_or_404(Entity, entity_name=entity)
    profiles = Profile.objects.all()

    if request.method == 'POST':
        form = PropertyModelForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request, 'Congratulations...! Property successfully added.')
            return redirect('add_property', entity.entity_name)
    else:
        form = PropertyModelForm(request.POST)

    context = {
        'form': form,
        'entity': entity,
        'profiles': profiles,
    }

    return render(request, 'new_door/add_property.html', context)


@login_required
def add_property_all(request):
    entities = Entity.objects.all()
    profiles = Profile.objects.all()

    if request.method == 'POST':
        form = PropertyModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Congratulations...! Property successfully added.')
            return redirect('property_all_overview')
    else:
        form = PropertyModelForm(request.POST)

    context = {
        'form': form,
        'entities': entities,
        'profiles': profiles,
    }

    return render(request, 'new_door/add_property_all_overview.html', context)


@login_required
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


@login_required
def add_user(request):
    if request.method == "POST":
        form = ProfileRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.email = form.cleaned_data.get('email')
            user.profile.mid_name = form.cleaned_data.get('mid_name')
            user.profile.pcontact = form.cleaned_data.get('pcontact')
            user.profile.scontact = form.cleaned_data.get('scontact')
            user.profile.scontact = form.cleaned_data.get('scontact')
            user.profile.is_tenant = form.cleaned_data.get('is_tenant')
            user.profile.is_owner = form.cleaned_data.get('is_owner')
            user.profile.marital_status = form.cleaned_data.get(
                'marital_status')
            user.profile.nationality = form.cleaned_data.get(
                'nationality')
            user.save()
            messages.success(request, 'Account successfully added')
            return redirect('login')
        else:
            messages.error(
                request, 'There was a problem creating the account please check your inputs')
            return redirect('add_user')
    else:
        form = ProfileRegistrationForm()
    context = {
        "form": form,
    }

    return render(request, 'new_door/add_user.html', context)

# @login_required
# def add_user_to_unit(request, unit_id):
#     if request.method == "POST":
#         form = ProfileRegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             user.refresh_from_db()
#             user.profile.email = form.cleaned_data.get('email')
#             user.profile.mid_name = form.cleaned_data.get('mid_name')
#             user.profile.pcontact = form.cleaned_data.get('pcontact')
#             user.profile.scontact = form.cleaned_data.get('scontact')
#             user.profile.scontact = form.cleaned_data.get('scontact')
#             user.profile.is_tenant = form.cleaned_data.get('is_tenant')
#             user.profile.is_owner = form.cleaned_data.get('is_owner')
#             user.profile.marital_status = form.cleaned_data.get(
#                 'marital_status')
#             user.profile.nationality = form.cleaned_data.get(
#                 'nationality')
#             user.save()
#             messages.success(request, 'Account successfully added')
#             return redirect('login')
#         else:
#             messages.error(
#                 request, 'There was a problem creating the account please check your inputs')
#             return redirect('add_user')
#     else:
#         form = ProfileRegistrationForm()
#     context = {
#         "form": form,
#     }

#     return render(request, 'new_door/add_user.html', context)


@login_required
def add_category_type(request):

    categories = CategoryType.objects.all()

    if request.method == 'POST':
        form = CategoryTypeModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Congratulations...! Category type successfully added.')
            return redirect('add_category_type')
    else:
        form = CategoryTypeModelForm()

    context = {'form': form, 'categories': categories}

    return render(request, 'new_door/add_category_type.html', context)


@login_required
@login_required
def add_property_type(request):

    property_types = PropertyType.objects.all()
    categories = CategoryType.objects.all()

    if request.method == 'POST':
        form = PropertyTypeModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Congratulations...! Property type successfully added.')
            return redirect('add_property_type')

    else:
        form = PropertyTypeModelForm()

    context = {
        'form': form,
        'property_types': property_types,
        'categories': categories
    }

    return render(request, 'new_door/property_type.html', context)


@login_required
@login_required
def add_ownership_type(request):

    ownership_types = OwnershipType.objects.all()

    if request.method == 'POST':
        form = OwnershipTypeModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Congratulations...! Ownership type successfully added.')
            return redirect('add_ownership_type')
    else:
        form = OwnershipTypeModelForm()

    context = {
        'form': form,
        'ownership_types': ownership_types,
    }

    return render(request, 'new_door/add_ownership_type.html', context)


@login_required
@login_required
def add_occupancy_type(request):

    occupancy_types = OccupancyType.objects.all()

    if request.method == 'POST':
        form = OccupancyTypeModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Congratulations...! Ownership type successfully added.')
            return redirect('add_occupancy_type')
    else:
        form = OccupancyTypeModelForm()

    context = {
        'form': form,
        'occupancy_types': occupancy_types,
    }

    return render(request, 'new_door/add_occupancy_type.html', context)


@login_required
@login_required
def add_tetant_contract(request):
    # Todo: Make sure template has valid fields

    occupancy_types = OccupancyType.objects.all()

    if request.method == 'POST':
        form = TenantContractModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Congratulations...! Contract successfully added.')
            return redirect('add_tetant_contract')
    else:
        form = TenantContractModelForm()

    context = {
        'form': form,
        'occupancy_types': occupancy_types,
    }

    return render(request, 'new_door/tenant_contract.html', context)


@login_required
@login_required
def add_contract_request(request):

    tenants = Profile.objects.all()
    contract_requests = ContractReqType.objects.all()

    if request.method == 'POST':
        form = ContractReqTypeModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Congratulations...! Contract request type successfully added.')
            return redirect('add_contract_request')
    else:
        form = ContractReqTypeModelForm()

    context = {
        'form': form,
        'tenants': tenants,
        'contract_requests': contract_requests,
    }

    return render(request, 'new_door/add_contract_request.html', context)


@login_required
@login_required
def add_tenant_request(request):

    tenant_requests = TenantReqType.objects.all()

    if request.method == 'POST':
        form = TenantReqTypeModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Congratulations...! Tenant request type successfully added.')
            return redirect('add_tenant_request')
    else:
        form = TenantReqTypeModelForm()

    context = {
        'form': form,
        'tenant_requests': tenant_requests,
    }

    return render(request, 'new_door/add_tenant_request.html', context)


@login_required
def add_status_request(request):

    statuses = StatusReqType.objects.all()

    if request.method == 'POST':
        form = StatusReqTypeModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Congratulations...! Status request type successfully added.')
            return redirect('add_status_request')
    else:
        form = StatusReqTypeModelForm()

    context = {
        'form': form,
        'statuses': statuses
    }

    return render(request, 'new_door/add_status_request.html', context)


@login_required
def add_doc_type(request):

    docs = DocumentType.objects.all()

    if request.method == 'POST':
        form = DocumentTypeModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Congratulations...! Document type successfully added.')
            return redirect('add_doc_type')
    else:
        form = DocumentTypeModelForm()

    context = {
        'form': form,
        'docs': docs
    }

    return render(request, 'new_door/add_documents_type.html', context)


@login_required
def add_payment_mode(request):

    payment_modes = PayModeType.objects.all()

    if request.method == 'POST':
        form = PayModeTypeModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Congratulations...! Payment mode successfully added.')
            return redirect('add_payment_mode')
    else:
        form = PayModeTypeModelForm()

    context = {
        'form': form,
        'payment_modes': payment_modes,
    }

    return render(request, 'new_door/add_payment_mode.html', context)


""" Edit Views  """


def update_entity(request, id):

    entity = get_object_or_404(Entity, pk=id)

    if request.method == "POST":
        form = EntityModelForm(request.POST, instance=entity)

        if form.is_valid():
            form.save()
            messages.success(
                request, 'Congratulations...! Entity successfully updated.')
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
            request, 'Congratulations...! Property successfully updated.')
        return redirect('property_overview', _property.entity.entity_name)
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

    if request.method == "POST":
        form = UnitModelForm(request.POST, instance=unit)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Congratulations...! Unit successfully updated.')
            return redirect('property_unit_overview', unit.property_id.pk)
    else:
        form = UnitModelForm(instance=unit)

    context = {
        'form': form,
        'unit': unit,
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
                request, 'Congratulations...! Property Type successfully updated.')
            return redirect('add_property_type')
    else:
        form = PropertyTypeModelForm(instance=property_type)

    context = {
        "form": form,
        "categories": categories
    }

    return render(request, 'new_door/update_property_type.html', context)


# Code refactored - 6-12-2020 8.33PM- Patrick

def update_category_type(request, id):

    category_type = get_object_or_404(CategoryType, pk=id)

    if request.method == "POST":
        form = CategoryTypeModelForm(request.POST, instance=category_type)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Congratulations...! Category type successfully updated.')
            return redirect('add_category_type')
    else:
        form = CategoryTypeModelForm(instance=category_type)

    context = {
        "form": form,
        "category_type": category_type,
    }

    return render(request, 'new_door/update_category_type.html', context)


def update_ownership_type(request, id):

    ownership_type = get_object_or_404(OwnershipType, pk=id)

    if request.method == "POST":
        form = OwnershipTypeModelForm(request.POST, instance=ownership_type)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Congratulations...! Ownership type successfully updated.')
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
                request, 'Congratulations...! Occupancy type successfully updated.')
            return redirect('add_occupancy_type')
    else:
        form = OccupancyTypeModelForm(instance=occupancy_type)

    context = {
        "form": form,
    }

    return render(request, 'new_door/update_occupancy_type.html', context)


def update_contract_request(request, id):

    contract_request = get_object_or_404(ContractReqType, pk=id)
    tenant = get_object_or_404(Profile, pk=contract_request.tenant.pk)

    if request.method == "POST":
        form = ContractReqTypeModelForm(
            request.POST, instance=contract_request)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Congratulations...! Contract request type successfully updated.')
            return redirect('add_contract_request')
    else:
        form = ContractReqTypeModelForm(instance=contract_request)

    context = {
        "form": form,
        "tenant": tenant
    }

    return render(request, 'new_door/update_contract_request.html', context)


def update_tenant_request(request, id):

    tenant_request = get_object_or_404(TenantReqType, pk=id)

    if request.method == "POST":
        form = TenantReqTypeModelForm(
            request.POST, instance=tenant_request)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Congratulations...! Tenant request type successfully updated.')
            return redirect('add_tenant_request')
    else:
        form = TenantReqTypeModelForm(instance=tenant_request)

    context = {
        "form": form,
    }

    return render(request, 'new_door/update_tenant_request.html', context)


def update_status_request(request, id):

    status_request = get_object_or_404(StatusReqType, pk=id)

    if request.method == "POST":
        form = StatusReqTypeModelForm(
            request.POST, instance=status_request)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Congratulations...! Status request type successfully updated.')
            return redirect('add_status_request')
    else:
        form = StatusReqTypeModelForm(instance=status_request)

    context = {
        "form": form,
        "status_request": status_request
    }

    return render(request, 'new_door/update_status_request.html', context)


def update_doc_type(request, id):

    doc_type = get_object_or_404(DocumentType, pk=id)

    if request.method == "POST":
        form = DocumentTypeModelForm(
            request.POST, instance=doc_type)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Congratulations...! Document type successfully updated.')
            return redirect('add_doc_type')
    else:
        form = DocumentTypeModelForm(instance=doc_type)

    context = {
        "form": form,
        "doc_type": doc_type
    }

    return render(request, 'new_door/update_documents_type.html', context)


def update_payment_mode(request, id):

    payment_mode = get_object_or_404(PayModeType, pk=id)

    if request.method == "POST":
        form = PayModeTypeModelForm(
            request.POST, instance=payment_mode)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Congratulations...! Payment mode successfully updated.')
            return redirect('add_payment_mode')
    else:
        form = PayModeTypeModelForm(instance=payment_mode)

    context = {
        "form": form,
        "payment_mode": payment_mode
    }

    return render(request, 'new_door/update_payment_mode.html', context)


""" Delete Views """

# Code refactored - 26-11-2020 11.33PM- Patrick


def delete_entity(request, id):
    entity = get_object_or_404(Entity, pk=id)
    entity.delete()
    messages.success(
        request, 'Congratulations...! Entity successfully deleted.')
    return redirect('entity_overview')

# Code refactored - 27-11-2020 5.30PM- Patrick


def delete_property(request, id):
    _property = Property.objects.get(pk=id)
    _property.delete()
    messages.success(
        request, 'Congratulations...! Property successfully deleted.')
    return redirect('property_all_overview')


def delete_unit(request, id):
    unit = Unit.objects.get(pk=id)
    unit.delete()
    messages.success(
        request, 'Congratulations...! Unit successfully deleted.')
    return redirect('unit_overview')


def delete_category_type(request, id):
    category_type = CategoryType.objects.get(pk=id)
    category_type.delete()
    messages.success(
        request, 'Congratulations...! Category Type successfully deleted.')
    return redirect('add_category_type')

# Code refactored - 27-11-2020 11.45PM- Patrick


def delete_property_type(request, id):
    property_type = PropertyType.objects.get(pk=id)
    property_type.delete()
    messages.success(
        request, 'Congratulations...! Property Type successfully deleted.')
    return redirect('add_property_type')


def delete_ownership_type(request, id):
    ownership_type = OwnershipType.objects.get(pk=id)
    ownership_type.delete()
    messages.success(
        request, 'Congratulations...! Ownership Type successfully deleted.')
    return redirect('add_ownership_type')


def delete_occupancy_type(request, id):
    occupancy_type = OccupancyType.objects.get(pk=id)
    occupancy_type.delete()
    messages.success(
        request, 'Congratulations...! Occupancy type successfully deleted.')
    return redirect('add_occupancy_type')


# Code refactored - 6-12-2020 9.40PM- Patrick

def delete_contract_request(request, id):

    contract_request = get_object_or_404(ContractReqType, pk=id)
    contract_request.delete()
    messages.success(
        request, 'Congratulations...! Contract request type successfully deleted.')

    return redirect('add_contract_request')


def delete_tenant_request(request, id):

    tenant_request = get_object_or_404(TenantReqType, pk=id)
    tenant_request.delete()
    messages.success(
        request, 'Congratulations...! Tenant request type successfully deleted.')
    return redirect('add_tenant_request')


def delete_status_request(request, id):

    status_request = get_object_or_404(StatusReqType, pk=id)
    status_request.delete()
    messages.success(
        request, 'Congratulations...! Status request type successfully deleted.')
    return redirect('add_status_request')


def delete_doc_type(request, id):

    doc_type = get_object_or_404(DocumentType, pk=id)
    doc_type.delete()
    messages.success(
        request, 'Congratulations...! Document type successfully deleted.')
    return redirect('add_doc_type')


def delete_payment_mode(request, id):

    payment_mode = get_object_or_404(PayModeType, pk=id)
    payment_mode.delete()
    messages.success(
        request, 'Congratulations...! Payment mode successfully deleted.')
    return redirect('add_payment_mode')


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
        'unit': unit,
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

def view_category_type(request, id):

    category_type = get_object_or_404(CategoryType, pk=id)
    form = OwnershipTypeModelForm(instance=category_type)

    context = {
        "form": form,
        "category_type": category_type,
    }

    return render(request, 'new_door/view_category_type.html', context)


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

# Todo//-link with template


def view_contract_request(request, id):

    contract_request = get_object_or_404(ContractReqType, pk=id)
    tenant = get_object_or_404(Profile, pk=contract_request.tenant.pk)

    form = ContractReqTypeModelForm(instance=contract_request)

    context = {
        "form": form,
        "tenant": tenant
    }

    return render(request, 'new_door/view_contract_request.html', context)


def view_tenant_request(request, id):

    tenant_request = get_object_or_404(TenantReqType, pk=id)
    form = TenantReqTypeModelForm(instance=tenant_request)

    context = {
        "form": form,
        "tenant_request": tenant_request,
    }

    return render(request, 'new_door/view_tenant_request.html', context)


def view_status_request(request, id):

    status_request = get_object_or_404(StatusReqType, pk=id)
    form = StatusReqTypeModelForm(instance=status_request)

    context = {
        "form": form,
        "status_request": status_request
    }

    return render(request, 'new_door/view_status_request.html', context)


def view_doc_type(request, id):

    doc_type = get_object_or_404(DocumentType, pk=id)
    form = DocumentTypeModelForm(instance=doc_type)

    context = {
        "form": form,
        "doc_type": doc_type
    }

    return render(request, 'new_door/view_documents_type.html', context)


def view_payment_mode(request, id):

    payment_mode = get_object_or_404(PayModeType, pk=id)
    form = PayModeTypeModelForm(instance=payment_mode)

    context = {
        "form": form,
        "payment_mode": payment_mode
    }

    return render(request, 'new_door/view_payment_mode.html', context)


""" Propery Unit Views """

# Code refactored - 28-11-2020 11.53PM- Patrick

# Check property to display


def prepopulated_field_unit(request, id):
    _property = get_object_or_404(Property, pk=id)

    property_types = PropertyType.objects.all()
    ownership_types = OwnershipType.objects.all()
    occupancy_types = OccupancyType.objects.all()

    if request.method == 'POST':
        form = UnitModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Congratulations...! Unit successfully added.')
            return redirect('property_unit_overview', _property.pk)
    else:
        data = {
            'product_id': _property
        }
        form = UnitModelForm(request.POST, initial=data)

    context = {
        'form': form,
        'property': _property,
        'property_types': property_types,
        'ownership_types': ownership_types,
        'occupancy_types': occupancy_types,
    }

    return render(request, 'new_door/add_property_unit.html', context)


def property_unit_overview(request, id):
    _property = get_object_or_404(Property, pk=id)
    units = Unit.objects.filter(property_id=_property.pk)

    number_of_vacant_units = Unit.objects.filter(
        occupancy_type__occupancy_type__iexact="vacant", property_id=_property).count()
    number_of_occupied_units = Unit.objects.filter(
        occupancy_type__occupancy_type__iexact="occupied",
        property_id=_property).count()

    if number_of_occupied_units is None:
        number_of_occupied_units = 0

    context = {
        'property': _property,
        'units': units,
        'number_of_vacant_units': number_of_vacant_units,
        'number_of_occupied_units': number_of_occupied_units,
    }

    return render(request, 'new_door/property_unit_overview.html', context)
