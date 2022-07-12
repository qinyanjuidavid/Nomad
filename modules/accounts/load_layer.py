import os

from django.contrib.gis.utils import LayerMapping
from modules.accounts.models import Counties

counties_mapping = {
    'fid': 'fid',
    'objectid': 'OBJECTID',
    'code_id': 'ID',
    'name': 'Name',
    'code': 'Code',
    'shape_leng': 'Shape_Leng',
    'shape_area': 'Shape_Area',
    'area': 'Area',
    'geom': 'MULTIPOLYGON'
}

county_shp = os.path.abspath(os.path.join(
    os.path.dirname(__file__), 'data/County.shp'))


def run(verbose=True):
    lm = LayerMapping(Counties, county_shp, counties_mapping,
                      transform=False, encoding="iso-8859-1")
    lm.save(strict=True, verbose=verbose)
