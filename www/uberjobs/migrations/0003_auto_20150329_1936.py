# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('uberjobs', '0002_auto_20150328_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='econseries',
            name='series_end_date',
            field=models.DateField(default=datetime.date(2015, 1, 1)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='econseries',
            name='series_start_date',
            field=models.DateField(default=datetime.date(2004, 1, 1)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='seriesitem',
            name='item_normalized_value',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='seriesitem',
            name='item_value',
            field=models.FloatField(),
            preserve_default=True,
        ),
    ]
