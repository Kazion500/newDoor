from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages

from .forms import (
    EntityModelForm,
    PropertyModelForm,
    #     F_CategoryType,
    #     f_OwnershipType,
    #     F_PropertyType,
    #     F_DocumentType,
    #     F_PayModeType,
    #     F_StatusReqType,
    #     F_TenantReqType,
    #     F_ContractReqType,
    #     F_DocumentsType,
    #     F_OccupancyType,
    #     F_TenantContract,
    #     F_User, F_Tenant
)

from .models import (
    Entity, Property,
    Unit, CategoryType,
    OwnershipType, PropertyType,
    DocumentType, PayModeType,
    StatusReqType, TenantReqType,
    ContractReqType, DocumentsType,
    OccupancyType, TenantContract,
    User, UnitImage
)

# Dashboard Rendering


def dashboard_view(request):
    return render(request, 'new_door/dashboard.html')


def tenant_dashboard(request):
    return render(request, 'new_door/tenant_dashboard.html')


def entity_overview(request):
    entities = Entity.objects.all()
    context = {
        'entities': entities
    }
    return render(request, 'new_door/entity_overview.html', context)


def property_overview(request):
    properties = Property.objects.all()
    context = {
        'properties': properties
    }
    return render(request, 'new_door/property_overview.html', context)


def unit_overview(request):
    units = Property.objects.all()
    context = {
        'units': units
    }
    return render(request, 'new_door/unit_overview.html', context)


def checklist(request):
    return render(request, 'new_door/checklist.html')


def upload_documents(request):
    return render(request, 'new_door/upload_documents.html')


def payment(request):
    return render(request, 'new_door/payment.html')


def add_entity(request):
    entities = Entity.objects.all()

    if request.method == 'POST':
        form = EntityModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Congratulations...! Document Type successfully added.')
            return redirect('add_entity')
    else:
        form = EntityModelForm()

    context = {
        'form': form,
        'entities': entities
    }
    return render(request, 'new_door/add_entity.html', context)


def add_property(request):
    entities = Entity.objects.all()
    if request.method == 'POST':
        form = PropertyModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Congratulations...! Property successfully added.')
            return redirect('add_property')
    else:
        form = PropertyModelForm(request.POST)

    context = {
        'form': form,
        'entities': entities
    }
    return render(request, 'new_door/add_property.html', context)

# def login_User(request):
#     if request.method == "POST":
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect("/")
#         else:
#             return render(request, 'login.html')
#     return render(request, 'login.html')

# ***************************************************************


# def logout_User(request):
#     logout(request)
#     return redirect("/login")

# # *********Class User_Login Defination Start Here---12-11-2020 12.14AM- Javed Farooqui *******

# # *****************************************************************************************************************************


# # ********************************************************************************************************************************************


# # *********Class Entity Defination Start Here---31-10-2020 12.43AM- Javed Farooqui *******

# # *********Class Entity Defination End Here---31-10-2020 01:10AM- Javed Farooqui *******

# # ********** Update_Entity Action button start here: 15.11.2020 11:55PM Javed Farooqui**********


# def Update_Entity(request, id):
#     pi = Entity.objects.get(pk=id)
#     ADENT = F_Entity(request.POST, instance=pi)
#     if ADENT.is_valid():
#         ADENT.save()
#         messages.success(
#             request, 'Congratulations...! Entity successfully Updated.')
#     else:
#         pi = Entity.objects.get(pk=id)
#         ADENT = F_Entity(instance=pi)
#     return render(request, 'Update_Entity.html', {'pi': pi})
# # ********** Update_Entity Action button end here: 16.11.2020 12:25AM Javed Farooqui**********

# # ********** View_Entity Action button start here: 16.11.2020 12:31AM Javed Farooqui**********


# def View_Entity(request, id):
#     pi = Entity.objects.get(pk=id)
#     ADENT = F_Entity(request.POST, instance=pi)
#     if ADENT.is_valid():
#         ADENT.save()
#         messages.success(
#             request, 'Congratulations...! Entity successfully Updated.')
#     else:
#         pi = Entity.objects.get(pk=id)
#         ADENT = F_Entity(instance=pi)
#     return render(request, 'View_Entity.html', {'pi': pi})
# # ********** View_Entity Action button end here: 16.11.2020 12:36AM Javed Farooqui**********

# # ********** Delete_Entity Action button start here: 16.11.2020 12:38AM Javed Farooqui**********


# def Delete_Entity(request, id):
#     TT = Entity.objects.get(pk=id)
#     TT.delete()
#     messages.success(
#         request, 'Congratulations...! Entity successfully Deleted.')
#     NTT = Entity.objects.all()
#     return render(request, 'Entity_Overview.html', {'ADANTT': NTT})
# # ********** Delete_Entity Action button end here: 16.11.2020 12:36AM Javed Farooqui**********


# # ********************************************************************************************************************************************


# # *********Class Property Defination Start Here---07-11-2020 04.43PM- Javed Farooqui *******

#     else:
#         ADPRT = F_property()
#     PRT = Property.objects.all()
#     NTT = Entity.objects.all()
#     return render(request, 'Add_Property.html', {'form': ADPRT, 'ADPRPRTY': PRT, 'ENTTY': NTT})
# # *********Class Property Defination End Here---07-11-2020 05.00PM- Javed Farooqui *******

# # *********Class Property_Overview Defination Start Here---07-11-2020 04.43PM- Javed Farooqui *******


# # *********Class Property_Overview Defination End Here---07-11-2020 05.00PM- Javed Farooqui *******

# # ********** Update_Property Action button start here: 16.11.2020 11:34PM Javed Farooqui**********


# def Update_Property(request, id):
#     pi = Property.objects.get(pk=id)
#     ADPRT = F_property(request.POST, instance=pi)
#     if ADPRT.is_valid():
#         ADPRT.save()
#         messages.success(
#             request, 'Congratulations...! Property successfully Updated.')
#     else:
#         pi = Property.objects.get(pk=id)
#         ADPRT = F_property(instance=pi)
#     ENTT = Entity.objects.all()
#     return render(request, 'Update_Property.html', {'pi': pi, 'ENTT': ENTT})
# # ********** Update_Property Action button end here: 16.11.2020 11:34PM Javed Farooqui**********

