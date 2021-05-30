from payment.views import payment, checklist
from django.urls import path


urlpatterns = [
    path('<str:user>/', payment, name='payment'),
    path('checkout/', checklist, name='payment'),
]
