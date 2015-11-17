# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('logapp', '0005_auto_20151112_0603'),
    ]

    operations = [
        migrations.CreateModel(
            name='blacklist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blackip', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='logtable',
            name='logdatetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 12, 6, 18, 54, 159292, tzinfo=utc)),
        ),
    ]