# # ********** Update_Property Action button start here: 16.11.2020 11:34PM Javed Farooqui**********


# def View_Property(request, id):
#     pi = Property.objects.get(pk=id)
#     ADPRT = F_property(request.POST, instance=pi)
#     if ADPRT.is_valid():
#         ADPRT.save()
#         messages.success(
#             request, 'Congratulations...! Property successfully Updated.')
#     else:
#         pi = Property.objects.get(pk=id)
#         ADPRT = F_property(instance=pi)
#         ENTT = Entity.objects.all()
#     return render(request, 'View_Property.html', {'pi': pi, 'ADANTT': ENTT})
# # ********** Update_Property Action button end here: 16.11.2020 11:34PM Javed Farooqui**********

# # ********** Delete_Unit Action button start here: 16.11.2020 12:38AM Javed Farooqui**********


# def Delete_Property(request, id):
#     PRT = Property.objects.get(pk=id)
#     PRT.delete()
#     messages.success(
#         request, 'Congratulations...! Property successfully Deleted.')
#     PRT = Property.objects.all()
#     return render(request, 'Property_Overview.html', {'ADPRT': PRT})
# # ********** Delete_Unit Action button end here: 16.11.2020 12:36AM Javed Farooqui**********

# # **************************************************************************************************************************


# # *********Class Add_Unit Defination Start Here---07-11-2020 06.00PM- Javed Farooqui *******
# def Add_Unit(request):
#     if request.method == 'POST':
#         ADUNT = F_Unit(request.POST)
#         files = request.FILES.getlist('unitimage')
#         if ADUNT.is_valid():
#             PRTID = ADUNT.cleaned_data['PropID']
#             PRTYPID = ADUNT.cleaned_data['PrtTypID']
#             UNTFLT = ADUNT.cleaned_data['flat']
#             OWID = ADUNT.cleaned_data['OwnerTypeID']
#             UNTRNT = ADUNT.cleaned_data['rent_amount']
#             UNTSZ = ADUNT.cleaned_data['size']
#             OCPID = ADUNT.cleaned_data['OccupancyTypeID']
#             UNTBED = ADUNT.cleaned_data['bedrooms']
#             UNTBTH = ADUNT.cleaned_data['bathrooms']
#             UNTPRK = ADUNT.cleaned_data['parking']
#             UNTDSC = ADUNT.cleaned_data['desc']
#             ADUNT = Unit(PropID=PRTID, PrtTypID=PRTYPID, flat=UNTFLT, OwnerTypeID=OWID, rent_amount=UNTRNT,
#                          size=UNTSZ, OccupancyTypeID=OCPID, bedrooms=UNTBED, bathrooms=UNTBTH, parking=UNTPRK, desc=UNTDSC)
#             ADUNT.save()
#             post = Unit.objects.latest('id')
#             for f in files:
#                 Uimg = UnitImage(UnitId=post, unitimage=f)
#                 Uimg.save()
#             messages.success(
#                 request, 'Congratulations...! Unit successfully added.')
#     else:
#         ADUNT = F_Unit()
#     UNT = Unit.objects.all()
#     PRT = Property.objects.all()
#     PT = PropertyType.objects.all()
#     OWN = OwnershipType.objects.all()
#     OPTY = OccupancyType.objects.all()
#     return render(request, 'Add_Unit.html', {'form': ADUNT, 'ADUNIT': UNT, 'ADPRPRTY': PRT, 'PT': PT, 'OWN': OWN, 'OPTY': OPTY})
# *********Class Add_Unit Defination End Here---07-11-2020 07.00PM- Javed Farooqui *******

# *********Class Unit_Overview Defination Start Here---16.11.2020 11:34PM- Javed Farooqui *******


#
# # *********Class Unit_Overview Defination End Here---16.11.2020 11:34PM- Javed Farooqui *******

# # ********** Update_Unit Action button start here: 16.11.2020 11:34PM Javed Farooqui**********


# def Update_Unit(request, id):
#     pi = Unit.objects.get(pk=id)
#     ADUNT = F_Unit(request.POST, instance=pi)
#     if ADUNT.is_valid():
#         ADUNT.save()
#         messages.success(
#             request, 'Congratulations...! Category Type successfully Updated.')
#     else:
#         pi = Unit.objects.get(pk=id)
#     ADUNT = F_Unit(instance=pi)
#     PRT = Property.objects.all()
#     PTAT = PropertyType.objects.all()
#     OPTY = OccupancyType.objects.all()
#     OWN = OwnershipType.objects.all()
#     return render(request, 'Update_Unit.html', {'pi': pi, 'ADPRPRTY': PRT, 'PTAT': PTAT, 'OPTY': OPTY, 'ADOWTP': OWN})
# # ********** Update_Unit Action button end here: 16.11.2020 11:34PM Javed Farooqui**********

# # ********** Update_Unit Action button start here: 16.11.2020 11:34PM Mohd Saad**********


# def View_Unit(request, id):
#     pi = Unit.objects.get(pk=id)
#     ADUNT = F_Unit(request.POST, instance=pi)
#     if ADUNT.is_valid():
#         ADUNT.save()
#         messages.success(
#             request, 'Congratulations...! Category Type successfully Updated.')
#     else:
#         pi = Unit.objects.get(pk=id)
#         ADUNT = F_Unit(instance=pi)
#         PRT = Property.objects.all()
#         PTAT = PropertyType.objects.all()
#         OPTY = OccupancyType.objects.all()
#         OWN = OwnershipType.objects.all()
#     return render(request, 'View_Unit.html', {'pi': pi, 'ADPRPRTY': PRT, 'PTAT': PTAT, 'OPTY': OPTY, 'ADOWTP': OWN})
# # ********** Update_Unit Action button end here: 31.10.2020 03:33PM Javed Farooqui**********

# # ********** Renewal_Unit Action button start here: 20.11.2020 10:40PM Javed & Mohd Saad**********


