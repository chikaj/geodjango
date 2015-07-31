from django.shortcuts import render
from django.http import HttpResponse
from .models import WorldBorder, StatesBorder
from .customsql import getGeoJSON, getGJ
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


# def updateGeoLocation(request):
#     if request.method == 'POST':
#         if 'geoLocation' in request.POST:
#             geoLocation = request.POST['geoLocation']
#             # update table with this new geoLocation
#             return HttpResponse('Successfully updated geoLocation!')

#     return HttpResponse('Oops. Something went wrong updateing geoLocation')
