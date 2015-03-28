# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EconCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category_name', models.CharField(max_length=200)),
                ('category_desc', models.CharField(max_length=1000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EconSeries',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('series_name', models.CharField(max_length=200)),
                ('series_id', models.CharField(max_length=20)),
                ('series_start_date', models.DateField()),
                ('series_end_date', models.DateField()),
                ('econ_category', models.ForeignKey(to='uberjobs.EconCategory')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SeriesItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item_year', models.CharField(max_length=4)),
                ('item_period', models.CharField(max_length=3)),
                ('item_value', models.DecimalField(max_digits=12, decimal_places=4)),
                ('item_normalized_value', models.DecimalField(max_digits=12, decimal_places=4)),
                ('series', models.ForeignKey(to='uberjobs.EconSeries')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
