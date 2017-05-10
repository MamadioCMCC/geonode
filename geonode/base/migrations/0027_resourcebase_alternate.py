# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0026_auto_20170510_0336'),
    ]

    operations = [
        migrations.AddField(
            model_name='resourcebase',
            name='alternate',
            field=models.CharField(max_length=128, null=True, blank=True),
        ),
    ]
