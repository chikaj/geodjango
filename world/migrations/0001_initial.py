# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rivers',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('scalerank', models.IntegerField()),
                ('featurecla', models.CharField(max_length=32)),
                ('name', models.CharField(max_length=254)),
                ('name_alt', models.CharField(max_length=254)),
                ('geom', django.contrib.gis.db.models.fields.LineStringField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='StatesBorder',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=25)),
                ('state_fips', models.CharField(max_length=2)),
                ('sub_region', models.CharField(max_length=20)),
                ('state_abbr', models.CharField(max_length=2)),
                ('pop2010', models.IntegerField()),
                ('pop2012', models.IntegerField()),
                ('sqmi', models.FloatField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='USCities',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=40)),
                ('class_id', models.CharField(max_length=30)),
                ('st', models.CharField(max_length=2)),
                ('stfips', models.CharField(max_length=2)),
                ('arealand', models.FloatField()),
                ('areawater', models.FloatField()),
                ('pop2000', models.IntegerField()),
                ('pop2007', models.IntegerField()),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='WorldBorder',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('area', models.IntegerField()),
                ('pop2005', models.IntegerField(verbose_name='Population 2005')),
                ('fips', models.CharField(max_length=2, verbose_name='FIPS Code')),
                ('iso2', models.CharField(max_length=2, verbose_name='2 DIGIT ISO')),
                ('iso3', models.CharField(max_length=3, verbose_name='3 DIGIT ISO')),
                ('un', models.IntegerField(verbose_name='UN Code')),
                ('region', models.IntegerField(verbose_name='Region code')),
                ('subregion', models.IntegerField(verbose_name='Sub-region code')),
                ('lon', models.FloatField(verbose_name='Longitude')),
                ('lat', models.FloatField(verbose_name='Longitude')),
                ('mpoly', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
    ]
