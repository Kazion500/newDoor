from django.urls import path

from app_config.views import (add_category_type, add_contract_request, add_doc_type, add_occupancy_type,
                              add_ownership_type, add_payment_mode, add_property_type, add_status_request, add_tenant_request,
                              delete_payment_mode, delete_ownership_type, delete_occupancy_type,
                              delete_category_type, delete_contract_request, delete_doc_type, delete_property_type,
                              delete_status_request, delete_tenant_request, update_category_type, update_contract_request,
                              update_doc_type, update_occupancy_type, update_ownership_type, update_payment_mode,
                              update_property_type, update_status_request,  update_tenant_request, view_category_type,
                              view_contract_request, view_doc_type, view_occupancy_type, view_ownership_type, view_payment_mode,
                              view_property_type, view_status_request, view_tenant_request)

urlpatterns = [

    path('add-category-type/', add_category_type,
         name='add_category_type'),
    path('update-category-type/<id>', update_category_type,
         name='update_category_type'),
    path('view-category-type/<id>', view_category_type,
         name='view_category_type'),
    path('delete-category-type/<id>', delete_category_type,
         name='delete_category_type'),

    # """ Master Routes Property Type """

    path('add-property-type/', add_property_type, name='add_property_type'),
    path('update-property-type/<id>', update_property_type,
         name='update_property_type'),
    path('view-property-type/<id>', view_property_type,
         name='view_property_type'),
    path('delete-property-type/<id>', delete_property_type,
         name='delete_property_type'),


    # """ Master Routes Ownership Type """

    path('add-ownership-type/', add_ownership_type,
         name='add_ownership_type'),
    path('update-ownership-type/<id>', update_ownership_type,
         name='update_ownership_type'),
    path('view-ownership-type/<id>', view_ownership_type,
         name='view_ownership_type'),
    path('delete-ownership-type/<id>', delete_ownership_type,
         name='delete_ownership_type'),


    # """ Master Routes Ownership Type """

    path('add-occupancy-type/', add_occupancy_type,
         name='add_occupancy_type'),
    path('update-occupancy-type/<id>', update_occupancy_type,
         name='update_occupancy_type'),
    path('view-occupancy-type/<id>', view_occupancy_type,
         name='view_occupancy_type'),
    path('delete-occupancy-type/<id>', delete_occupancy_type,
         name='delete_occupancy_type'),



    # """ Master Routes Contract Request Type """
    path('add-contract-request/', add_contract_request,
         name='add_contract_request'),
    path('update-contract-request/<id>', update_contract_request,
         name='update_contract_request'),
    path('delete-contract-request/<id>', delete_contract_request,
         name='delete_contract_request'),
    path('view-contract-request/<id>', view_contract_request,
         name='view_contract_request'),


    # """ Master Routes Tenant Request """
    path('add-tenant-request/', add_tenant_request,
         name='add_tenant_request'),
    path('update-tenant-request/<id>', update_tenant_request,
         name='update_tenant_request'),
    path('delete-tenant-request/<id>', delete_tenant_request,
         name='delete_tenant_request'),
    path('view-tenant-request/<id>', view_tenant_request,
         name='view_tenant_request'),


    # """ Master Routes Status Request """
    path('add-status-request/', add_status_request,
         name='add_status_request'),
    path('update-status-request/<id>', update_status_request,
         name='update_status_request'),
    path('delete-status-request/<id>', delete_status_request,
         name='delete_status_request'),
    path('view-status-request/<id>', view_status_request,
         name='view_status_request'),


    # """ Master Routes Document Type """
    path('add-doc-type/', add_doc_type,
         name='add_doc_type'),
    path('update-doc-type/<id>', update_doc_type,
         name='update_doc_type'),
    path('delete-doc-type/<id>', delete_doc_type,
         name='delete_doc_type'),
    path('view-doc-type/<id>', view_doc_type,
         name='view_doc_type'),


    # """ Master Routes Payment Mode """
    path('add-payment-mode/', add_payment_mode,
         name='add_payment_mode'),
    path('update-payment-mode/<id>', update_payment_mode,
         name='update_payment_mode'),
    path('delete-payment-mode/<id>', delete_payment_mode,
         name='delete_payment_mode'),
    path('view-payment-mode/<id>', view_payment_mode,
         name='view_payment_mode')
]
