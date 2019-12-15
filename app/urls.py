from django.conf.urls import include, url
from django.urls import path, include
from . import views

app_name = 'app'

urlpatterns = [
    url(r'^$', views.MainPage.as_view(), name='home'),
    url(r'^incidences/$', views.incidences_datasets, name='incidences'),
    path(r'', include('pwa.urls')),
]