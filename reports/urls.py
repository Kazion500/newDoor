from reports.views import entity_report, property_unit_report, report, tenant_detail_report, tenant_payment_report, unpaid_tenant_report
from django.urls import path
from reports.views import (EntityCSVView, EntityPDFView,
                            PropertyCSVView, PropertyPDFView, PropertyUnitPDFView)


urlpatterns = [
    path('export/<str:user_id>', EntityPDFView.as_view(), name='export'),
    path('export-csv/<str:user_id>',
         EntityCSVView.as_view(), name='export_csv'),
    path('export-property/<str:pk>', PropertyPDFView.as_view(),
         name='export_property'),
    path('export-csv-property/<str:pk>', PropertyCSVView.as_view(),
         name='export_property_csv'),
    path('property-unit-report/<str:property_id>', PropertyUnitPDFView.as_view(),
         name='property_unit_report'),

    path('report/', report, name='report'),
    path('oveview-report/', entity_report, name='oveview_report'),
    path('property-unit-report/', property_unit_report,
         name='property_unit_report'),
    path('tenant-detail-report/', tenant_detail_report,
         name='tenant_detail_report'),
    path('tenant-payment-report/', tenant_payment_report,
         name='tenant_payment_report'),
    path('unpaid-tenant-report/', unpaid_tenant_report,
         name='unpaid_tenant_report'),
]
