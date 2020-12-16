from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import SiginInUserForm, ProfileRegistrationForm
from django.contrib import messages
from new_door.models import Profile


def signup_view(request):
    if request.method == "POST":
        form = ProfileRegistrationForm(request.POST)
        print(form.errors)
        if form.is_valid():
            invalid_user=send_verification_email(request,form)
            # user = form.save()
            print(invalid_user.profile)
            invalid_user.refresh_from_db()
            invalid_user.profile.email = form.cleaned_data.get('email')
            invalid_user.profile.mid_name = form.cleaned_data.get('mid_name')
            invalid_user.profile.pcontact = form.cleaned_data.get('pcontact')
            invalid_user.profile.scontact = form.cleaned_data.get('scontact')
            invalid_user.profile.scontact = form.cleaned_data.get('scontact')
            invalid_user.profile.is_tenant = form.cleaned_data.get('is_tenant')
            invalid_user.profile.is_owner = form.cleaned_data.get('is_owner')
            invalid_user.profile.marital_status = form.cleaned_data.get(
                'marital_status')
            invalid_user.profile.nationality = form.cleaned_data.get(
                'nationality')
            invalid_user.save()
            messages.success(request, 'Account successfully added')
            return redirect('login')
        else:
            messages.error(
                request, 'There was a problem creating the account please check your inputs')
            return redirect('signup')
    else:
        form = ProfileRegistrationForm()
    context = {
        "form": form,
    }

    return render(request, 'auth/signup.html', context)


def login_view(request):

    if request.user.is_authenticated:
        return redirect('/')

    if request.method == "POST":
        form = SiginInUserForm(request.POST)

        if form.is_valid():
            user_name = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(
                request, username=user_name, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in successfully')
                return redirect('/')
            else:
                messages.error(
                    request, "User doesn't exist: Make sure your password and username are correct")
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
