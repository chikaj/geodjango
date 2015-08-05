from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import WorldBorder, StatesBorder, TestPoints
from .customsql import getGeoJSON, getGJ
import json
from django.contrib.gis.geos import Point
# import json


def index(request):
    # my_tab = "'public.world_statesborder'"
    # params = "'id, name, pop2012'"
    states = getGeoJSON()
    rivers = getGJ('public.world_rivers', 'name, featurecla')
    cities = getGJ('public.world_uscities', 'name, pop2007')

    return render(request, 'world/index.html', {'states': states,
        'rivers': rivers, 'cities': cities})


def states(request):
    qs = StatesBorder.objects.all().geojson()
    return render(request, 'world/index.html', {'borders': qs})


def updateGeoLocation(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        if 'geoLocation' in body:
            geoLocation = body['geoLocation']
            # update table with this new geoLocation
            point = TestPoints(name="test", popularity=0, geom=Point(geoLocation[0], geoLocation[1]))
            point.save()
            return JsonResponse({'id': point.id})

    return HttpResponse('Oops. Something went wrong updating geoLocation', status=500)
