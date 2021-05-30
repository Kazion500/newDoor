from tenant.forms import TenantContractModelForm
from django.db.models.query_utils import Q
from django.http.response import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
import stripe


from new_door.models import (
    Entity, Property, TenantDocument,
    Unit, Profile, PropertyType,
    OccupancyType, OwnershipType,
    DocumentType
)
from payment.models import Payment
from tenant.models import TenantContract

from new_door.forms import (
    EntityModelForm,
    PropertyModelForm,
    UnitModelForm,
    UploadDocumentModelForm,
)


# stripe.api_key = config('STRIPE_SECRET_KEY')
stripe.api_key = 'sk_test_51I0mEFGz8qAcurV0PCi7DH9LM4fx9QghxgAxnV9eWAP1gmllKeSzmSIbDvU0THz6i0HzP7EdXHxBTVtbo1HHYd8u00lnHS3VYg'


@login_required
def dashboard_view(request):
    manager_id = request.user.pk
    if request.user.is_tenant:
        return redirect('tenant_dashboard')

    # get payment and property related to manager
    payments = Payment.objects.filter(
        unit__property_id__entity__manager__pk=manager_id)
    properties = Property.objects.filter(
        entity__manager__pk=manager_id).order_by('-property_name')[:4]

    tenant_payments = payments.order_by('-paid_date')[:4]
    total_payments = payments.aggregate(amount=Sum("amount"))
    due_payments = payments.aggregate(due=Sum("remain_amount"))

    total_num_units = Unit.objects.filter(
        property_id__entity__manager__pk=manager_id).count()
    units = Unit.objects.filter(
        Q(property_id__entity__manager__pk=manager_id),
        Q(tenantcontract__gte=1)
    ).order_by('occupancy_type')[:4]

    vacant_units = Unit.objects.filter(
        occupancy_type__occupancy_type__iexact="vacant").count()

    context = {
        'total_num_units': total_num_units,
        'vacant_units': vacant_units,
        'units': units,
        'properties': properties,
        'tenant_payments': tenant_payments,
        'total_payments': total_payments,
        'due_payments': due_payments,
    }
    return render(request, 'new_door/dashboard.html', context)


@login_required
def entity_overview(request):
    entities = Entity.objects.filter(manager__pk=request.user.pk)
    context = {
        'entities': entities
    }
    return render(request, 'new_door/entity_overview.html', context)


@login_required
def property_overview(request, entity):
    total_earnings = 0
    all_units_amount = 0
    due_amount = 0

    entity = get_object_or_404(Entity, entity_name=entity)
    properties = Property.objects.filter(
        Q(entity__entity_name=entity),
        Q(entity__manager__pk=request.user.pk)
    )

    number_of_units = Unit.objects.filter(
        property_id__entity__entity_name=entity).count()

    number_of_vacant_units = Unit.objects.filter(
        Q(occupancy_type__occupancy_type__iexact="vacant"),
        Q(property_id__entity__entity_name=entity)).count()

    number_of_occupied_units = Unit.objects.filter(
        occupancy_type__occupancy_type__iexact="occupied",
        property_id__entity__entity_name=entity).count()

    if number_of_occupied_units:
        percentage = number_of_occupied_units / number_of_units * 100
    else:
        percentage = 0

    # Help calculate due amount
    try:
        all_units_amount = Unit.tenantcontract.get_queryset().filter(
            property_id__entity__entity_name=entity).aggregate(rent=Sum('annual_rent'))
        total_earnings = Payment.objects.filter(
            contract__unit__property_id__entity__entity_name=entity).aggregate(amount=Sum('amount'))

    except:
        pass
    if all_units_amount['rent'] and total_earnings['amount']:
        due_amount = int(all_units_amount['rent']) - int(total_earnings['amount'])

    if due_amount == None:
        due_amount = 0

    context = {
        'entity': entity,
        'properties': properties,
        'number_of_units': number_of_units,
        'number_of_occupied_units': number_of_occupied_units,
        'number_of_vacant_units': number_of_vacant_units,
        'percentage': int(percentage),
        "total_earnings": total_earnings,
        "all_units_amount": all_units_amount,
        "due_amount": due_amount
    }

    return render(request, 'new_door/property_overview.html', context)


@login_required
def property_all_overview(request):
    total_earnings = 0
    all_units_amount = 0
    due_amount = 0

    # TODO: // add user roles

    properties = Property.objects.filter(
        Q(entity__manager__pk=request.user.pk)
    )
    number_of_units = Unit.objects.all().count()

    number_of_vacant_units = Unit.objects.exclude(
        occupancy_type__occupancy_type__iexact="occupied").count()
    number_of_occupied_units = Unit.objects.filter(
        occupancy_type__occupancy_type__iexact="occupied").count()

    if number_of_occupied_units:
        percentage = number_of_occupied_units / number_of_units * 100
    else:
        percentage = 0

    # Help calculate due amount
    try:
        all_units_amount = Unit.tenantcontract.get_queryset(
        ).aggregate(rent=Sum('annual_rent'))
        total_earnings = Payment.objects.all().aggregate(amount=Sum('amount'))
    except:
        pass
    
    if all_units_amount['rent'] and total_earnings['amount']:
        due_amount = int(all_units_amount['rent']) - int(total_earnings['amount'])

    if due_amount == None:
        due_amount = 0

    context = {
        'properties': properties,
        'number_of_units': number_of_units,
        'number_of_occupied_units': number_of_occupied_units,
        'number_of_vacant_units': number_of_vacant_units,
        'percentage': int(percentage),
        'all_units_amount': all_units_amount,
        "total_earnings": total_earnings,
        "due_amount": due_amount,
    }

    return render(request, 'new_door/property_all_overview.html', context)


