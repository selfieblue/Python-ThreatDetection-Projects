# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('logapp', '0004_auto_20151112_0557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logtable',
            name='logdatetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 12, 6, 3, 24, 287361, tzinfo=utc)),
        ),
    ]
