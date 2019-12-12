import os
from django.contrib.gis.utils import LayerMapping
from .models import Counties

# Auto-generated `LayerMapping` dictionary for Counties model

#counties_mapping = {
#    'cellcode': 'CELLCODE',
#    'eoforigin': 'EOFORIGIN',
#    'noforigin': 'NOFORIGIN',
#    'geom': 'MULTIPOLYGON',
#}


#countie_mapping = {
#    'counties': 'Counties',
#    'codes': 'Codes',
#    'cty_code': 'Cty_CODE',
#    'dis': 'dis',
#    'geom': 'MULTIPOLYGON',
#}

#ie_10km.shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'ireland_shapefile/ie_10km.shp'))


def run(verbose=True):
    lm = LayerMapping(Counties, countie_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)
