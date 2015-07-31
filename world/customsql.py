from django.db import connection
import json


def getGeoJSON():
    cursor = connection.cursor()

    my_tab = 'public.world_statesborder'
    params = 'id, name, pop2012'
    cursor.execute("select geoqs2geojson(%s, %s)", [my_tab, params])
    # cursor.execute("select geoqs2geojson('public.world_rivers', 'name, featurecla')")
    # cursor.execute("select geoqs2geojson('public.world_testpoints', 'name, popularity')")
    # cursor.execute("select geoqs2geojson('public.world_uscities', 'name, pop2007')")
    row = cursor.fetchall()

    geojson = json.dumps(row)
    geojson = geojson[2:len(geojson)-2]

    cursor.close()

    return geojson


def getGJ(table_name, parameters):
    cursor = connection.cursor()

    qry = "select geoqs2geojson('" + table_name + "', '" + parameters + "')"
    print(qry)
    cursor.execute(qry)
    row = cursor.fetchall()

    geojson = json.dumps(row)
    geojson = geojson[2:len(geojson)-2]

    cursor.close()

    return geojson
