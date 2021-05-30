from accounts.views import email_verification, login_view, logout_view
from django.urls import path


urlpatterns = [
    # path('auth/signup/', auth_signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('activate/<uidb64>/<token>', email_verification, name='activate')
]
