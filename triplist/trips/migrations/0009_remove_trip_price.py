# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0008_auto_20170519_1625'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trip',
            name='price',
        ),
    ]
