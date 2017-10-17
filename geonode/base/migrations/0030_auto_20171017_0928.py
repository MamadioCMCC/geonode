# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0029_auto_20170928_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resourcebase',
            name='hazard_type',
            field=models.CharField(choices=[(b'earthquake', 'Earthquake'), (b'river_flood', 'River Flood'), (b'coastal_flood', 'Coastal Flood'), (b'urban_flood', 'Urban Flood'), (b'tsunami', 'Tsunami'), (b'strong_wind', 'Strong Wind'), (b'landslide', 'Landslide'), (b'drought', 'Drought'), (b'extreme_heat', 'Extreme Heat'), (b'wildfire', 'Wildfire'), (b'volcanic_ash', 'Volcanic Ash'), (b'water_scarcity', 'Water Scarcity')], max_length=50, blank=True, help_text='Choose the hazard type from a drop down menu.', null=True, verbose_name='hazard type'),
        ),
    ]
