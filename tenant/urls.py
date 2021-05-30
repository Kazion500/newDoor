from tenant.views import add_tenant_to_unit, add_tetant_contract, tenant_dashboard
from django.urls import path


urlpatterns = [
    path('dashboard/', tenant_dashboard, name='tenant_dashboard'),
    path('contract/<str:user>',
         add_tetant_contract, name='add_tetant_contract'),
    path('add-user/<unit_id>', add_tenant_to_unit, name='add_tenant_to_unit'),
]
