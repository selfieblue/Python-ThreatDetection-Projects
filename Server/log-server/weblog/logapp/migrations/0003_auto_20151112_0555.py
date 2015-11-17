# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logapp', '0002_auto_20151112_0542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logtable',
            name='logdatetime',
            field=models.DateTimeField(default=False),
        ),
    ]
