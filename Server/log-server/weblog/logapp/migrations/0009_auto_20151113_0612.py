# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logapp', '0008_delete_blacklist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logtable',
            name='logdetail',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='logtable',
            name='logread',
            field=models.CharField(max_length=2),
        ),
    ]