# def Renewal_Request(request):
#     return render(request, 'Renewal_Unit.html')
# # ********** Renewal_Unit Action button end here: 20.11.2020 10:40PM Javed & Mohd Saad**********

# # ********** Renewal_Unit Action button start here: 20.11.2020 10:40PM Javed & Mohd Saad**********


# def Maintenance_Request(request):
#     return render(request, 'Renewal_Unit.html')
# # ********** Renewal_Unit Action button end here: 20.11.2020 10:40PM Javed & Mohd Saad**********

# # ********** Delete_Unit Action button start here: 16.11.2020 12:38AM Javed Farooqui**********


# def Delete_Unit(request, id):
#     UNT = Unit.objects.get(pk=id)
#     UNT.delete()
#     messages.success(
#         request, 'Congratulations...! Unit successfully Deleted.')
#     UNT = Unit.objects.all()
#     return render(request, 'Unit_Overview.html', {'ADUNIT': UNT})
# # ********** Delete_Unit Action button end here: 16.11.2020 12:36AM Javed Farooqui**********

# # **************************************************************************************************************************


# # *********Class Category_Type Defination Start Here---31-10-2020 02.22AM- Javed Farooqui *******
# def Category_Type(request):
#     if request.method == 'POST':
#         ADCATTYP = F_CategoryType(request.POST)
#         if ADCATTYP.is_valid():
#             CATTP = ADCATTYP.cleaned_data['CatType']
#             CATDSC = ADCATTYP.cleaned_data['desc']
#             ADCATTYP = CategoryType(CatType=CATTP, desc=CATDSC)
#             ADCATTYP.save()
#             messages.success(
#                 request, 'Congratulations...! Category Type successfully added.')
#     else:
#         ADCATTYP = F_CategoryType()
#     CAT = CategoryType.objects.all()
#     return render(request, 'Category_Type.html', {'form': ADCATTYP, 'ADCTTP': CAT})
# # *********Class Property Defination End Here---31-10-2020 02:10AM- Javed Farooqui *******

# # ********** Delete Action button start here: 31.10.2020 03:00PM Javed Farooqui**********


# def delete_category(request, id):
#     CTP = CategoryType.objects.get(pk=id)
#     CTP.delete()
#     messages.success(
#         request, 'Congratulations...! Category Type successfully Deleted.')
#     CAT = CategoryType.objects.all()
#     return render(request, 'Category_Type.html', {'ADCTTP': CAT})
# # ********** Delete Action button end here: 31.10.2020 03:15AM Javed Farooqui**********

# # ********** View Catagory_Type Action button start here: 06-11-2020 02.47AM Javed Farooqui**********


# def View_Cattyp(request, id):
#     pi = CategoryType.objects.get(pk=id)
#     ADCATTYP = F_CategoryType(request.POST, instance=pi)
#     if ADCATTYP.is_valid():
#         ADCATTYP.save()
#         messages.success(
#             request, 'Congratulations...! Category Type successfully Updated.')
#     else:
#         pi = CategoryType.objects.get(pk=id)
#         ADCATTYP = F_CategoryType(instance=pi)
#     return render(request, 'View_Category_Type.html', {'pi': pi})
# # ********** View Catagory_Type button end here: 06-11-2020 02.48AM Javed Farooqui**********

# # ********** update_Cattyp Action button start here: 31.10.2020 03:20PM Javed Farooqui**********


# def update_Cattyp(request, id):
#     pi = CategoryType.objects.get(pk=id)
#     ADCATTYP = F_CategoryType(request.POST, instance=pi)
#     if ADCATTYP.is_valid():
#         ADCATTYP.save()
#         messages.success(
#             request, 'Congratulations...! Category Type successfully Updated.')
#     else:
#         pi = CategoryType.objects.get(pk=id)
#         ADCATTYP = F_CategoryType(instance=pi)
#     return render(request, 'Update_Category_Type.html', {'pi': pi})
# # ********** update_Cattyp Action button end here: 31.10.2020 03:33PM Javed Farooqui**********


# # ******************************************************************************************************************************


# # *********Class Property Defination Start Here---31-10-2020 03.35AM- Javed Farooqui *******
# def Ownership_Type(request):
#     if request.method == 'POST':
#         ADOWNTYP = f_OwnershipType(request.POST)
#         if ADOWNTYP.is_valid():
#             OWNTP = ADOWNTYP.cleaned_data['OwnershipType']
#             OWNDSC = ADOWNTYP.cleaned_data['desc']
#             ADOWNTYP = OwnershipType(OwnershipType=OWNTP, desc=OWNDSC)
#             ADOWNTYP.save()
#             messages.success(
#                 request, 'Congratulations...! Ownership Type successfully added.')
#     else:
#         ADOWNTYP = f_OwnershipType()
#     OWN = OwnershipType.objects.all()
#     return render(request, 'Ownership_Type.html', {'form': ADOWNTYP, 'ADOWTP': OWN})
# # *********Class Property Defination End Here---31-10-2020 04:00AM- Javed Farooqui *******

# # ********** Delete Action button start here: 31.10.2020 03:35PM Javed Farooqui**********


# def delete_Ownership(request, id):
#     CTP = OwnershipType.objects.get(pk=id)
#     CTP.delete()
#     messages.success(
#         request, 'Congratulations...! Ownership Type successfully Deleted.')
#     OWN = OwnershipType.objects.all()
#     return render(request, 'Ownership_Type.html', {'ADOWTP': OWN})
# # ********** Delete Action button End here: 31.10.2020 04:05AM Javed Farooqui**********

# # ********** View_Doc_Type Action button start here: 06-11-2020 02.45AM Javed Farooqui**********


# def View_Ownership(request, id):
#     pi = OwnershipType.objects.get(pk=id)
#     ADOWNTYP = f_OwnershipType(request.POST, instance=pi)
#     if ADOWNTYP.is_valid():
#         ADOWNTYP.save()
#         messages.success(
#             request, 'Congratulations...! Ownership Type successfully Updated.')
#     else:
#         pi = OwnershipType.objects.get(pk=id)
#         ADOWNTYP = f_OwnershipType(instance=pi)
#     return render(request, 'View_Ownership_Type.html', {'pi': pi})
# # ********** View_Doc_Type Action button End here: 06-11-2020 02.46AM Javed Farooqui**********

