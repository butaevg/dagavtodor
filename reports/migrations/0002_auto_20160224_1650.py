# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='pic_1',
            field=models.ImageField(upload_to=b'machine', max_length=250, verbose_name=b'\xd0\xa4\xd0\xbe\xd1\x82\xd0\xbe\xd0\xb3\xd1\x80\xd0\xb0\xd1\x84\xd0\xb8\xd1\x8f'),
        ),
        migrations.AlterField(
            model_name='workimg',
            name='pic',
            field=models.ImageField(max_length=250, upload_to=b'work/%Y-%m-%d/'),
        ),
    ]