def property_unit_overview(request, id):
    total_earning = 0
    num_of_docs = 0

    _property = get_object_or_404(Property, pk=id)
    units = Unit.objects.filter(property_id=_property.pk)

    number_of_vacant_units = Unit.objects.exclude(
        occupancy_type__occupancy_type__iexact="occupied").filter(property_id__id=id).count()
    number_of_occupied_units = Unit.objects.filter(
        occupancy_type__occupancy_type__iexact="occupied", property_id=_property).count()

    try:
        total_earning = Payment.objects.filter(
            contract__unit__property_id__pk=id).aggregate(amount=Sum('amount'))
        num_of_docs = DocumentType.objects.all().aggregate(docs=Sum('num_of_doc'))
    except:
        pass

    if number_of_occupied_units is None:
        number_of_occupied_units = 0

    context = {
        'property': _property,
        'units': units,
        "total_earning": total_earning,
        'number_of_vacant_units': number_of_vacant_units,
        'number_of_occupied_units': number_of_occupied_units,
        'num_of_docs': num_of_docs,
    }

    return render(request, 'new_door/property_unit_overview.html', context)


@login_required
def unit_overview(request):
    total_earning = 0
    num_of_docs = 0

    units = Unit.objects.all()
    number_of_vacant_units = Unit.objects.exclude(
        occupancy_type__occupancy_type__iexact="occupied").count()
    number_of_occupied_units = Unit.objects.filter(
        occupancy_type__occupancy_type__iexact="occupied").count()

    try:
        total_earning = Payment.objects.all().aggregate(amount=Sum('amount'))
        num_of_docs = DocumentType.objects.all().aggregate(docs=Sum('num_of_doc'))

    except:
        pass

    if number_of_occupied_units is None:
        number_of_occupied_units = 0

    context = {
        'units': units,
        "total_earning": total_earning,
        'number_of_occupied_units': number_of_occupied_units,
        'number_of_vacant_units': number_of_vacant_units,
        'num_of_docs': num_of_docs,
    }

    return render(request, 'new_door/unit_overview.html', context)


@login_required
def upload_documents(request, user):
    tenant_contract = ''
    property_owner = ''
    tenant = get_object_or_404(Profile, user__username__iexact=user)
    uploaded_documents = TenantDocument.objects.filter(tenant=tenant)
    doc_type = DocumentType.objects.all()
    # uploaded_documents = DocumentType.objects.filter(uploaddocument__doc_type=uploaded_document.doc_type)

    try:
        tenant_contract = TenantContract.objects.get(
            tenant__user__username=user)
        property_owner = Property.objects.get(
            pk=tenant_contract.property_id_id)

    except TenantContract.DoesNotExist:
        messages.info(
            request, 'You dont have a contract please contact your real estate manager')
        return redirect('tenant_dashboard')

    if request.method == "POST":
        form = UploadDocumentModelForm(request.POST, request.FILES)

        if form.is_valid():
            uploaded_doc = form.save(commit=False)
            current_doc_type = DocumentType.objects.get(
                pk=uploaded_doc.doc_type.pk)
            uploaded_documents_to_check = TenantDocument.objects.filter(
                tenant=tenant, doc_type=current_doc_type)
            doc_id = int(form.data.get('doc_type'))

            # validate if the user is uploading the same document multiple times
            if doc_id == uploaded_doc.doc_type.pk and uploaded_documents_to_check.count() == current_doc_type.num_of_doc:
                messages.error(
                    request, f'You have already upload the documents with document type of {uploaded_doc.doc_type.docs_type} and reach the maximum number of uploads for this type of document')
                return redirect('upload_documents', tenant.user.username)

            # validate the number of doc against the required
            if not uploaded_documents_to_check.count() < current_doc_type.num_of_doc:
                messages.error(
                    request, f'You have reacted the maximum number of uploads for this type of document')
                return redirect('upload_documents', tenant.user.username)

            elif uploaded_documents_to_check.count() == current_doc_type.num_of_doc:
                messages.error(
                    request, f'You have reacted the maximum number of uploads for this type of document')
                return redirect('upload_documents', tenant.user.username)

            for image in request.FILES.getlist('image'):
                credentials = TenantDocument(
                    tenant=uploaded_doc.tenant, image=image, doc_type=uploaded_doc.doc_type)
                credentials.save()
            messages.success(
                request, 'Congratulations...! Documents uploaded successfully.')

            msg_to_owner = f"Hello Admin,\nDocuments for {user} are ready make sure you verify them"
            
            # add new query
            # if property_owner.owner_name.user.email:
            #     send_mail(
            #         'New Door Contract',
            #         msg_to_owner,
            #         'noreply@newdoor.com',
            #         [property_owner.owner_name.user.email],
            #         fail_silently=False,
            #     )
            return redirect('upload_documents', tenant.user.username)
    else:
        form = UploadDocumentModelForm()

    context = {
        "form": form,
        "uploaded_documents": uploaded_documents,
        "doc_types": doc_type,
        "tenant": tenant

    }
    return render(request, 'tenant/upload_document.html', context)


