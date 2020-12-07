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
            # print(dir(user))
            # profile = Profile.objects.get(user=user)
            # profile.email = user.email
            # profile.first_name = user.first_name
            # profile.mid_name = user.mid_name
            # profile.last_name = user.last_name
            # profile.pcontact = user.pcontact
            # profile.scontact = user.scontact
            # profile.marital_status = user.marital_status
            # profile.nationality= user.nationality
            # profile.roll_id = user.nationality
            # profile.save()
    else:
        form = ProfileRegistrationForm()
    context = {
        "form": form,
    }

    return render(request, 'auth/signup.html', context)


def login_view(request):

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
