# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='listhostname',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('listhost', models.CharField(max_length=50)),
                ('listip', models.CharField(max_length=50)),
                ('listagent', models.CharField(max_length=20)),
                ('liststatus', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='logtable',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('logserver', models.CharField(max_length=50)),
                ('logtype', models.CharField(max_length=50)),
                ('loglevel', models.CharField(max_length=50)),
                ('logdetail', models.CharField(max_length=500)),
            ],
        ),
    ]
