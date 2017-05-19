# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0005_auto_20170519_1543'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='accomodation',
            field=models.ManyToManyField(to='trips.Accomodation'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='trip',
            name='activity',
            field=models.ManyToManyField(to='trips.Activity'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='trip',
            name='transporation',
            field=models.ManyToManyField(to='trips.Transportation'),
            preserve_default=True,
        ),
    ]
