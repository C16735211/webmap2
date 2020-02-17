from django.conf.urls import include, url
from django.urls import path, include
from . import views
from django.contrib import admin
from django.urls import path
from users import views as user_views

app_name = 'app'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    url(r'^$', views.MainPage.as_view(), name='home'),
    url(r'^incidences/$', views.incidences_datasets, name='incidences'),
    path(r'', include('pwa.urls')),
]
