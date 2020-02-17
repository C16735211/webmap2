from django.core.serializers import serialize
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from .models import Incidences
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
class MainPage(TemplateView):
    template_name = 'app/base.html'


@login_required
def home(request):
    return render(request, "home.html", {})


def incidences_datasets(request):
    incidences = serialize('geojson', Incidences.objects.all())
    return HttpResponse(incidences, content_type='json')
