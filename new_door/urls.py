from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from accounts import views as auth_views


urlpatterns = [

    path('', views.dashboard_view, name='dashboard'),
    path('tenant-dashboard/', views.tenant_dashboard, name='tenant_dashboard'),

    # """ Entity Routes """

    path('entity-overview/', views.entity_overview, name='entity_overview'),
    path('add-entity/', views.add_entity, name='add_entity'),
    path('update-entity/<id>', views.update_entity, name='update_entity'),
    path('view-entity/<id>', views.view_entity, name='view_entity'),
    path('delete-entity/<id>', views.delete_entity, name='delete_entity'),

    #  Edit Profile
     path('edit-profile/<str:username>', views.edit_profile, name='edit_profile'),

    # """ Propery Routes """

    path('property-overview/',
         views.property_all_overview, name='property_all_overview'),
    path('property-overview/<str:entity>',
         views.property_overview, name='property_overview'),
    path('property-unit-overview/<id>', views.property_unit_overview,
         name='property_unit_overview'),
    path('add-property/<str:entity>', views.add_property, name='add_property'),
    path('add-property-all/', views.add_property_all, name='add_property_all'),
    path('update-property/<id>', views.update_property, name='update_property'),
    path('view-property/<id>', views.view_property, name='view_property'),
    path('delete-property/<id>', views.delete_property, name='delete_property'),


    # """ Unit Routes """

    path('unit-overview/', views.unit_overview, name='unit_overview'),
    path('add-unit/', views.add_unit, name='add_unit'),
    path('add-unit/<id>', views.prepopulated_field_unit,
         name='prepopulated_field_unit'),
    path('update-unit/<id>', views.update_unit, name='update_unit'),
    path('view-unit/<id>', views.view_unit, name='view_unit'),
    path('delete-unit/<id>', views.delete_unit, name='delete_unit'),

    # """ Add User """
    path('add-user/', views.add_user, name='add_user'),
    path('add-user/<unit_id>', views.add_tenant_to_unit, name='add_tenant_to_unit'),


    # """ Master Routes Catergory Type"""

    path('add-category-type/', views.add_category_type,
         name='add_category_type'),
    path('update-category-type/<id>', views.update_category_type,
         name='update_category_type'),
    path('view-category-type/<id>', views.view_category_type,
         name='view_category_type'),
    path('delete-category-type/<id>', views.delete_category_type,
         name='delete_category_type'),

    # """ Master Routes Property Type """

    path('add-property-type/', views.add_property_type, name='add_property_type'),
    path('update-property-type/<id>', views.update_property_type,
         name='update_property_type'),
    path('view-property-type/<id>', views.view_property_type,
         name='view_property_type'),
    path('delete-property-type/<id>', views.delete_property_type,
         name='delete_property_type'),


    # """ Master Routes Ownership Type """

    path('add-ownership-type/', views.add_ownership_type,
         name='add_ownership_type'),
    path('update-ownership-type/<id>', views.update_ownership_type,
         name='update_ownership_type'),
    path('view-ownership-type/<id>', views.view_ownership_type,
         name='view_ownership_type'),
    path('delete-ownership-type/<id>', views.delete_ownership_type,
         name='delete_ownership_type'),


    # """ Master Routes Ownership Type """

    path('add-occupancy-type/', views.add_occupancy_type,
         name='add_occupancy_type'),
    path('update-occupancy-type/<id>', views.update_occupancy_type,
         name='update_occupancy_type'),
    path('view-occupancy-type/<id>', views.view_occupancy_type,
         name='view_occupancy_type'),
    path('delete-occupancy-type/<id>', views.delete_occupancy_type,
         name='delete_occupancy_type'),

    # """ Master Routes Document upload """
    path('upload-documents/<str:user>',
         views.upload_documents, name='upload_documents'),
    path('review-documents/<str:user>',
         views.review_documents, name='review_documents'),
    path('verify-documents/<str:user>',
         views.verify_documents, name='verify_documents'),
    path('delete-documents/<str:doc_id>',
         views.upload_doc_delete, name='upload_doc_delete'),



    # """ Master Routes Contract Request Type """
    path('add-contract-request/', views.add_contract_request,
         name='add_contract_request'),
    path('update-contract-request/<id>', views.update_contract_request,
         name='update_contract_request'),
    path('delete-contract-request/<id>', views.delete_contract_request,
         name='delete_contract_request'),
    path('view-contract-request/<id>', views.view_contract_request,
         name='view_contract_request'),


    # """ Master Routes Tenant Request """
    path('add-tenant-request/', views.add_tenant_request,
         name='add_tenant_request'),
    path('update-tenant-request/<id>', views.update_tenant_request,
         name='update_tenant_request'),
    path('delete-tenant-request/<id>', views.delete_tenant_request,
         name='delete_tenant_request'),
    path('view-tenant-request/<id>', views.view_tenant_request,
         name='view_tenant_request'),


    # """ Master Routes Status Request """
    path('add-status-request/', views.add_status_request,
         name='add_status_request'),
    path('update-status-request/<id>', views.update_status_request,
         name='update_status_request'),
    path('delete-status-request/<id>', views.delete_status_request,
         name='delete_status_request'),
    path('view-status-request/<id>', views.view_status_request,
         name='view_status_request'),


    # """ Master Routes Document Type """
    path('add-doc-type/', views.add_doc_type,
         name='add_doc_type'),
    path('update-doc-type/<id>', views.update_doc_type,
         name='update_doc_type'),
    path('delete-doc-type/<id>', views.delete_doc_type,
         name='delete_doc_type'),
    path('view-doc-type/<id>', views.view_doc_type,
         name='view_doc_type'),


    # """ Master Routes Payment Mode """
    path('add-payment-mode/', views.add_payment_mode,
         name='add_payment_mode'),
    path('update-payment-mode/<id>', views.update_payment_mode,
         name='update_payment_mode'),
    path('delete-payment-mode/<id>', views.delete_payment_mode,
         name='delete_payment_mode'),
    path('view-payment-mode/<id>', views.view_payment_mode,
         name='view_payment_mode'),


    # """ TENANT SECTION """
    path('tetant-contract/<str:user>',
         views.add_tetant_contract, name='add_tetant_contract'),

    # path('checklist/', views.checklist, name='checklist'),

    path('payment/<str:user>', views.payment, name='payment'),

    # Authentication routes
    #     path('auth/signup/', auth_views.signup_view, name='signup'),
    path('auth/login/', auth_views.login_view, name='login'),
    path('auth/logout/', auth_views.logout_view, name='logout'),
    path('activate/<uidb64>/<token>', views.email_verification, name='activate'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