# # ********** Update_Doc_Type Action button start here: 31.10.2020 03:45PM Javed Farooqui**********


# def update_Ownership(request, id):
#     pi = OwnershipType.objects.get(pk=id)
#     ADOWNTYP = f_OwnershipType(request.POST, instance=pi)
#     if ADOWNTYP.is_valid():
#         ADOWNTYP.save()
#         messages.success(
#             request, 'Congratulations...! Ownership Type successfully Updated.')
#     else:
#         pi = OwnershipType.objects.get(pk=id)
#         ADOWNTYP = f_OwnershipType(instance=pi)
#     return render(request, 'Update_Ownership_Type.html', {'pi': pi})
# # ********** Update_Doc_Type Action button End here: 31.10.2020 04:05PM Javed Farooqui**********


# # ******************************************************************************************************************************


# # *********Class Property_Type Defination Start Here---31-10-2020 04.30PM- Javed Farooqui *******
# def Property_Type(request):
#     if request.method == 'POST':
#         ADPRTTYP = F_PropertyType(request.POST)
#         if ADPRTTYP.is_valid():
#             PRTCTID = ADPRTTYP.cleaned_data['CatId']
#             PRTTP = ADPRTTYP.cleaned_data['PrtType']
#             PRTTDSC = ADPRTTYP.cleaned_data['desc']
#             ADPRTTYP = PropertyType(CatId=PRTCTID, PrtType=PRTTP, desc=PRTTDSC)
#             ADPRTTYP.save()
#             messages.success(
#                 request, 'Congratulations...! Property Type successfully added.')
#     else:
#         ADPRTTYP = F_PropertyType()
#     PTAT = PropertyType.objects.all()
#     CAT = CategoryType.objects.all()
#     return render(request, 'Property_Type.html', {'form': ADPRTTYP, 'PTAT': PTAT, 'CTID': CAT})
# # *********Class Property_Type Defination End Here---31-10-2020 05:35PM- Javed Farooqui *******

# # ********** Delete Property_Type Action button start here: 31.10.2020 04:30PM Javed Farooqui**********


# def Delete_Property_Type(request, id):
#     PTP = PropertyType.objects.get(pk=id)
#     PTP.delete()
#     messages.success(
#         request, 'Congratulations...! Property Type successfully Deleted.')
#     PTAT = PropertyType.objects.all()
#     return render(request, 'Property_Type.html', {'PTAT': PTAT})
# # ********** Delete Property_Type Action button End here: 31.10.2020 05:35PM Javed Farooqui**********

# # ********** View_Prop_Type Action button start here: 06-11-2020 02.43AM Javed Farooqui**********


# def View_Property_Type(request, id):
#     pi = PropertyType.objects.get(pk=id)
#     ADPRTTYP = F_PropertyType(request.POST, instance=pi)
#     if ADPRTTYP.is_valid():
#         ADPRTTYP.save()
#         messages.success(
#             request, 'Congratulations...! Property Type successfully Updated.')
#     else:
#         pi = PropertyType.objects.get(pk=id)
#         ADPRTTYP = F_PropertyType(instance=pi)
#     CAT = CategoryType.objects.all()
#     return render(request, 'View_Property_Type.html', {'ip': pi, 'temp': CAT})
# # ********** View_Prop_Type Action button End here: 06-11-2020 02.44AM Javed Farooqui**********

# # ********** Update_Prop_Type Action button start here: 31.10.2020 04:30PM Javed Farooqui**********


# def Update_Property_Type(request, id):
#     pi = PropertyType.objects.get(pk=id)
#     ADPRTTYP = F_PropertyType(request.POST, instance=pi)
#     if ADPRTTYP.is_valid():
#         ADPRTTYP.save()
#         messages.success(
#             request, 'Congratulations...! Property Type successfully Updated.')
#     else:
#         pi = PropertyType.objects.get(pk=id)
#         ADPRTTYP = F_PropertyType(instance=pi)
#     CAT = CategoryType.objects.all()
#     return render(request, 'Update_Property_Type.html', {'ip': pi, 'temp': CAT})
# # ********** Update_Prop_Type Action button End here: 31.10.2020 03:33PM Javed Farooqui**********


# # ******************************************************************************************************************************


# # *********Class Payment_Mode_Type Defination Start Here---02-11-2020 07.40PM- Javed Farooqui *******
# def PayMode_Type(request):
#     if request.method == 'POST':
#         ADPYMD = F_PayModeType(request.POST)
#         if ADPYMD.is_valid():
#             PMT = ADPYMD.cleaned_data['PayType']
#             PMTDSC = ADPYMD.cleaned_data['desc']
#             ADPYMD = PayModeType(PayType=PMT, desc=PMTDSC)
#             ADPYMD.save()
#             messages.success(
#                 request, 'Congratulations...! Payment Mode Type successfully added.')
#     else:
#         ADPYMD = F_PayModeType()
#     PMTY = PayModeType.objects.all()
#     return render(request, 'PayMode_Type.html', {'form': ADPYMD, 'ADPMT': PMTY})
# # *********Class Payment_Mode_Type Defination End Here---02-11-2020 08.00PM- Javed Farooqui *******

# # *********Delete Payment_Mode_Type Defination Start Here---02-11-2020 08.01PM- Javed Farooqui *******


# def Delete_PayModeType(request, id):
#     PMTP = PayModeType.objects.get(pk=id)
#     PMTP.delete()
#     messages.success(
#         request, 'Congratulations...! Payment Mode Type successfully Deleted.')
#     PTY = PayModeType.objects.all()
#     return render(request, 'PayMode_Type.html', {'ADPMT': PTY})
# # ********** Delete Payment_Mode_Type Action button end here: 02-11-2020 08.20PM Javed Farooqui**********

