from app_config.models import CategoryType
from payment.models import Payment
from tenant.models import TenantContract
from django.db.models.query_utils import Q
from django.http.response import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum, Max, Min
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
from profiles.utils import account_activation_token
from django.urls import reverse
import stripe
from django_renderpdf.views import PDFView
from csv_export.views import CSVExportView

from new_door.models import Unit
from app_config.models import OccupancyType
from profiles.forms import ProfileRegistrationForm
from profiles.models import Profile

# Create your views here.


@login_required
def profile_view(request, username):
    user = request.user.username
    profile = get_object_or_404(Profile, user__username=username)
    context = {
        "profile": profile
    }
    return render(request, 'profile/my_profile.html', context)


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
            user.profile.is_owner = True
            user.profile.marital_status = form.cleaned_data.get(
                'marital_status')
            user.profile.nationality = form.cleaned_data.get('nationality')
            user.profile.image = form.cleaned_data.get('image')
            # Change user.is_active to False
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

            mail_context = {"link": activate_url,
                            "username": user.username.upper()}

            html_content_template = render_to_string(
                'email_temp/welcome.html', mail_context)

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


@login_required
def edit_profile(request, username):
    profile = Profile.objects.get(user__username=username)
    profile_ = User.objects.get(username=username)
    if request.method == "POST":
        form = ProfileRegistrationForm(request.POST, instance=profile_)

    else:
        form = ProfileRegistrationForm(instance=profile_)

    return render(request, 'profile/edit_profile.html', {"form": form})


# @login_required
