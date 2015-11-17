# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('logapp', '0006_auto_20151112_0618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logtable',
            name='logdatetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
