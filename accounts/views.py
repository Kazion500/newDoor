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
            user = form.save()
            print(user.profile)
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
