from django.http.response import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMultiAlternatives, send_mail
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.template.loader import render_to_string
from .utils import account_activation_token
from django.urls import reverse
import stripe
import datetime
from datetime import timezone, date


from .models import (
    Entity, Property,
    Unit, CategoryType,
    Profile, PropertyType,
    OccupancyType, OwnershipType,
    DocumentType, PayModeType,
    StatusReqType, TenantReqType,
    ContractReqType, TenantContract,
    UploadDocument, Payment

)
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
    ProfileRegistrationForm,
    UploadDocumentModelForm,
)


# stripe.api_key = config('STRIPE_SECRET_KEY')
stripe.api_key = 'sk_test_51I0mEFGz8qAcurV0PCi7DH9LM4fx9QghxgAxnV9eWAP1gmllKeSzmSIbDvU0THz6i0HzP7EdXHxBTVtbo1HHYd8u00lnHS3VYg'


# Dashboard Rendering


@login_required
def dashboard_view(request):
    if request.user.profile.is_tenant:
        return redirect('tenant_dashboard')

    total_num_units = Unit.objects.all().count()
    vacant_units = Unit.objects.filter(
        occupancy_type__occupancy_type__iexact="vacant").count()

    context = {
        'total_num_units': total_num_units,
        'vacant_units': vacant_units
    }
    return render(request, 'new_door/dashboard.html', context)


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

    if number_of_occupied_units:
        percentage = number_of_occupied_units / number_of_units * 100
    else:
        percentage = 0

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

    if number_of_occupied_units:
        percentage = number_of_occupied_units / number_of_units * 100
    else:
        percentage = 0

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

    collected_amount = 0
    remain_amount = 0

    units = Unit.objects.all()
    number_of_vacant_units = Unit.objects.filter(
        occupancy_type__occupancy_type__iexact="vacant").count()
    number_of_occupied_units = Unit.objects.filter(
        occupancy_type__occupancy_type__iexact="occupied").count()

    for unit in units:
        for payment in unit.tenantcontract.payment_set.all():
            collected_amount += payment.amount
            remain_amount = payment.remain_amount


    if number_of_occupied_units is None:
        number_of_occupied_units = 0

    context = {
        'units': units,
        "collected_amount": collected_amount,
        "remain_amount": remain_amount,
        'number_of_occupied_units': number_of_occupied_units,
        'number_of_vacant_units': number_of_vacant_units,
    }

    return render(request, 'new_door/unit_overview.html', context)


@login_required
def checklist(request):
    return render(request, 'new_door/checklist.html')


