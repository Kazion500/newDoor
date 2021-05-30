from django.db.models.aggregates import Min, Sum
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMultiAlternatives, send_mail
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from django.urls import reverse

from profiles.utils import account_activation_token
from tenant.models import TenantContract
from profiles.forms import ProfileRegistrationForm
from app_config.models import OccupancyType
from new_door.models import Property, TenantDocument, Unit
from profiles.models import Profile
from payment.models import Payment

import random

# Create your views here.


@login_required
def tenant_dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if not request.user.profile.is_tenant:
        return redirect('dashboard')

    logged_user = request.user.username
    payments = 0
    amount = 0
    due_amount = 0
    unit_rental = 0
    units = []
    uploaded_documents = []

    try:
        payments = Payment.objects.filter(
            contract__tenant__user__username=logged_user).order_by('paid_date')[:5]
        amount = Payment.objects.filter(
            contract__tenant__user__username=logged_user).aggregate(paid=Sum('amount'))
        due_amount = Payment.objects.filter(
            contract__tenant__user__username=logged_user).aggregate(remain=Min('remain_amount'))
        units = Unit.objects.filter(
            tenantcontract__tenant__user__username=logged_user)
        uploaded_documents = TenantDocument.objects.filter(
            tenant__user__username=logged_user)

        for unit in units:
            unit_rental += unit.tenantcontract.annual_rent
    except:
        pass

    context = {
        "payments": payments,
        "unit_rental": unit_rental,
        'amount': amount,
        'due_amount': due_amount,
        "units": units,
        "uploaded_documents": uploaded_documents,
    }

    return render(request, 'tenant/tenant_dashboard.html', context)


@login_required
def add_tetant_contract(request, user):
    # Todo: Make sure template has valid fields
    tenant_contract = TenantContract.objects.get(tenant__user__username=user)

    tenant = Profile.objects.get(user__username=user)
    property_ = Property.objects.get(pk=tenant_contract.property_id.pk)
    unit = Unit.objects.get(pk=tenant_contract.unit.pk)

    occupancy_types = OccupancyType.objects.all()

    if request.method == 'POST':
        form = TenantContractModelForm(request.POST, instance=tenant_contract)
        if form.is_valid():
            discount = form.cleaned_data.get('discount')
            security_dep = form.cleaned_data.get('security_dep')
            commission = form.cleaned_data.get('commission')

            if discount == None and security_dep == None and commission == None:
                messages.error(
                    request, 'All fields must be filled')
                return redirect('add_tetant_contract', user)

            if not tenant.is_tenant:
                messages.error(
                    request, 'User is not a tenant please make sure the user is a tenant')
                return redirect('add_tetant_contract', user)

            # calculate total unit amount
            total_unit_amount = unit.rent_amount + \
                int(security_dep) + int(commission) - int(discount)
            tenant_contract.annual_rent = total_unit_amount
            unit_occupancy = OccupancyType.objects.get(
                occupancy_type__iexact='Payment Pending')
            unit.occupancy_type = unit_occupancy
            tenant_contract.save()
            unit.save()
            form.save()

            messages.success(
                request, 'Congratulations...! Contract successfully added.')

            msg_to_tenant = f"Hi {user},\n Your contract has been generated. Kindly proceed with making your first payment.\n NOTE: Your First Payment should be done within the first 5 days following contract generation \n\n Best Regard\n Faraz\n New Door Manager."

            send_mail(
                'New Door Contract',
                msg_to_tenant,
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

            user = Profile.objects.create_user(
                username=username,
                email=email,
                first_name=firstname,
                last_name=lastname
            )
            user.set_password(password)
            user.profile.mid_name = form.cleaned_data.get('mid_name')
            user.profile.pcontact = form.cleaned_data.get('pcontact')
            user.profile.scontact = form.cleaned_data.get('scontact')
            user.profile.is_tenant = True
            user.profile.marital_status = form.cleaned_data.get(
                'marital_status')
            user.profile.nationality = form.cleaned_data.get('nationality')
            user.profile.image = form.cleaned_data.get('image')
            # Change to False in production
            # user.is_active = False
            user.save()
            occupancy_type = OccupancyType.objects.get(
                occupancy_type='Email Verification')

            tenant = Profile.objects.get(user=user)
            if not tenant.is_tenant:
                messages.error(
                    request, 'User is not a tenant please make sure the user is a tenant')
                return redirect(add_tenant_to_unit, unit_id)
            tenant_contract = TenantContract(tenant=tenant, unit=unit)
            property_ = Property.objects.get(unit=unit)
            tenant_contract.property_id = property_
            ran_num = random.randint(1, 900000)

            tenant_contract.contract_no = ran_num
            tenant_contract.annual_rent = unit.rent_amount
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
