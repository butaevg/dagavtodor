# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pressa', '0002_auto_20160217_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advert',
            name='putdate',
            field=models.DateTimeField(verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0'),
        ),
    ]
