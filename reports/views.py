from django.db.models.query_utils import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django_renderpdf.views import PDFView
from csv_export.views import CSVExportView


from new_door.models import Entity, Property, Unit
from profiles.models import Profile

import datetime
# Create your views here.
today = datetime.date.today()


class EntityPDFView(PDFView):

    template_name = 'report/entity_report.html'
    prompt_download = True
    download_name = 'Property Unit Report'

    def get_context_data(self, *args, **kwargs):
        """Pass some extra context to the template."""
        context = super().get_context_data(*args, **kwargs)

        context['entities'] = Entity.objects.filter(
            manager=kwargs["user_id"]
        )
        context['date'] = today
        return context


class EntityCSVView(CSVExportView):
    model = Entity
    fields = '__all__'
    specify_separator = False
    filename = 'Entity Report.csv'

    def get_queryset(self):
        queryset = super(EntityCSVView, self).get_queryset()
        return queryset.filter(manager__id=self.request.user.pk)


class PropertyPDFView(PDFView):

    template_name = 'report/property_report.html'

    def get_context_data(self, *args, **kwargs):
        """Pass some extra context to the template."""
        context = super().get_context_data(*args, **kwargs)

        context['properties'] = Property.objects.filter(
            Q(entity__manager__is_manager=True) & Q(
                entity__manager__pk=kwargs['pk'])
        )
        context['date'] = today
        return context


class PropertyCSVView(CSVExportView):
    model = Property
    fields = '__all__'
    specify_separator = False
    filename = 'Property.csv'

    def get_queryset(self):
        queryset = super(PropertyCSVView, self).get_queryset()
        return queryset.filter(entity__manager__pk=self.request.user.pk)


class PropertyUnitPDFView(PDFView):

    template_name = 'report/test.html'

    def get_context_data(self, *args, **kwargs):
        """Pass some extra context to the template."""
        context = super().get_context_data(*args, **kwargs)

        context['property'] = Property.objects.get(
            pk=kwargs["property_id"]
        )
        context['date'] = today
        return context

# Dashboard Rendering


@login_required
def report(request):
    manager_id = request.user.pk
    entities = Entity.objects.filter(manager__pk=manager_id)
    units = Unit.objects.filter(
        property_id_id__entity__manager__pk=manager_id)
    properties = Property.objects.filter(entity__manager__pk=manager_id)
    tenants = Profile.objects.filter(is_tenant=True)

    context = {
        "entities": entities,
        "units": units,
        "properties": properties,
        "tenants": tenants,
    }
    return render(request, 'report/index.html', context)


@login_required
def entity_report(request):
    user = request.user
    entities = Entity.objects.filter(
        Q(manager__pk=user.pk) & Q(manager__profile__is_manager=True)
    )

    if len(entities) == 0:
        return redirect('dashboard')
    context = {
        "entities": entities
    }
    return render(request, 'report/tests.html', context)


def property_unit_report(request, property_id):
    user = request.user
    manager_profile = get_object_or_404(Profile, pk=user.pk)
    property = Property.objects.get(
        pk=property_id
    )

    context = {
        "property": property
    }
    return render(request, 'report/test.html', context)


@login_required
def tenant_detail_report(request):
    return render(request, 'report/tenant_detail_report.html')


@login_required
def tenant_payment_report(request):
    return render(request, 'report/tenant_payment_report.html')


@login_required
def unpaid_tenant_report(request):
    return render(request, 'report/unpaid_tenant_report.html')
