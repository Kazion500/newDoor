from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.shortcuts import redirect
from six import text_type
from django.contrib.auth.models import User
from django.contrib import messages
class AppTokenGenerator(PasswordResetTokenGenerator):

    def _make_hash_value(self, user, timestamp):
        return (text_type(user.is_active) + text_type(user.pk) + text_type(timestamp))


account_activation_token = AppTokenGenerator()


def check_activate_status(request):
    request.user.is_active = False
    messages.error(request,'Your account is not activated please check your email and activate your account')
    return redirect('login')