# # **********View Payment_Mode_Type Action button start here: 06-11-2020 02.41AM Javed Farooqui**********


# def View_PayModeType(request, id):
#     PTy = PayModeType.objects.get(pk=id)
#     ADPRTTYP = F_PayModeType(request.POST, instance=PTy)
#     if ADPRTTYP.is_valid():
#         ADPRTTYP.save()
#         messages.success(
#             request, 'Congratulations...! Property Type successfully Updated.')
#     else:
#         PTy = PayModeType.objects.get(pk=id)
#         ADPRTTYP = F_PayModeType(instance=PTy)
#     return render(request, 'View_PayMode_Type.html', {'PAYTYP': PTy})
# # ********** View Payment_Mode_Type Action button end here: 06-11-2020 02.41AM Javed Farooqui**********

# # **********Update Payment_Mode_Type Action button start here: 02-11-2020 08.22PM Javed Farooqui**********


# def Update_PayModeType(request, id):
#     PTy = PayModeType.objects.get(pk=id)
#     ADPRTTYP = F_PayModeType(request.POST, instance=PTy)
#     if ADPRTTYP.is_valid():
#         ADPRTTYP.save()
#         messages.success(
#             request, 'Congratulations...! Payment Mode Type successfully Updated.')
#     else:
#         PTy = PayModeType.objects.get(pk=id)
#         ADPRTTYP = F_PayModeType(instance=PTy)
#     return render(request, 'Update_PayMode_Type.html', {'PAYTYP': PTy})
# # ********** Update Payment_Mode_Type Action button end here: 02-11-2020 08.37PM Javed Farooqui**********


# # ******************************************************************************************************************************


# # *********Class Status_Request_Type Defination Start Here---02-11-2020 09:44PM- Javed Farooqui *******
# def StatusReq_Type(request):
#     if request.method == 'POST':
#         ADSTRQ = F_StatusReqType(request.POST)
#         if ADSTRQ.is_valid():
#             SRT = ADSTRQ.cleaned_data['StRqty']
#             SRTDSC = ADSTRQ.cleaned_data['desc']
#             ADSTRQ = StatusReqType(StRqty=SRT, desc=SRTDSC)
#             ADSTRQ.save()
#             messages.success(
#                 request, 'Congratulations...! Status Request Type successfully added.')
#     else:
#         ADSTRQ = F_StatusReqType()
#     SRTY = StatusReqType.objects.all()
#     return render(request, 'StatusReq_Type.html', {'form': ADSTRQ, 'ADSRQ': SRTY})
# # *********Class Status_Request_Type Defination End Here---02-11-2020 10:08PM- Javed Farooqui *******

# # *********Delete Status_Request_Type Defination Start Here---02-11-2020 10:08PM- Javed Farooqui *******


# def Delete_StatusReqType(request, id):
#     SRQ = StatusReqType.objects.get(pk=id)
#     SRQ.delete()
#     messages.success(
#         request, 'Congratulations...! Status Request Type successfully Deleted.')
#     SRTY = StatusReqType.objects.all()
#     return render(request, 'StatusReq_Type.html', {'ADSRQ': SRTY})
# # ********** Delete Status_Request_Type Action button end here: 02-11-2020 08:20PM Javed Farooqui**********

# # **********View Status_Request_Type Action button start here: 06-11-2020 02.39AM Javed Farooqui**********


# def View_StatusReqType(request, id):
#     STT = StatusReqType.objects.get(pk=id)
#     ADSRTYP = F_StatusReqType(request.POST, instance=STT)
#     if ADSRTYP.is_valid():
#         ADSRTYP.save()
#         messages.success(
#             request, 'Congratulations...! Status Request Type successfully Updated.')
#     else:
#         STT = StatusReqType.objects.get(pk=id)
#         ADSRTYP = F_StatusReqType(instance=STT)
#     return render(request, 'View_StatusReq_Type.html', {'pi': STT})
# # ********** View Status_Request_Type Action button end here: 06-11-2020 02.39AM Javed Farooqui**********

# # **********Update Status_Request_Type Action button start here: 02-11-2020 10:35PM Javed Farooqui**********


# def Update_StatusReqType(request, id):
#     STT = StatusReqType.objects.get(pk=id)
#     ADSRTYP = F_StatusReqType(request.POST, instance=STT)
#     if ADSRTYP.is_valid():
#         ADSRTYP.save()
#         messages.success(
#             request, 'Congratulations...! Status Request Type successfully Updated.')
#     else:
#         STT = StatusReqType.objects.get(pk=id)
#         ADSRTYP = F_StatusReqType(instance=STT)
#     return render(request, 'Update_StatusReq_Type.html', {'pi': STT})
# # ********** Update Status_Request_Type Action button end here: 02-11-2020 10:00PM Javed Farooqui**********


# # ******************************************************************************************************************************


# # *********Class Tenant_Request_Type Defination Start Here---04-11-2020 08.15PM- Javed Farooqui *******
# def TenantReq_Type(request):
#     if request.method == 'POST':
#         ADTNTRQTY = F_TenantReqType(request.POST)
#         if ADTNTRQTY.is_valid():
#             TNR = ADTNTRQTY.cleaned_data['TenantReqType']
#             TNRDSC = ADTNTRQTY.cleaned_data['desc']
#             ADTNTRQTY = TenantReqType(TenantReqType=TNR, desc=TNRDSC)
#             ADTNTRQTY.save()
#             messages.success(
#                 request, 'Congratulations...! Tenant Request Type successfully added.')
#     else:
#         ADTNTRQTY = F_TenantReqType()
#     TR = TenantReqType.objects.all()
#     return render(request, 'TenantReq_Type.html', {'form': ADTNTRQTY, 'ADTNRQ': TR})
# # *********Class Tenant_Request_Type Defination End Here---04-11-2020 08.44PM- Javed Farooqui *******

# # ********** Delete Tenant_Request_Type Action button start here: 04-11-2020 08.15PM Javed Farooqui**********


