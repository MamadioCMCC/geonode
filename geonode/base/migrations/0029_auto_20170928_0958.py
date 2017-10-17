# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0028_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resourcebase',
            name='hazard_unit',
            field=models.CharField(choices=[(b'1/0', 'inundated / not inundated'), (b'cm', 'centimeters'), (b'CTA', 'Consumption to Availability Ratio'), (b'dm', 'decimeters'), (b'hz', 'hertz, wave frequencies'), (b'kg', 'kilograms'), (b'kg/s', 'kilograms per second'), (b'km/h', 'kilometers per hour'), (b'kn', 'decimeters'), (b'm', 'meters'), (b'm/s', 'meters per second'), (b'mm', 'millimeters'), (b'MMI', 'Modified Mercalli Intensity'), (b'mph', 'Miles per hour'), (b'SA-g-dec', 'Spectral Acceleration (g)'), (b'PGA-g-dec', 'Peak Ground Acceleration (g)'), (b'PGA-g-per', 'Peak Ground Acceleration (%g)'), (b'PGA-cm/s^2', 'Peak Ground Acceleration (centimeter per second)'), (b'PGA-m/s^2', 'Peak Ground Acceleration (meter per second)'), (b'PGA-gal', 'Peak Ground Acceleration (gal: same as cm/s^2)'), (b'PGV-cm/s^2', 'Peak Ground Velocity'), (b'Q', 'Discharge (deficit)'), (b'VEI', 'Volcanic Explosivity Index'), (b'WCI', 'Water Crowding Index'), (b'WRSI', 'Water Requirement Satisfaction Index'), (b'PDSI', 'Palmer Drought Severity Index'), (b'PON', 'Percent of Normal'), (b'SPI', 'Standardized Precipitation Index'), (b'CMI', 'Crop Moisture Index'), (b'SWSI', 'Surface Water Supply Index'), (b'RDI', 'Reclamation Drought Index'), (b'LSI', 'Landslide Susceptibility Index'), (b'RDI', 'Reclamation Drought Index'), (b'VHL', 'Volcanic Hazard Level'), (b'THL', 'Tsunami Hazard Level'), (b'WA', 'Water Availability (aggregated runoff)'), (b'WBGT_C', 'Wet Bulb Globe Temperature (Celcius)'), (b'kW_m', 'Fire Line Intensity'), (b'FAI', 'Flooded Area Index'), (b'FWI', 'Canadian Fire Weather Index')], max_length=10, blank=True, help_text='The units of intensity specified in the hazard layer (e.g. metres, feet, PGA, m/s, index name)', null=True, verbose_name='intensity unit'),
        ),
    ]
