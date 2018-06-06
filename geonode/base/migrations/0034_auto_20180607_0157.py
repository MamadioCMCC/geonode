# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0033_auto_20180330_0951'),
    ]

    operations = [
        migrations.AddField(
            model_name='resourcebase',
            name='calculation_method_quality',
            field=models.DecimalField(null=True, max_digits=3, decimal_places=2),
        ),
        migrations.AddField(
            model_name='resourcebase',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime.now, help_text='reference date for the cited resource', null=True, verbose_name='creation date', blank=True),
        ),
        migrations.AddField(
            model_name='resourcebase',
            name='data_update_date',
            field=models.DateTimeField(default=datetime.datetime.now, help_text='reference date for the cited resource', null=True, verbose_name='data update date', blank=True),
        ),
        migrations.AddField(
            model_name='resourcebase',
            name='download_url',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='resourcebase',
            name='hazard_glide',
            field=models.CharField(help_text='ID associated with hazard event; only to keep historic layers', max_length=255, null=True, verbose_name='glide number', blank=True),
        ),
        migrations.AddField(
            model_name='resourcebase',
            name='hazard_period',
            field=models.CharField(help_text='The return period of the layer (in years)', max_length=10, null=True, verbose_name='return period', blank=True),
        ),
        migrations.AddField(
            model_name='resourcebase',
            name='hazard_set',
            field=models.CharField(help_text='This ID will link the three associated layers for each hazard dataset so that the analytical framework knows to reference these three layers in the same query.', max_length=255, null=True, verbose_name='hazard set id', blank=True),
        ),
        migrations.AddField(
            model_name='resourcebase',
            name='hazard_type',
            field=models.CharField(choices=[(b'earthquake', 'Earthquake'), (b'river_flood', 'River Flood'), (b'coastal_flood', 'Coastal Flood'), (b'urban_flood', 'Urban Flood'), (b'tsunami', 'Tsunami'), (b'strong_wind', 'Strong Wind'), (b'landslide', 'Landslide'), (b'drought', 'Drought'), (b'extreme_heat', 'Extreme Heat'), (b'wildfire', 'Wildfire'), (b'volcanic_ash', 'Volcanic Ash'), (b'water_scarcity', 'Water Scarcity')], max_length=50, blank=True, help_text='Choose the hazard type from a drop down menu.', null=True, verbose_name='hazard type'),
        ),
        migrations.AddField(
            model_name='resourcebase',
            name='hazard_unit',
            field=models.CharField(choices=[(b'1/0', 'inundated / not inundated'), (b'cm', 'centimeters'), (b'CTA', 'Consumption to Availability Ratio'), (b'dm', 'decimeters'), (b'hz', 'hertz, wave frequencies'), (b'kg', 'kilograms'), (b'kg/s', 'kilograms per second'), (b'km/h', 'kilometers per hour'), (b'kn', 'decimeters'), (b'm', 'meters'), (b'm/s', 'meters per second'), (b'mm', 'millimeters'), (b'MMI', 'Modified Mercalli Intensity'), (b'mph', 'Miles per hour'), (b'SA-g-dec', 'Spectral Acceleration (g)'), (b'PGA-g-dec', 'Peak Ground Acceleration (g)'), (b'PGA-g-per', 'Peak Ground Acceleration (%g)'), (b'PGA-cm/s^2', 'Peak Ground Acceleration (centimeter per second)'), (b'PGA-m/s^2', 'Peak Ground Acceleration (meter per second)'), (b'PGA-gal', 'Peak Ground Acceleration (gal: same as cm/s^2)'), (b'PGV-cm/s^2', 'Peak Ground Velocity'), (b'Q', 'Discharge (deficit)'), (b'VEI', 'Volcanic Explosivity Index'), (b'WCI', 'Water Crowding Index'), (b'WRSI', 'Water Requirement Satisfaction Index'), (b'PDSI', 'Palmer Drought Severity Index'), (b'PON', 'Percent of Normal'), (b'SPI', 'Standardized Precipitation Index'), (b'CMI', 'Crop Moisture Index'), (b'SWSI', 'Surface Water Supply Index'), (b'RDI', 'Reclamation Drought Index'), (b'LSI', 'Landslide Susceptibility Index'), (b'RDI', 'Reclamation Drought Index'), (b'VHL', 'Volcanic Hazard Level'), (b'THL', 'Tsunami Hazard Level'), (b'WA', 'Water Availability (aggregated runoff)'), (b'WBGT_C', 'Wet Bulb Globe Temperature (Celcius)'), (b'kW_m', 'Fire Line Intensity'), (b'FAI', 'Flooded Area Index'), (b'FWI', 'Canadian Fire Weather Index')], max_length=10, blank=True, help_text='The units of intensity specified in the hazard layer (e.g. metres, feet, PGA, m/s, index name)', null=True, verbose_name='intensity unit'),
        ),
        migrations.AddField(
            model_name='resourcebase',
            name='metadata_update_date',
            field=models.DateTimeField(auto_now=True, help_text='reference date for the cited resource', null=True, verbose_name='metadata update date'),
        ),
        migrations.AddField(
            model_name='resourcebase',
            name='publication_date',
            field=models.DateTimeField(auto_now_add=True, help_text='reference date for the cited resource', null=True, verbose_name='publication date'),
        ),
        migrations.AddField(
            model_name='resourcebase',
            name='scientific_quality',
            field=models.DecimalField(null=True, max_digits=3, decimal_places=2),
        ),
    ]