# def Delete_TenantReqType(request, id):
#     TRQ = TenantReqType.objects.get(pk=id)
#     TRQ.delete()
#     messages.success(
#         request, 'Congratulations...! Tenant Request Type successfully Deleted.')
#     TR = TenantReqType.objects.all()
#     return render(request, 'TenantReq_Type.html', {'ADTNRQ': TR})
# # ********** Delete Tenant_Request_Type Action button End here: 04-11-2020 08.44PM Javed Farooqui**********

# # ********** View Tenant_Request_Type Action button start here: 06-11-2020 02.36AM Javed Farooqui**********


# def View_TenantReqType(request, id):
#     pi = TenantReqType.objects.get(pk=id)
#     ADTNTRQTY = F_TenantReqType(request.POST, instance=pi)
#     if ADTNTRQTY.is_valid():
#         ADTNTRQTY.save()
#         messages.success(
#             request, 'Congratulations...! Tenant Request Type successfully Updated.')
#     else:
#         pi = TenantReqType.objects.get(pk=id)
#         ADTNTRQTY = F_TenantReqType(instance=pi)
#     return render(request, 'View_TenantReq_Type.html', {'pi': pi})
# # ********** View Tenant_Request_Type Action button End here: 06-11-2020 02.36AM Javed Farooqui**********

# # ********** Update Tenant_Request_Type Action button start here: 04-11-2020 08.15PM Javed Farooqui**********


# def Update_TenantReqType(request, id):
#     pi = TenantReqType.objects.get(pk=id)
#     ADTNTRQTY = F_TenantReqType(request.POST, instance=pi)
#     if ADTNTRQTY.is_valid():
#         ADTNTRQTY.save()
#         messages.success(
#             request, 'Congratulations...! Tenant Request Type successfully Updated.')
#     else:
#         pi = TenantReqType.objects.get(pk=id)
#         ADTNTRQTY = F_TenantReqType(instance=pi)
#     return render(request, 'Update_TenantReq_Type.html', {'pi': pi})
# # ********** Update Tenant_Request_Type Action button End here: 04-11-2020 08.44PM Javed Farooqui**********


# # ******************************************************************************************************************************


# # *********Class Contract_Request_Type Defination Start Here---04-11-2020 08.48PM- Javed Farooqui ******************************
# def ContractReq_Type(request):
#     if request.method == 'POST':
#         ADCNTRQTY = F_ContractReqType(request.POST)
#         if ADCNTRQTY.is_valid():
#             CTR = ADCNTRQTY.cleaned_data['ContractReqType']
#             CTRDSC = ADCNTRQTY.cleaned_data['desc']
#             ADCNTRQTY = ContractReqType(ContractReqType=CTR, desc=CTRDSC)
#             ADCNTRQTY.save()
#             messages.success(
#                 request, 'Congratulations...! Contract Request Type successfully added.')
#     else:
#         ADCNTRQTY = F_ContractReqType()
#     CRT = ContractReqType.objects.all()
#     return render(request, 'ContractReq_Type.html', {'form': ADCNTRQTY, 'ADCNRQ': CRT})
# # *********Class Contract_Request_Type Defination End Here---04-11-2020 09:11PM- Javed Farooqui *******

# # ********** Delete Contract_Request_Type Action button start here: 04-11-2020 08.15PM Javed Farooqui**********


# def Delete_ContractReqType(request, id):
#     TRQ = ContractReqType.objects.get(pk=id)
#     TRQ.delete()
#     messages.success(
#         request, 'Congratulations...! Contract Request Type successfully Deleted.')
#     CRT = ContractReqType.objects.all()
#     return render(request, 'ContractReq_Type.html', {'ADCNRQ': CRT})
#    # ********** Delete Contract_Request_Type Action button start here: 04-11-2020 09:11PM Javed Farooqui**********
# # ********** Delete Contract_Request_Type Action button end here: 04-11-2020 09:11PM Javed Farooqui**************************

# # ********** View Contract_Request_Type Action button start here: 06-11-2020 02.30AM Javed Farooqui**********


# def View_ContractReqType(request, id):
#     pi = ContractReqType.objects.get(pk=id)
#     ADCNTRQTY = F_ContractReqType(request.POST, instance=pi)
#     if ADCNTRQTY.is_valid():
#         ADCNTRQTY.save()
#         messages.success(
#             request, 'Congratulations...! Contract Request Type successfully Updated.')
#     else:
#         pi = ContractReqType.objects.get(pk=id)
#         ADCNTRQTY = F_ContractReqType(instance=pi)
#     return render(request, 'View_ContractReq_Type.html', {'pi': pi})
# # ********** View Contract_Request_Type Action button end here: 06-11-2020 02.32AM Javed Farooqui**************************

# # ********** Update Contract_Request_Type Action button start here: 04-11-2020 08.15PM Javed Farooqui**********


# def Update_ContractReqType(request, id):
#     pi = ContractReqType.objects.get(pk=id)
#     ADCNTRQTY = F_ContractReqType(request.POST, instance=pi)
#     if ADCNTRQTY.is_valid():
#         ADCNTRQTY.save()
#         messages.success(
#             request, 'Congratulations...! Contract Request Type successfully Updated.')
#     else:
#         pi = ContractReqType.objects.get(pk=id)
#         ADCNTRQTY = F_ContractReqType(instance=pi)
#     return render(request, 'Update_ContractReq_Type.html', {'pi': pi})
# # ********** Update Contract_Request_Type Action button end here: 04-11-2020 09:11PM Javed Farooqui**************************


# # ******************************************************************************************************************************


# # *********Class Documents_Type Defination Start Here---04-11-2020 10.15PM- Javed Farooqui *************************************
# def Documents_Type(request):
#     if request.method == 'POST':
#         ADDOCTY = F_DocumentsType(request.POST)
#         if ADDOCTY.is_valid():
#             DCT = ADDOCTY.cleaned_data['DocumentsType']
#             DCTDSC = ADDOCTY.cleaned_data['desc']
#             ADDOCTY = DocumentsType(DocumentsType=DCT, desc=DCTDSC)
#             ADDOCTY.save()
#             messages.success(
#                 request, 'Congratulations...! Documents Type successfully added.')
#     else:
#         ADDOCTY = F_DocumentsType()
#     DOT = DocumentsType.objects.all()
#     return render(request, 'Documents_Type.html', {'form': ADDOCTY, 'ADDT': DOT})
# # *********Class Documents_Type Defination End Here---04-11-2020 10.39PM- Javed Farooqui *******

