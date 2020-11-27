from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path('tenant-dashboard/', views.tenant_dashboard, name='tenant_dashboard'),

    # """ Entity Routes """
    path('entity-overview/', views.entity_overview, name='entity_overview'),
    path('add-entity/', views.add_entity, name='add_entity'),
    path('update-entity/<id>', views.update_entity, name='update_entity'),
    path('delete-entity/<id>', views.delete_entity, name='delete_entity'),



    # """ Propery Routes """
    path('property-overview/', views.property_overview, name='property_overview'),
    path('add-property/', views.add_property, name='add_property'),
    path('update-property/<id>', views.update_property, name='update_property'),
    path('delete-property/<id>', views.delete_property, name='delete_property'),


    # """ Unit Routes """
    path('unit-overview/', views.unit_overview, name='unit_overview'),
    path('add-unit/', views.add_unit, name='add_unit'),
    path('update-unit/<id>', views.update_unit, name='update_unit'),
    path('delete-unit/<id>', views.delete_unit, name='delete_unit'),

    # """ Master Routes Catergory Type"""
    path('add-category-type/', views.add_category_type,
         name='add_category_type'),
    path('delete-category-type/<id>', views.delete_category_type,
         name='delete_category_type'),

    # """ Master Routes Property Type """
    path('add-property-type/', views.add_property_type, name='add_property_type'),
    path('update-property-type/<id>', views.update_property_type,
         name='update_property_type'),
    path('delete-property-type/<id>', views.delete_property_type,
         name='delete_property_type'),
    # path('Update_Property_Type-<id>/',
    #      views.Update_Property_Type, name='UpdatePropertyType'),
    # path('Delete_Property_Type/<int:id>/',
    #      views.Delete_Property_Type, name="DeletePropertyType"),


    # # *************Master Table Ownership_Type*************
    path('add-ownership-type', views.add_ownership_type, name='add_ownership_type'),
    path('update-ownership-type/<id>', views.update_ownership_type,
         name='update_ownership_type'),
    path('delete-ownership-type/<id>', views.delete_ownership_type,
         name='delete_ownership_type'),
    # path('View_Ownership_Type-<id>/',
    #      views.View_Ownership, name='ViewOwnershipType'),
    # path('Update_Ownership_Type-<id>/',
    #      views.update_Ownership, name='UpdateOwnershipType'),
    # path('Delete_Ownership_Type/<int:id>/',
    #      views.delete_Ownership, name="DeleteOwnershipType"),

    # path('upload-documents/', views.upload_documents, name='upload_documents'),
    # path('payment/', views.payment, name='payment'),




    # path('checklist/', views.checklist, name='checklist'),
    # path('login', views.login_User, name='login'),
    # path('logout', views.logout_User, name='logout'),
    # path('Main_NewDoor', views.Main_NewDoor, name='Main_NewDoor'),
    # path('Dashboard', views.Dashboard, name='Dashboard'),
    # path('Tenant_Dashboard', views.Tenant_Dashboard, name='Tenant_Dashboard'),

    # # ************* Table Entity*************
    # path('Add_Entity', views.Add_Entity, name='Add_Entity'),
    # path('Entity_Overview', views.Entity_Overview, name='Entity_Overview'),
    # path('View_Entity-<id>/', views.View_Entity, name='ViewEntity'),
    # path('Update_Entity-<id>/', views.Update_Entity, name='UpdateEntity'),
    # path('Delete_Entity/<int:id>/', views.Delete_Entity, name='DeleteEntity'),

    # # ************* Table Property*************
    # path('Add_Property', views.Add_Property, name='Add_Property'),
    # path('Property_Overview', views.Property_Overview, name='Property_Overview'),
    # path('View_Property-<id>/', views.View_Property, name='ViewProperty'),
    # path('Update_Property-<id>/', views.Update_Property, name='UpdateProperty'),
    # path('Delete_Property/<int:id>/',
    #      views.Delete_Property, name="DeleteProperty"),

    # # *************Table Unit*************
    # path('Add_Unit', views.Add_Unit, name='Add_Unit'),
    # path('Unit_Overview', views.Unit_Overview, name='Unit_Overview'),
    # path('View_Unit-<id>/', views.View_Unit, name='ViewUnit'),
    # path('Renewal_Request', views.Renewal_Request, name='RenewalRequest'),
    # path('Maintenance_Request', views.Maintenance_Request,
    #      name='Maintenance_Request'),
    # path('Update_Unit-<id>/', views.Update_Unit, name='UpdateUnit'),
    # path('Delete_Unit/<int:id>/', views.Delete_Unit, name="DeleteUnit"),

    # # *************Table User*************
    # path('Add_User', views.Add_User, name='Add_User'),
    # # path('Property_Overview', views.Property_Overview, name='Property_Overview'),

    # # *************Master Table Category_Type*************
    # path('Category_Type', views.Category_Type, name='Category_Type'),
    # path('View_Category_Type-<id>/', views.View_Cattyp, name='Viewcategory'),
    # path('Update_Category_Type-<id>/',
    #      views.update_Cattyp, name='updatecategory'),
    # path('Delete_Category_Type/<int:id>/',
    #      views.delete_category, name="deletecategory"),





    # # *************Master Table PayMode_Type*************
    # path('PayMode_Type', views.PayMode_Type, name='PayMode_Type'),
    # path('View_PayMode_Type-<id>/', views.View_PayModeType, name='ViewPayModeType'),
    # path('Update_PayMode_Type-<id>/',
    #      views.Update_PayModeType, name='UpdatePayModeType'),
    # path('Delete_PayMode_Type/<int:id>/',
    #      views.Delete_PayModeType, name="DeletePayModeType"),

    # # *************Master Table StatusReq_Type*************
    # path('StatusReq_Type', views.StatusReq_Type, name='StatusReq_Type'),
    # path('View_StatusReqType-<id>/',
    #      views.View_StatusReqType, name='ViewStatusReqType'),
    # path('Update_StatusReqType-<id>/',
    #      views.Update_StatusReqType, name='UpdateStatusReqType'),
    # path('Delete_StatusReq_Type/<int:id>/',
    #      views.Delete_StatusReqType, name="DeleteStatusReqType"),

    # # *************Master Table Tenant_Request_Type*************
    # path('TenantReq_Type', views.TenantReq_Type, name='TenantReq_Type'),
    # path('View_TenantReq_Type-<id>/',
    #      views.View_TenantReqType, name='ViewTenantReqType'),
    # path('Update_TenantReq_Type-<id>/',
    #      views.Update_TenantReqType, name='UpdateTenantReqType'),
    # path('Delete_TenantReq_Type/<int:id>/',
    #      views.Delete_TenantReqType, name="DeleteTenantReqType"),

    # # *************Master Table Contract_Request_Type*************
    # path('ContractReq_Type', views.ContractReq_Type, name='ContractReq_Type'),
    # path('View_ContractReq_Type-<id>/',
    #      views.View_ContractReqType, name='ViewContractReqType'),
    # path('Update_ContractReq_Type-<id>/',
    #      views.Update_ContractReqType, name='UpdateContractReqType'),
    # path('Delete_ContractReq_Type/<int:id>/',
    #      views.Delete_ContractReqType, name="DeleteContractReqType"),

    # # *************Master Table Documents_Type*************
    # path('Documents_Type', views.Documents_Type, name='Documents_Type'),
    # path('View_Documents_Type-<id>/',
    #      views.View_DocumentsType, name='ViewDocumentsType'),
    # path('Update_Documents_Type-<id>/',
    #      views.Update_DocumentsType, name='UpdateDocumentsType'),
    # path('Delete_Documents_Type/<int:id>/',
    #      views.Delete_DocumentsType, name="DeleteDocumentsType"),

    # # *************Master Table Occupancy_Type*************
    # path('Occupancy_Type', views.Occupancy_Type, name='Occupancy_Type'),
    # path('View_Occupancy_Type-<id>/',
    #      views.View_OccupancyType, name='ViewOccupancyType'),
    # path('Update_Occupancy_Type-<id>/',
    #      views.Update_OccupancyType, name='UpdateOccupancyType'),
    # path('Delete_Occupancy_Type/<int:id>/',
    #      views.Delete_OccupancyType, name="DeleteOccupancyType"),

    # # *************Master Table Tenant*************
    # path('Add_Tenant', views.Add_Tenant, name='Add_Tenant'),
    # path('Tenant_Contract', views.Tenant_Contract, name='Tenant_Contract'),
    # path('Review_Documents', views.Review_Documents, name='Review_Documents'),

    # # *************Table Upload Documents*************
    # path('Upload_Documents', views.Upload_Documents, name='UploadDocuments'),

    # # *************Table Payment*************
    # path('Payment', views.Payment, name='Payment'),
]
