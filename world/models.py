from django.contrib.gis.db import models


class WorldBorder(models.Model):
    # Regular Django fields corresponding to the attributes in the
    # world borders shapefile
    name = models.CharField(max_length=50)
    area = models.IntegerField()
    pop2005 = models.IntegerField('Population 2005')
    fips = models.CharField('FIPS Code', max_length=2)
    iso2 = models.CharField('2 DIGIT ISO', max_length=2)
    iso3 = models.CharField('3 DIGIT ISO', max_length=3)
    un = models.IntegerField('UN Code')
    region = models.IntegerField('Region code')
    subregion = models.IntegerField('Sub-region code')
    lon = models.FloatField('Longitude')
    lat = models.FloatField('Longitude')

    # GeoDjango specific: a geometry field (MultiPolygonField), and
    # overriding the default manager with a GeoManager instance.
    mpoly = models.MultiPolygonField(srid=4326)
    objects = models.GeoManager()

    # Returns the string representation of the model.
    def __str__(self):
        return self.name


class StatesBorder(models.Model):
    name = models.CharField(max_length=25)
    state_fips = models.CharField(max_length=2)
    sub_region = models.CharField(max_length=20)
    state_abbr = models.CharField(max_length=2)
    pop2010 = models.IntegerField()
    pop2012 = models.IntegerField()
    sqmi = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)
    objects = models.GeoManager()

    def __str__(self):
        return self.name


class USCities(models.Model):
    name = models.CharField(max_length=40)
    class_id = models.CharField(max_length=30)
    st = models.CharField(max_length=2)
    stfips = models.CharField(max_length=2)
    arealand = models.FloatField()
    areawater = models.FloatField()
    pop2000 = models.IntegerField()
    pop2007 = models.IntegerField()
    geom = models.PointField(srid=4326)
    objects = models.GeoManager()

    def __str__(self):
        return self.name


class Rivers(models.Model):
    scalerank = models.IntegerField()
    featurecla = models.CharField(max_length=32)
    name = models.CharField(max_length=254)
    name_alt = models.CharField(max_length=254)
    geom = models.LineStringField(srid=4326)
    objects = models.GeoManager()

    def __str__(self):
        return self.name


class TestPoints(models.Model):
    name = models.CharField(max_length=50)
    popularity = models.IntegerField()
    geom = models.PointField(srid=4326)
    objects = models.GeoManager()

    def __str__(self):
        return self.name
