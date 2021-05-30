from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from new_door.models import Profile
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode

from tenant.models import TenantContract
from profiles.utils import account_activation_token
from accounts.forms import SiginInUserForm
from new_door.models import Unit
from app_config.models import OccupancyType


def login_view(request):

    if request.user.is_authenticated:
        return redirect('/')

    if request.method == "POST":
        form = SiginInUserForm(request.POST)

        if form.is_valid():
            user_name = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=user_name, password=password)

            if user != None and not user.is_active:
                messages.error(request, 'Your account is not activated')
                return redirect('login')

            if user != None:
                login(request, user)
                messages.success(request, 'Logged in successfully')
                return redirect('/')
            else:
                messages.error(request, 'Your password or email is invalid')
                return redirect('login')

        else:
            messages.error(
                request, 'Check your inputs i.e username and password')
            return redirect('login')
    else:
        form = SiginInUserForm()

    context = {
        "form": form,
    }

    return render(request, 'auth/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('login')


def email_verification(request, uidb64, token):
    try:
        id = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=id)

        if not account_activation_token.check_token(user, token):
            return redirect(f'login?message=User already activated')

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

        # Send Email

        messages.success(request, 'Account activated successfully')
        return redirect('login')

    except Exception as ex:
        pass

    return redirect('login')
