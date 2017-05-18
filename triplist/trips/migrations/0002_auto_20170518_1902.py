# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='country',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='country',
            name='longitude',
        ),
        migrations.AlterField(
            model_name='trip',
            name='trip_end_at',
            field=models.DateTimeField(verbose_name=b'EndAt'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='trip',
            name='trip_start_at',
            field=models.DateTimeField(verbose_name=b'StartAt'),
            preserve_default=True,
        ),
    ]
