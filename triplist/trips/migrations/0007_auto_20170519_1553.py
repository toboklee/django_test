# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0006_auto_20170519_1547'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trip',
            old_name='transporation',
            new_name='transportation',
        ),
    ]