# # ********** Delete Documents_Type Action button start here: 04-11-2020 10.15PM Javed Farooqui***************************


# def Delete_DocumentsType(request, id):
#     TRQ = DocumentsType.objects.get(pk=id)
#     TRQ.delete()
#     messages.success(
#         request, 'Congratulations...! Documents Type successfully Deleted.')
#     DOT = DocumentsType.objects.all()
#     return render(request, 'Documents_Type.html', {'ADDT': DOT})
# # ********** Delete Documents_Type Action button end here: 04-11-2020 10.39PM Javed Farooqui***************************

# # ********** View Documents_Type Action button start here: 05-11-2020 12.30PM Javed Farooqui**********


# def View_DocumentsType(request, id):
#     pi = DocumentsType.objects.get(pk=id)
#     ADDOCTY = F_DocumentsType(request.POST, instance=pi)
#     if ADDOCTY.is_valid():
#         ADDOCTY.save()
#         messages.success(
#             request, 'Congratulations...! Documents Type successfully Updated.')
#     else:
#         pi = DocumentsType.objects.get(pk=id)
#         ADDOCTY = F_DocumentsType(instance=pi)
#     return render(request, 'View_Documents_Type.html', {'pi': pi})
# # ********** View Documents_Type Action button end here: 05-11-2020 12.39PM Javed Farooqui*********************************

# # ********** Update Documents_Type Action button start here: 04-11-2020 10.15PM Javed Farooqui**********


# def Update_DocumentsType(request, id):
#     pi = DocumentsType.objects.get(pk=id)
#     ADDOCTY = F_DocumentsType(request.POST, instance=pi)
#     if ADDOCTY.is_valid():
#         ADDOCTY.save()
#         messages.success(
#             request, 'Congratulations...! Documents Type successfully Updated.')
#     else:
#         pi = DocumentsType.objects.get(pk=id)
#         ADDOCTY = F_DocumentsType(instance=pi)
#     return render(request, 'Update_Documents_Type.html', {'pi': pi})
# # ********** Update Documents_Type Action button end here: 04-11-2020 10.39PM Javed Farooqui*********************************


# # ******************************************************************************************************************************


# # *********Class Occupancy_Type Defination Start Here---07-11-2020 01.15PM- Javed Farooqui *************************************
# def Occupancy_Type(request):
#     if request.method == 'POST':
#         OCPTYP = F_OccupancyType(request.POST)
#         if OCPTYP.is_valid():
#             OPT = OCPTYP.cleaned_data['OccupancyType']
#             OPTDSC = OCPTYP.cleaned_data['desc']
#             OCPTYP = OccupancyType(OccupancyType=OPT, desc=OPTDSC)
#             OCPTYP.save()
#             messages.success(
#                 request, 'Congratulations...! Occupancy Type successfully added.')
#     else:
#         OCPTYP = F_OccupancyType()
#     OPTY = OccupancyType.objects.all()
#     return render(request, 'Occupancy_Type.html', {'form': OCPTYP, 'OPTY': OPTY})
# # *********Class Occupancy_Type Defination End Here---04-11-2020 10.39PM- Javed Farooqui *******

# # ********** Delete Occupancy_Type Action button start here: 04-11-2020 10.15PM Javed Farooqui***************************


# def Delete_OccupancyType(request, id):
#     TRQ = OccupancyType.objects.get(pk=id)
#     TRQ.delete()
#     messages.success(
#         request, 'Congratulations...! Occupancy Type successfully Deleted.')
#     OPTY = OccupancyType.objects.all()
#     return render(request, 'Occupancy_Type.html', {'OPTY': OPTY})
# # ********** Delete Occupancy_Type Action button end here: 04-11-2020 10.39PM Javed Farooqui***************************

# # ********** View Occupancy_Type Action button start here: 05-11-2020 12.30PM Javed Farooqui**********


# def View_OccupancyType(request, id):
#     pi = OccupancyType.objects.get(pk=id)
#     OCPTYP = F_OccupancyType(request.POST, instance=pi)
#     if OCPTYP.is_valid():
#         OCPTYP.save()
#         messages.success(
#             request, 'Congratulations...! Occupancy Type successfully Updated.')
#     else:
#         pi = OccupancyType.objects.get(pk=id)
#         OCPTYP = F_OccupancyType(instance=pi)
#     return render(request, 'View_Occupancy_Type.html', {'pi': pi})
# # ********** View Occupancy_Type Action button end here: 05-11-2020 12.39PM Javed Farooqui*********************************

# # ********** Update Occupancy_Type Action button start here: 04-11-2020 10.15PM Javed Farooqui**********


# def Update_OccupancyType(request, id):
#     pi = OccupancyType.objects.get(pk=id)
#     OCPTYP = F_OccupancyType(request.POST, instance=pi)
#     if OCPTYP.is_valid():
#         OCPTYP.save()
#         messages.success(
#             request, 'Congratulations...! Occupancy Type successfully Updated.')
#     else:
#         pi = OccupancyType.objects.get(pk=id)
#         OCPTYP = F_OccupancyType(instance=pi)
#     return render(request, 'Update_Occupancy_Type.html', {'pi': pi})
# # ********** Update Occupancy_Type Action button end here: 04-11-2020 10.39PM Javed Farooqui*********************************


# # ************************************************************************************************************************

