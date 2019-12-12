from django.core.serializers import serialize
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from .models import Incidences


# Create your views here.
class MainPage(TemplateView):
    template_name = 'app/base.html'


def incidences_datasets(request):
    incidences = serialize('geojson', Incidences.objects.all())
    return HttpResponse(incidences, content_type='json')
