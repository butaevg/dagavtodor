# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0002_auto_20160224_1650'),
    ]

    operations = [
        migrations.AddField(
            model_name='machine',
            name='pic_2',
            field=models.ImageField(upload_to=b'machine', verbose_name=b'\xd0\xa4\xd0\xbe\xd1\x82\xd0\xbe\xd0\xb3\xd1\x80\xd0\xb0\xd1\x84\xd0\xb8\xd1\x8f', blank=True),
        ),
        migrations.AddField(
            model_name='machine',
            name='pic_3',
            field=models.ImageField(upload_to=b'machine', verbose_name=b'\xd0\xa4\xd0\xbe\xd1\x82\xd0\xbe\xd0\xb3\xd1\x80\xd0\xb0\xd1\x84\xd0\xb8\xd1\x8f', blank=True),
        ),
        migrations.AlterField(
            model_name='machine',
            name='pic_1',
            field=models.ImageField(upload_to=b'machine', verbose_name=b'\xd0\xa4\xd0\xbe\xd1\x82\xd0\xbe\xd0\xb3\xd1\x80\xd0\xb0\xd1\x84\xd0\xb8\xd1\x8f'),
        ),
    ]
