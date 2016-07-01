# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('workbook', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workbook',
            name='putdate',
            field=models.DateField(default=datetime.datetime.now, verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0'),
        ),
    ]
