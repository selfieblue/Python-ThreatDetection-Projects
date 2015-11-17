# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('logapp', '0010_auto_20151113_1104'),
    ]

    operations = [
        migrations.CreateModel(
            name='checktable',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('serverrole', models.CharField(max_length=50)),
                ('lastquery', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
