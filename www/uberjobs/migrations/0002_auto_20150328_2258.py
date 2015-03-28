# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('uberjobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='econseries',
            name='series_end_date',
            field=models.DateField(default=datetime.date.today),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='econseries',
            name='series_start_date',
            field=models.DateField(default=datetime.date.today),
            preserve_default=True,
        ),
    ]
