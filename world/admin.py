from django.contrib.gis import admin
from world.models import WorldBorder, StatesBorder, USCities, Rivers, TestPoints

admin.site.register(WorldBorder, admin.OSMGeoAdmin)
admin.site.register(StatesBorder, admin.OSMGeoAdmin)
admin.site.register(USCities, admin.OSMGeoAdmin)
admin.site.register(Rivers, admin.OSMGeoAdmin)
admin.site.register(TestPoints, admin.OSMGeoAdmin)
