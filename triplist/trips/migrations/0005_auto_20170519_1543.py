# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0004_accomodation_activity_transportation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accomodation',
            name='country',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='country',
        ),
        migrations.AddField(
            model_name='transportation',
            name='end_city',
            field=models.ForeignKey(related_name='transportation.end_city', to='trips.City', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='transportation',
            name='start_city',
            field=models.ForeignKey(related_name='transportation.start_city', to='trips.City', null=True),
            preserve_default=True,
        ),
    ]
