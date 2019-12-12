from __future__ import unicode_literals
from django.db import models

from django.contrib.gis.db import models
from django.db.models import Manager as GeoManager


# Create your models here.
class WorldBorder(models.Model):
    # Regular Django fields corresponding to the attributes in the
    # world borders shapefile.
    name = models.CharField(max_length=50)
    area = models.IntegerField()
    pop2005 = models.IntegerField('Population 2005')
    fips = models.CharField('FIPS Code', max_length=2)
    iso2 = models.CharField('2 Digit ISO', max_length=2)
    iso3 = models.CharField('3 Digit ISO', max_length=3)
    un = models.IntegerField('United Nations Code')
    region = models.IntegerField('Region Code')
    subregion = models.IntegerField('Sub-Region Code')
    lon = models.FloatField()
    lat = models.FloatField()

    # GeoDjango-specific: a geometry field (MultiPolygonField)
    mpoly = models.MultiPolygonField()

    # Returns the string representation of the model.
    def __str__(self):
        return self.name


class Incidences(models.Model):
    name = models.CharField(max_length=50)
    location = models.PointField(srid=4326)
    objects = models.Manager()

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = " Incidences"


#class Counties(models.Model):
#    cellcode = models.CharField(max_length=14)
#    eoforigin = models.BigIntegerField()
#    noforigin = models.BigIntegerField()
#    geom = models.MultiPolygonField(srid=4326)

class Counties(models.Model):
    counties = models.CharField(max_length=25)
    codes = models.IntegerField()
    cty_code = models.IntegerField()
    dis = models.IntegerField()
    geom = models.MultiPolygonField(srid=4326)

    def __unicode__(self):
        return self.counties


