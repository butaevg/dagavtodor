# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pressa', '0003_auto_20160513_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advert',
            name='putdate',
            field=models.DateField(verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0'),
        ),
        migrations.AlterField(
            model_name='post',
            name='putdate',
            field=models.DateTimeField(verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0'),
        ),
    ]
