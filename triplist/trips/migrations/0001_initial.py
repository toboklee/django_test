# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('longitude', models.DecimalField(max_digits=9, decimal_places=6)),
                ('latitude', models.DecimalField(max_digits=9, decimal_places=6)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('longitude', models.DecimalField(max_digits=9, decimal_places=6)),
                ('latitude', models.DecimalField(max_digits=9, decimal_places=6)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('max_people', models.IntegerField(default=1)),
                ('trip_start_at', models.DateTimeField(auto_now_add=True, verbose_name=b'StartAt')),
                ('trip_end_at', models.DateTimeField(auto_now_add=True, verbose_name=b'EndAt')),
                ('price', models.CharField(max_length=15)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name=b'CreatedAt')),
                ('last_modified_at', models.DateTimeField(auto_now_add=True, verbose_name=b'ModifiedAt')),
                ('destination', models.ManyToManyField(to='trips.Country')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(related_name='country', to='trips.Country'),
            preserve_default=True,
        ),
    ]
