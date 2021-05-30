from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from app_config.forms import CategoryTypeModelForm, ContractReqTypeModelForm, DocumentTypeModelForm, OccupancyTypeModelForm, OwnershipTypeModelForm, PayModeTypeModelForm, PropertyTypeModelForm, StatusReqTypeModelForm, TenantReqTypeModelForm
from app_config.models import CategoryType, ContractReqType, DocumentType, OccupancyType, OwnershipType, PayModeType, PropertyType, StatusReqType, TenantReqType
from profiles.models import Profile

# Create your views here.


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

    return render(request, 'app_config/add_category_type.html', context)


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

    return render(request, 'app_config/property_type.html', context)


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

    return render(request, 'app_config/add_ownership_type.html', context)


@login_required
def add_occupancy_type(request):

    occupancy_types = OccupancyType.objects.all()

    if request.method == 'POST':
        form = OccupancyTypeModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Congratulations...! Occupancy type successfully added.')
            return redirect('add_occupancy_type')
    else:
        form = OccupancyTypeModelForm()

    context = {
        'form': form,
        'occupancy_types': occupancy_types,
    }

    return render(request, 'app_config/add_occupancy_type.html', context)


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

    return render(request, 'app_config/add_contract_request.html', context)


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

    return render(request, 'app_config/add_tenant_request.html', context)


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

    return render(request, 'app_config/add_status_request.html', context)


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

    return render(request, 'app_config/add_documents_type.html', context)


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

    return render(request, 'app_config/add_payment_mode.html', context)


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

    return render(request, 'app_config/update_property_type.html', context)


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

    return render(request, 'app_config/update_category_type.html', context)


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

    return render(request, 'app_config/update_ownership_type.html', context)


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

    return render(request, 'app_config/update_occupancy_type.html', context)


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

    return render(request, 'app_config/update_contract_request.html', context)


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

    return render(request, 'app_config/update_tenant_request.html', context)


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

    return render(request, 'app_config/update_status_request.html', context)


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

    return render(request, 'app_config/update_documents_type.html', context)


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

    return render(request, 'app_config/update_payment_mode.html', context)


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


def view_property_type(request, id):

    property_type = get_object_or_404(PropertyType, pk=id)
    categories = CategoryType.objects.all()

    form = PropertyTypeModelForm(instance=property_type)

    context = {
        "form": form,
        "categories": categories
    }

    return render(request, 'app_config/view_property_type.html', context)


# Code refactored - 28-11-2020 9.53PM- Patrick

def view_category_type(request, id):

    category_type = get_object_or_404(CategoryType, pk=id)
    form = OwnershipTypeModelForm(instance=category_type)

    context = {
        "form": form,
        "category_type": category_type,
    }

    return render(request, 'app_config/view_category_type.html', context)


def view_ownership_type(request, id):

    ownership_type = get_object_or_404(OwnershipType, pk=id)
    form = OwnershipTypeModelForm(instance=ownership_type)

    context = {
        "form": form,
    }

    return render(request, 'app_config/view_ownership_type.html', context)


def view_occupancy_type(request, id):

    occupancy_type = get_object_or_404(OccupancyType, pk=id)
    form = OccupancyTypeModelForm(instance=occupancy_type)

    context = {
        "form": form,
    }

    return render(request, 'app_config/view_occupancy_type.html', context)

# Todo//-link with template


def view_contract_request(request, id):

    contract_request = get_object_or_404(ContractReqType, pk=id)
    tenant = get_object_or_404(Profile, pk=contract_request.tenant.pk)

    form = ContractReqTypeModelForm(instance=contract_request)

    context = {
        "form": form,
        "tenant": tenant
    }

    return render(request, 'app_config/view_contract_request.html', context)


def view_tenant_request(request, id):

    tenant_request = get_object_or_404(TenantReqType, pk=id)
    form = TenantReqTypeModelForm(instance=tenant_request)

    context = {
        "form": form,
        "tenant_request": tenant_request,
    }

    return render(request, 'app_config/view_tenant_request.html', context)


def view_status_request(request, id):

    status_request = get_object_or_404(StatusReqType, pk=id)
    form = StatusReqTypeModelForm(instance=status_request)

    context = {
        "form": form,
        "status_request": status_request
    }

    return render(request, 'app_config/view_status_request.html', context)


def view_doc_type(request, id):

    doc_type = get_object_or_404(DocumentType, pk=id)
    form = DocumentTypeModelForm(instance=doc_type)

    context = {
        "form": form,
        "doc_type": doc_type
    }

    return render(request, 'app_config/view_documents_type.html', context)


def view_payment_mode(request, id):

    payment_mode = get_object_or_404(PayModeType, pk=id)
    form = PayModeTypeModelForm(instance=payment_mode)

    context = {
        "form": form,
        "payment_mode": payment_mode
    }

    return render(request, 'app_config/view_payment_mode.html', context)
