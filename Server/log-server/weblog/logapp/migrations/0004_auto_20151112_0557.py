# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('logapp', '0003_auto_20151112_0555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logtable',
            name='logdatetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 12, 5, 57, 19, 100896, tzinfo=utc)),
        ),
    ]
