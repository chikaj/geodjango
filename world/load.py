import os
from django.contrib.gis.utils import LayerMapping
from world.models import WorldBorder, StatesBorder, USCities, Rivers

world_mapping = {
    'fips': 'FIPS',
    'iso2': 'ISO2',
    'iso3': 'ISO3',
    'un': 'UN',
    'name': 'NAME',
    'area': 'AREA',
    'pop2005': 'POP2005',
    'region': 'REGION',
    'subregion': 'SUBREGION',
    'lon': 'LON',
    'lat': 'LAT',
    'mpoly': 'MULTIPOLYGON',
}

world_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),
    '../../vector_data/worldBorders.shp'))


statesborder_mapping = {
    'name': 'STATE_NAME',
    'state_fips': 'STATE_FIPS',
    'sub_region': 'SUB_REGION',
    'state_abbr': 'STATE_ABBR',
    'pop2010': 'POP2010',
    'pop2012': 'POP2012',
    'sqmi': 'SQMI',
    'geom': 'MULTIPOLYGON',
}

states_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),
    '../../vector_data/states.shp'))


uscities_mapping = {
    'name': 'NAME',
    'class_id': 'CLASS',
    'st': 'ST',
    'stfips': 'STFIPS',
    'arealand': 'AREALAND',
    'areawater': 'AREAWATER',
    'pop2000': 'POP2000',
    'pop2007': 'POP2007',
    'geom': 'POINT',
}

uscities_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),
    '../../vector_data/us_cities.shp'))


cities_mapping = {
    'name': 'NAME',
    'class_id': 'CLASS',
    'st': 'ST',
    'stfips': 'STFIPS',
    'arealand': 'AREALAND',
    'areawater': 'AREAWATER',
    'pop2000': 'POP2000',
    'pop2007': 'POP2007',
    'geom': 'POINT',
}

cities_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),
    '../../vector_data/us_cities.shp'))


rivers_mapping = {
    'scalerank': 'scalerank',
    'featurecla': 'featurecla',
    'name': 'name',
    'name_alt': 'name_alt',
    'geom': 'LINESTRING',
}

rivers_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),
    '../../vector_data/rivers.shp'))


def runWorld(verbose=True):
    lm = LayerMapping(WorldBorder, world_shp, world_mapping,
                      transform=False, encoding='iso-8859-1')

    lm.save(strict=True, verbose=verbose)


def runStates(verbose=True):
    lm = LayerMapping(StatesBorder, states_shp, statesborder_mapping,
                      transform=False, encoding='iso-8859-1')

    lm.save(strict=True, verbose=verbose)


def runUSCities(verbose=True):
    lm = LayerMapping(USCities, uscities_shp, uscities_mapping,
                      transform=False, encoding='iso-8859-1')

    lm.save(strict=True, verbose=verbose)


# def runCities(verbose=True):
#     lm = LayerMapping(Cities, cities_shp, cities_mapping,
#                       transform=False, encoding='iso-8859-1')

#     lm.save(strict=True, verbose=verbose)


def runRivers(verbose=True):
    lm = LayerMapping(Rivers, rivers_shp, rivers_mapping,
                      transform=False, encoding='iso-8859-1')

    lm.save(strict=True, verbose=verbose)