# # ********** Update Add_Tenant Action button start here: 21-11-2020 03:10PM Javed Farooqui**********
# def Add_Tenant(request):
#     if request.method == "POST":
#         ADTNT = F_Tenant(request.POST)
#         if ADTNT.is_valid():
#             userid = ADTNT.cleaned_data['user_id']
#             userpwrd = ADTNT.cleaned_data['user_password']
#             usrfsnm = ADTNT.cleaned_data['usr_f_name']
#             usrmdnm = ADTNT.cleaned_data['usr_m_name']
#             usrlsnm = ADTNT.cleaned_data['usr_l_name']
#             email = ADTNT.cleaned_data['email']
#             pcont = ADTNT.cleaned_data['pcontact']
#             scont = ADTNT.cleaned_data['scontact']
#             marital = ADTNT.cleaned_data['marry_status']
#             national = ADTNT.cleaned_data['nationality']
#             roll = ADTNT.cleaned_data['rollid']
#             tenant = Tenant(user_id=userid, user_password=userpwrd, usr_f_name=usrfsnm, usr_m_name=usrmdnm, usr_l_name=usrlsnm,
#                             email=email, pcontact=pcont, scontact=scont, marry_status=marital, nationality=national, rollid=roll)
#         tenant.save()
#         messages.success(
#             request, 'Congratulations...! Tenant successfully added.')
#     else:
#         ADTNT = F_Tenant()
#     TENT = Tenant.objects.all()
#     return render(request, 'Add_Tenant.html')
# # ********** Update Add_Tenant Action button end here: 21-11-2020 03:35PM Javed Farooqui**********

# # ********** Update Tenant_Contract Action button start here: 20-11-2020 03:10PM Javed Farooqui**********


# def Tenant_Contract(request):
#     if request.method == 'POST':
#         ADTNTCONTR = F_TenantContract(request.POST)
#         if ADTNTCONTR.is_valid():
#             PROPID = ADTNTCONTR.cleaned_data['PropID']
#             UNITID = ADTNTCONTR.cleaned_data['UnitID']
#             CONTRACTNO = ADTNTCONTR.cleaned_data['ContractNo']
#             STARTDATE = ADTNTCONTR.cleaned_data['StartDate']
#             ENDDATE = ADTNTCONTR.cleaned_data['EndDate']
#             DISCOUNT = ADTNTCONTR.cleaned_data['Discount']
#             ANNUALRENT = ADTNTCONTR.cleaned_data['AnnualRent']
#             SECURITYDEP = ADTNTCONTR.cleaned_data['SecurityDep']
#             COMMISSION = ADTNTCONTR.cleaned_data['Commission']
#             EMI = ADTNTCONTR.cleaned_data['Installments']
#             REMARK = ADTNTCONTR.cleaned_data['Remark']
#             SMSNOTIFY = ADTNTCONTR.cleaned_data['SMSNotify']
#             EMAILNOTIFY = ADTNTCONTR.cleaned_data['EmailNotify']
#             ADTNTCONTR = TenantContract(PropID=PROPID, UnitID=UNITID, ContractNo=CONTRACTNO, StartDate=STARTDATE, EndDate=ENDDATE, Discount=DISCOUNT,
#                                         AnnualRent=ANNUALRENT, SecurityDep=SECURITYDEP, Commission=COMMISSION, Installments=EMI, Remark=REMARK, SMSNotify=SMSNOTIFY, EmailNotify=EMAILNOTIFY)
#             ADTNTCONTR.save()
#             messages.success(
#                 request, 'Congratulations...! Occupancy Type successfully added.')
#     else:
#         ADTNTCONTR = F_TenantContract()
#     TNTCTRT = TenantContract.objects.all()
#     UNT = Unit.objects.all()
#     PRT = Property.objects.all()
#     return render(request, 'Tenant_Contract.html', {'form': ADTNTCONTR, 'TNTCTRT': TNTCTRT, 'ADUNIT': UNT, 'ADPRPRTY': PRT})
# # ********** Update Tenant_Contract Action button end here: 21-11-2020 03:35PM Javed Farooqui**********

# # **********************************************************************************************************************


# def Add_User(request):
#     if request.method == "POST":
#         OCPTYP = F_User(request.POST)
#         if OCPTYP.is_valid():
#             userid = OCPTYP.cleaned_data['user_id']
#             userpwrd = OCPTYP.cleaned_data['user_password']
#             usrfsnm = OCPTYP.cleaned_data['usr_f_name']
#             usrmdnm = OCPTYP.cleaned_data['usr_m_name']
#             usrlsnm = OCPTYP.cleaned_data['usr_l_name']
#             email = OCPTYP.cleaned_data['email']
#             pcont = OCPTYP.cleaned_data['pcontact']
#             scont = OCPTYP.cleaned_data['scontact']
#             marital = OCPTYP.cleaned_data['marry_status']
#             national = OCPTYP.cleaned_data['nationality']
#             roll = OCPTYP.cleaned_data['rollid']
#             Usr = User(user_id=userid, user_password=userpwrd, usr_f_name=usrfsnm, usr_m_name=usrmdnm, usr_l_name=usrlsnm,
#                        email=email, pcontact=pcont, scontact=scont, marry_status=marital, nationality=national, rollid=roll)
#         Usr.save()
#         messages.success(
#             request, 'Congratulations...! User successfully added.')
#     else:
#         OCPTYP = F_User()
#     OPTY = User.objects.all()
#     return render(request, 'Add_User.html')

# # ******************************************************


# # ********** Update Review_Documents Action button start here: 20-11-2020 10.15PM Javed Farooqui**********
# def Review_Documents(request):
#     # pi = TenantContract.objects.get(pk=id)
#     # ADTNTCONTR = F_TenantContract(request.POST, instance=pi)
#     # if ADTNTCONTR.is_valid():
#     #         ADTNTCONTR.save()
#     #         messages.success(
#     #         request, 'Congratulations...! Occupancy Type successfully Updated.')
#     # else:
#     #     pi = TenantContract.objects.get(pk=id)
#     #     ADTNTCONTR = F_TenantContract(instance=pi)
#     return render(request, 'Review_Documents.html')
# # ********** Update Review_Documents Action button end here: 20-11-2020 12.39AM Javed Farooqui************

# # ********** Update Upload_Documents Action button start here: 21-11-2020 04.00PM Mohd Saad**********


# # ********** Update Upload_Documents Action button end here: 21-11-2020 12.39AM Javed Farooqui************
