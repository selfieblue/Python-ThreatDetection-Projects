# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('logapp', '0009_auto_20151113_0612'),
    ]

    operations = [
        migrations.AddField(
            model_name='logtable',
            name='logaction',
            field=models.CharField(max_length=100, default=datetime.datetime(2015, 11, 13, 11, 4, 42, 977704, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='logtable',
            name='logrole',
            field=models.CharField(max_length=50, default=datetime.datetime(2015, 11, 13, 11, 4, 57, 605543, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='logtable',
            name='logdetail',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='logtable',
            name='logread',
            field=models.CharField(max_length=1),
        ),
    ]
