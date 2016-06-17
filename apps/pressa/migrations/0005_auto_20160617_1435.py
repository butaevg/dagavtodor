# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('pressa', '0004_auto_20160513_1827'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='address',
            field=models.CharField(max_length=200, verbose_name=b'\xd0\x9f\xd0\xbe\xd1\x87\xd1\x82\xd0\xbe\xd0\xb2\xd1\x8b\xd0\xb9 \xd0\xb0\xd0\xb4\xd1\x80\xd0\xb5\xd1\x81 *', blank=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='name',
            field=models.CharField(max_length=100, verbose_name=b'\xd0\xa4\xd0\x98\xd0\x9e \xd0\xbf\xd0\xbe\xd0\xbb\xd0\xbd\xd0\xbe\xd1\x81\xd1\x82\xd1\x8c\xd1\x8e *'),
        ),
    ]
