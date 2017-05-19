# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0007_auto_20170519_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='accomodation',
            name='max_people',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='accomodation',
            name='price_diff',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='activity',
            name='max_people',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='activity',
            name='price_diff',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='transportation',
            name='max_people',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='transportation',
            name='price_diff',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
    ]
