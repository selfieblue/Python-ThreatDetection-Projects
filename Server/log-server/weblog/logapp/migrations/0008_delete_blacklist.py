# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logapp', '0007_auto_20151112_0626'),
    ]

    operations = [
        migrations.DeleteModel(
            name='blacklist',
        ),
    ]