@login_required
def upload_documents(request, user):
    tenant = get_object_or_404(Profile, user__username__iexact=user)
    uploaded_documents = UploadDocument.objects.filter(tenant=tenant)
    doc_type = DocumentType.objects.all()
    # uploaded_documents = DocumentType.objects.filter(uploaddocument__doc_type=uploaded_document.doc_type)

    if request.method == "POST":
        form = UploadDocumentModelForm(request.POST, request.FILES)

        if form.is_valid():
            uploaded_doc = form.save(commit=False)
            for image in request.FILES.getlist('image'):
                credentials = UploadDocument(
                    tenant=uploaded_doc.tenant, image=image, doc_type=uploaded_doc.doc_type)
                credentials.save()
            messages.success(
                request, 'Congratulations...! Documents uploaded successfully.')
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
    tenant = get_object_or_404(Profile, user__username=user)
    tenant_contract = get_object_or_404(TenantContract, tenant=tenant)
    tenant_docs = UploadDocument.objects.filter(tenant=tenant)
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
    tenant_docs = UploadDocument.objects.filter(tenant=tenant)
    tenant_doc = UploadDocument.objects.filter(tenant=tenant)[0]
    unit = Unit.objects.get(tenantcontract__tenant__user__username=user)
    # occupancy_type_ = OccupancyType.objects.get(
    #     occupancy_type='Payment Pending')
    occupancy_type_ = OccupancyType.objects.get(
        occupancy_type='Create Contract')

    if request.method == 'POST':
        user = request.POST.get('user')
        operation = request.POST.get('operation')
        filename = request.POST.get('filename')
        tenant_email = tenant_doc.tenant.user.email

        if operation == 'delete':
            tenant_imgs = UploadDocument.objects.filter(
                tenant__user__username=user)
            for tenant_img in tenant_imgs:
                server_file = tenant_img.image.name
                if server_file == filename:
                    tenant_img.delete()

            # msg_error = f"Hi {user} \n document of type {filename} has been rejected because its not clear. \n "
            # send_mail(
            #     'Documents Rejected',
            #     msg_error,
            #     'noreply@newdoor.com',
            #     [tenant_email],
            #     fail_silently=False,
            # )

        elif operation == 'save':
            tenant_img = ''
            tenant_imgs = UploadDocument.objects.filter(
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

            # msg = f"Hi {user} \n {filename} have been accepted. \n Kindly login to the dashboard and proceed with the making payment"
            # send_mail(
            #     'Documents Approved',
            #     msg,
            #     'noreply@newdoor.com',
            #     [tenant_email],
            #     fail_silently=False,
            # )
            return JsonResponse({'message': 'verified', 'user': user, 'file': tenant_img.image.name})

    context = {
        # 'form': form,
        "tenant_docs": tenant_docs,
        "tenant_doc": tenant_doc,
        'tenant': tenant
    }
    return render(request, 'tenant/verify_document.html', context)


@login_required
def payment(request, user):
    unit_amount = TenantContract.objects.get(
        tenant__user__username=user).unit.rent_amount
    security_dep = TenantContract.objects.get(
        tenant__user__username=user).security_dep
    commission = TenantContract.objects.get(
        tenant__user__username=user).commission
    installment = TenantContract.objects.get(
        tenant__user__username=user).installments

    # Sum of the amount to be paid
    final_amount = int(security_dep) + int(commission) + int(unit_amount)

    tenant_contract = TenantContract.objects.get(
        tenant__user__username=user)

    profile = Profile.objects.get(user__username=user)

    if request.method == "POST":
        customer = stripe.Customer.create(
            name=request.POST.get('fullname'),
            email=request.POST.get('email'),
            source=request.POST.get('stripeToken')
        )
        rental_amount = stripe.Charge.create(
            customer=customer,
            amount=int(final_amount) * 100 // int(installment),
            currency="usd",
            receipt_email=request.POST.get('email'),
        )
        if rental_amount.paid:
            unit_contract = Unit.objects.get(tenantcontract__tenant=profile)
            occupancy = OccupancyType.objects.get(
                occupancy_type__iexact="Occupied")
            # occupancy = OccupancyType.objects.get(
            #     occupancy_type__iexact="Create Contract")
            unit_contract.occupancy_type = occupancy
            unit_contract.save()

            messages.success(
                request, f'Payment of ${rental_amount.amount / 100} has been made successfully')
            paid_amount = rental_amount.amount / 100
            remain_amount = int(final_amount) - paid_amount

            try:
                payments = Payment.objects.filter(contract=tenant_contract)
                for payment in payments:
                    print(dir(payment))
                    r_amount = payment.remain_amount
                    p_amount = payment.amount
                    remain_amount = r_amount - p_amount

                Payment.objects.create(
                    contract=tenant_contract,
                    amount=paid_amount,
                    status='Completed',
                    remain_amount=remain_amount,
                    remarks='Paid'
                )
            except Payment.DoesNotExist:
                intial_payment = Payment(
                    contract=tenant_contract,
                    amount=paid_amount,
                    status='Completed',
                    remain_amount=remain_amount,
                    remarks='Paid'
                )
                intial_payment.save()

                # print(intial_payment.amount)
                # if intial_payment.remain_amount == 0:
                #     messages.info(request, 'Payment completed')

            msg_success = f"Hi {user} \n You have made a payment of ${rental_amount.amount // 100} to new door real estate"
            send_mail(
                f'Payment Done for unit flat number {unit_contract.flat}',
                msg_success,
                'noreply@newdoor.com',
                [profile.user.email],
                fail_silently=False,
            )

            return redirect('payment', profile.user.username)

        else:
            messages.error(
                request, 'There was a problem  making your payment make sure you details are correct')

    return render(request, 'payment/payment.html')


""" Add Views  """


@login_required
def add_entity(request):
    entities = Entity.objects.all()

    if request.method == 'POST':
        form = EntityModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Congratulations...! Entity successfully added.')
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
        form = ProfileRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            firstname = form.cleaned_data.get('first_name')
            lastname = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')

            user = User.objects.create_user(
                username=username,
                email=email,
                first_name=firstname,
                last_name=lastname
            )
            user.set_password(password)
            user.profile.mid_name = form.cleaned_data.get('mid_name')
            user.profile.pcontact = form.cleaned_data.get('pcontact')
            user.profile.scontact = form.cleaned_data.get('scontact')
            user.profile.is_tenant = form.cleaned_data.get('is_tenant')
            user.profile.is_owner = form.cleaned_data.get('is_owner')
            user.profile.marital_status = form.cleaned_data.get(
                'marital_status')
            user.profile.nationality = form.cleaned_data.get('nationality')
            user.profile.image = form.cleaned_data.get('image')
            user.is_active = False
            user.save()

            current_site = get_current_site(request)

            email_body = {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            }
            link = reverse('activate', kwargs={
                'uidb64': email_body['uid'], 'token': email_body['token']})

            email_subject = 'Activate your account'

            activate_url = 'http://'+current_site.domain+link

            html_content_template = render_to_string(
                'auth/email_verification_msg.html', {"link": activate_url, "username": user.username.upper()})
            email = EmailMultiAlternatives(
                email_subject,
                html_content_template,
                'noreply@newdoor.com',
                [email],
            )
            email.attach_alternative(html_content_template, "text/html")
            email.send(fail_silently=False)

            messages.success(request, 'Account created successfully')
            return redirect('login')

    else:
        form = ProfileRegistrationForm()
    context = {
        "form": form,
    }

    return render(request, 'new_door/add_user.html', context)


def email_verification(request, uidb64, token):
    try:
        id = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=id)

        if not account_activation_token.check_token(user, token):
            return redirect('login'+'?message='+'User already activated')

        if user.is_active:
            return redirect('login')
        user.is_active = True
        user.save()

        tenant = Profile.objects.get(user=user)
        tenant_contract = TenantContract.objects.get(tenant=tenant)
        occupancy_type = OccupancyType.objects.get(
            occupancy_type__iexact="Document Pending")
        unit = tenant_contract.unit
        acctual_unit = Unit.objects.get(pk=unit.pk)
        acctual_unit.occupancy_type = occupancy_type
        acctual_unit.save()

        messages.success(request, 'Account activated successfully')
        return redirect('login')

    except Exception as ex:
        pass

    return redirect('login')

