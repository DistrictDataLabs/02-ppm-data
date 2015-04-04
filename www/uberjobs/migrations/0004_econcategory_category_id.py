# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uberjobs', '0003_auto_20150329_1936'),
    ]

    operations = [
        migrations.AddField(
            model_name='econcategory',
            name='category_id',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
    ]
