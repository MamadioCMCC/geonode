# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0025_auto_20170510_0255'),
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