# @login_required


@login_required
def add_tenant_to_unit(request, unit_id):
    unit = Unit.objects.get(pk=unit_id)

    if request.method == "POST":
        form = ProfileRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            firstname = form.cleaned_data.get('first_name')
            lastname = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')

            user = User.objects.create_user(
                username=username,
                email=email,
                first_name=firstname,
                last_name=lastname
            )
            user.set_password(password)
            user.profile.mid_name = form.cleaned_data.get('mid_name')
            user.profile.pcontact = form.cleaned_data.get('pcontact')
            user.profile.scontact = form.cleaned_data.get('scontact')
            user.profile.is_tenant = form.cleaned_data.get('is_tenant')
            user.profile.marital_status = form.cleaned_data.get(
                'marital_status')
            user.profile.nationality = form.cleaned_data.get('nationality')
            user.profile.image = form.cleaned_data.get('image')
            user.is_active = False
            user.save()
            occupancy_type = OccupancyType.objects.get(
                occupancy_type='User Verification Pending')

            tenant = Profile.objects.get(user=user)
            if not tenant.is_tenant:
                messages.error(
                    request, 'User is not a tenant please make sure the user is a tenant')
                return redirect(add_tenant_to_unit, unit_id)
            tenant_contract = TenantContract(tenant=tenant, unit=unit)
            property_ = Property.objects.get(unit=unit)
            tenant_contract.property_id = property_
            unit.occupancy_type = occupancy_type
            unit.save()
            tenant_contract.save()

            current_site = get_current_site(request)

            email_body = {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            }
            link = reverse('activate', kwargs={
                'uidb64': email_body['uid'], 'token': email_body['token']})

            email_subject = 'Activate your account'

            activate_url = 'http://'+current_site.domain+link

            html_content_template = render_to_string(
                'auth/email_verification_msg.html', {"link": activate_url, "username": user.username.upper()})
            email = EmailMultiAlternatives(
                email_subject,
                html_content_template,
                'noreply@newdoor.com',
                [email],
            )
            email.attach_alternative(html_content_template, "text/html")
            email.send(fail_silently=False)

            messages.success(request, 'Account created successfully')
            return redirect('login')

    else:
        form = ProfileRegistrationForm()

    context = {
        "form": form
    }

    return render(request, 'new_door/add_user_unit.html', context)


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

    return render(request, 'new_door/add_occupancy_type.html', context)


@login_required
def add_tetant_contract(request, user):
    # Todo: Make sure template has valid fields
    tenant_contract = TenantContract.objects.get(tenant__user__username=user)

    tenant = Profile.objects.get(user__username=user)
    property_ = Property.objects.get(pk=tenant_contract.property_id.pk)
    unit = Unit.objects.get(pk=tenant_contract.unit.pk)
    unit_occupancy = OccupancyType.objects.get(
        occupancy_type__iexact='Payment Pending')
    unit.occupancy_type = unit_occupancy
    unit.save()

    occupancy_types = OccupancyType.objects.all()

    if request.method == 'POST':
        form = TenantContractModelForm(request.POST, instance=tenant_contract)
        if form.is_valid():
            if not tenant.is_tenant:
                messages.error(
                    request, 'User is not a tenant please make sure the user is a tenant')
                return redirect('add_tetant_contract', user)

            form.save()
            messages.success(
                request, 'Congratulations...! Contract successfully added.')

            msg = f"Hi {user}\n Your contract has been generated"
            tenant.user.email
            send_mail(
                'New Door Contract',
                msg,
                'noreply@newdoor.com',
                [tenant.user.email],
                fail_silently=False,
            )
            return redirect('review_documents', user)
    else:
        form = TenantContractModelForm(instance=tenant_contract)

    context = {
        'form': form,
        'occupancy_types': occupancy_types,
        "tenant": tenant,
        "property": property_,
        "unit": unit,
    }

    return render(request, 'tenant/tenant_contract.html', context)


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


def upload_doc_delete(request, doc_id):
    uploaded_document = UploadDocument.objects.filter(pk=doc_id)
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
