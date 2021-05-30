from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from new_door.views import (add_entity, add_property, add_property_all, add_unit, dashboard_view,
                            delete_entity, delete_property, delete_unit, entity_overview,
                            prepopulated_field_unit, property_all_overview, property_overview, property_unit_overview, review_documents,
                            unit_overview, update_entity, update_property, update_unit, upload_doc_delete, upload_documents, verify_documents, view_entity, view_property,
                            view_unit
                            )


urlpatterns = [

    path('', dashboard_view, name='dashboard'),


    # """ Entity Routes """

    path('entity-overview/', entity_overview, name='entity_overview'),
    path('add-entity/', add_entity, name='add_entity'),
    path('update-entity/<id>', update_entity, name='update_entity'),
    path('view-entity/<id>', view_entity, name='view_entity'),
    path('delete-entity/<id>', delete_entity, name='delete_entity'),

    # """ Propery Routes """

    path('property-overview/',
         property_all_overview, name='property_all_overview'),
    path('property-overview/<str:entity>',
         property_overview, name='property_overview'),
    path('property-unit-overview/<id>', property_unit_overview,
         name='property_unit_overview'),
    path('add-property/<str:entity>', add_property, name='add_property'),
    path('add-property-all/', add_property_all, name='add_property_all'),
    path('update-property/<id>', update_property, name='update_property'),
    path('view-property/<id>', view_property, name='view_property'),
    path('delete-property/<id>', delete_property, name='delete_property'),


    # """ Unit Routes """

    path('unit-overview/', unit_overview, name='unit_overview'),
    path('add-unit/', add_unit, name='add_unit'),
    path('add-unit/<id>', prepopulated_field_unit,
         name='prepopulated_field_unit'),
    path('update-unit/<id>', update_unit, name='update_unit'),
    path('view-unit/<id>', view_unit, name='view_unit'),
    path('delete-unit/<id>', delete_unit, name='delete_unit'),


    # """ Master Routes Document upload """
    path('upload-documents/<str:user>',
         upload_documents, name='upload_documents'),
    path('review-documents/<str:user>',
         review_documents, name='review_documents'),
    path('verify-documents/<str:user>',
         verify_documents, name='verify_documents'),
    path('delete-documents/<str:doc_id>',
         upload_doc_delete, name='upload_doc_delete'),

    # include Tentant routes
    path('tenant/', include('tenant.urls')),

    # include Tentant routes
    path('profile/', include('profiles.urls')),

    # include Payment routes
    path('payment/', include('payment.urls')),

    # include App Config routes
    path('config/', include('app_config.urls')),

    # include Authentication routes
    path('account/', include('accounts.urls')),

    # include Report routes
    path('reports/', include('reports.urls'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
