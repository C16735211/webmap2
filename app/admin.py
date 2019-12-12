from django.contrib.gis import admin
from .models import WorldBorder, Incidences
from leaflet.admin import LeafletGeoAdmin


# Register your models here.
class IncidencesAdmin(LeafletGeoAdmin):
    #pass
    list_display = ('name', "location")


admin.site.register(WorldBorder, admin.GeoModelAdmin)
admin.site.register(Incidences, IncidencesAdmin)
