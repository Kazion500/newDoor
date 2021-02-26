from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import SiginInUserForm, ProfileRegistrationForm
from django.contrib import messages
from new_door.models import Profile
from new_door.utils import check_activate_status


def login_view(request):

    if request.user.is_authenticated:
        return redirect('/')

    if request.method == "POST":
        form = SiginInUserForm(request.POST)

        if form.is_valid():
            user_name = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=user_name, password=password)

            if user != None:
                login(request, user)
                messages.success(request, 'Logged in successfully')
                return redirect('/')
            else:
                messages.success(request, 'Your password or email is invalid')
                return redirect('/')

            # try:
            #     auth_user = User.objects.get(username=user_name)
            #     if not auth_user.is_active:
            #         messages.error(
            #             request, "Please make sure you activate your account before loggin in")
            #         return redirect('login')
            #     elif not auth_user.check_password(password):
            #         messages.error(
            #             request, "Make sure your password and username are correct")
            #         return redirect('login')

            #     user = authenticate(request, username=user_name, password=password)

            #     if user is not None:
            #         login(request, user)
            #         messages.success(request, 'Logged in successfully')
            #         return redirect('/')

            # except User.DoesNotExist:
            # messages.error(
            #     request, "Make sure your password and username are correct")
            # return redirect('login')

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