def review_documents(request, user):
    # TODO:// add authorization
    tenant = get_object_or_404(Profile, user__username=user)
    tenant_contract = get_object_or_404(TenantContract, tenant=tenant)
    tenant_docs = TenantDocument.objects.filter(tenant=tenant)

    if request.method == 'POST':
        form = TenantContractModelForm(request.POST, instance=tenant_contract)
        if form.is_valid():
            contract_no = form.cleaned_data['contract_no']
            form.save()
            messages.success(
                request, 'Congratulations...! Documents uploaded successfully.')
            return redirect('add_tetant_contract')
    else:
        form = TenantContractModelForm(instance=tenant_contract)

    context = {
        'form': form,
        "tenant_contract": tenant_contract,
        "tenant_docs": tenant_docs
    }
    return render(request, 'tenant/review_documents.html', context)


def verify_documents(request, user):
    tenant = get_object_or_404(Profile, user__username=user)
    tenant_contract = TenantContract.objects.get(tenant__user__username=user)
    tenant_docs = TenantDocument.objects.filter(tenant=tenant)
    unit = Unit.objects.get(tenantcontract__tenant__user__username=user)

    try:
        tenant_doc = TenantDocument.objects.filter(tenant=tenant)[0]
    except:
        return redirect('unit_overview')

    occupancy_type_ = OccupancyType.objects.get(
        occupancy_type='Create Contract')

    if request.method == 'POST':
        user = request.POST.get('user')
        operation = request.POST.get('operation')
        filename = request.POST.get('filename')
        doc_id = request.POST.get('docId')
        tenant_email = tenant_doc.tenant.user.email

        if operation == 'delete':
            tenant_imgs = TenantDocument.objects.filter(
                tenant__user__username=user)
            for tenant_img in tenant_imgs:
                doc_type = tenant_img.doc_type
                doc_types = DocumentType.objects.get(pk=doc_type.pk)
                docs = TenantDocument.objects.filter(doc_type=doc_types)
                for doc in docs:
                    if doc.pk == int(doc_id):
                        doc.delete()
                    messages.success(
                        request, 'Sorry...! Your documents were rejected successfully')

            msg_error = f"Hi {user} \n document of type {filename} has been rejected because its not clear. \n "
            send_mail(
                'Documents Rejected',
                msg_error,
                'noreply@newdoor.com',
                [tenant_email],
                fail_silently=False,
            )

        elif operation == 'save':
            tenant_img = ''
            tenant_imgs = TenantDocument.objects.filter(
                tenant__user__username=user)

            for tenant_img in tenant_imgs:
                server_file = tenant_img.image.name
                if server_file == filename:
                    tenant_img.is_verified = True
                    tenant_img.save()

            unit.occupancy_type = occupancy_type_
            unit.save()
            messages.success(
                request, 'Congratulations...! Documents verified successfully')

            msg = f"Hi {user} \n {filename} have been accepted. \n Kindly login to the dashboard and proceed with the making payment"
            send_mail(
                'Documents Approved',
                msg,
                'noreply@newdoor.com',
                [tenant_email],
                fail_silently=False,
            )
            return JsonResponse({'message': 'verified', 'user': user, 'file': tenant_img.image.name})

    context = {
        "tenant_docs": tenant_docs,
        "tenant_doc": tenant_doc,
        'tenant': tenant
    }
    return render(request, 'tenant/verify_document.html', context)

# TODO//: add functionality


""" Add Views  """


@login_required
def add_entity(request):
    manager = request.user
    entities = Entity.objects.all()

    if request.method == 'POST':
        form = EntityModelForm(request.POST)
        if form.is_valid():
            entity = form.save(commit=False)
            entity.manager = manager
            entity.save()
            messages.success(
                request, 'Congratulations...! Entity successfully added.')
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

    if request.method == 'POST':
        form = PropertyModelForm(request.POST)
        print(form.errors)

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
    }

    return render(request, 'new_door/add_property.html', context)


@login_required
def add_property_all(request):
    entities = Entity.objects.all()

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
            messages.error(
                request, 'Make sure all fields are filled')
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


def upload_doc_delete(request, doc_id):
    uploaded_document = TenantDocument.objects.filter(pk=doc_id)
    uploaded_document.delete()
    return redirect('upload_documents', request.user.username)


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
