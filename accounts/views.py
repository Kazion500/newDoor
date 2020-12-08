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
            user.profile.first_name = form.cleaned_data.get('first_name')
            user.profile.mid_name = form.cleaned_data.get('mid_name')
            user.profile.last_name = form.cleaned_data.get('last_name')
            user.profile.pcontact = form.cleaned_data.get('pcontact')
            user.profile.scontact = form.cleaned_data.get('scontact')
            user.profile.marital_status = form.cleaned_data.get(
                'marital_status')
            user.profile.nationality = form.cleaned_data.get(
                'nationality')
            user.profile.roll_id = form.cleaned_data.get(
                'roll_id')
            user.save()
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
