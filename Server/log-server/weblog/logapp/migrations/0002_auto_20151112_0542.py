# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('logapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listhostname',
            name='listaction',
            field=models.CharField(max_length=100, default=datetime.datetime(2015, 11, 12, 5, 38, 27, 700747, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='logtable',
            name='logdatetime',
            field=models.DateTimeField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='logtable',
            name='logread',
            field=models.CharField(max_length=1, default=datetime.datetime(2015, 11, 12, 5, 42, 1, 547410, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
