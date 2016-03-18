# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roads', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camip',
            name='img',
            field=models.ImageField(upload_to=b'webcam', verbose_name=b'\xd0\x9a\xd0\xb0\xd1\x80\xd1\x82\xd0\xb8\xd0\xbd\xd0\xba\xd0\xb0'),
        ),
        migrations.AlterField(
            model_name='map',
            name='map_rayon',
            field=models.ImageField(upload_to=b'maps', verbose_name=b'\xd0\x9a\xd0\xb0\xd1\x80\xd1\x82\xd0\xb0', blank=True),
        ),
        migrations.AlterField(
            model_name='reportimg',
            name='url',
            field=models.ImageField(upload_to=b'roads/%Y-%m-%d/', max_length=250, verbose_name=b'\xd0\xa4\xd0\xbe\xd1\x82\xd0\xbe'),
        ),
        migrations.AlterField(
            model_name='road',
            name='pic',
            field=models.ImageField(upload_to=b'roads', max_length=250, verbose_name=b'\xd0\x9a\xd0\xb0\xd1\x80\xd1\x82\xd0\xb0-\xd1\x81\xd1\x85\xd0\xb5\xd0\xbc\xd0\xb0', blank=True),
        ),
    ]
