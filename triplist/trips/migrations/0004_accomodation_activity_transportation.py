# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0003_auto_20170518_1903'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accomodation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=50)),
                ('city', models.ForeignKey(related_name='accomodation.city', to='trips.City')),
                ('country', models.ForeignKey(related_name='accomodation.country', to='trips.Country')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('city', models.ForeignKey(related_name='activity.city', to='trips.City')),
                ('country', models.ForeignKey(related_name='activity.country', to='trips.Country')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Transportation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
