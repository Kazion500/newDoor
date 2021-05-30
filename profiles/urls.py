
from profiles.views import add_user, edit_profile, profile_view
from django.urls import path


urlpatterns = [
    path('add-user/', add_user, name='add_user'),
    path('edit-profile/<str:username>', edit_profile, name='edit_profile'),
    path('profile/<str:username>', profile_view, name='my_profile'),
]
