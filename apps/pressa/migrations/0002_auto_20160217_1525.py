# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pressa', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='pic',
            field=models.ImageField(upload_to=b'articles/%Y-%m-%d/', max_length=250, verbose_name=b'\xd0\xa4\xd0\xbe\xd1\x82\xd0\xbe', blank=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='url',
            field=models.ImageField(upload_to=b'photo', max_length=250, verbose_name=b'\xd0\xa4\xd0\xbe\xd1\x82\xd0\xbe'),
        ),
        migrations.AlterField(
            model_name='post',
            name='mainpic',
            field=models.ImageField(upload_to=b'news/%Y-%m-%d/', max_length=250, verbose_name=b'\xd0\x9a\xd0\xb0\xd1\x80\xd1\x82\xd0\xb8\xd0\xbd\xd0\xba\xd0\xb0 \xd0\xbd\xd0\xb0 \xd0\xb3\xd0\xbb\xd0\xb0\xd0\xb2\xd0\xbd\xd0\xbe\xd0\xb9'),
        ),
        migrations.AlterField(
            model_name='postimg',
            name='pic',
            field=models.ImageField(upload_to=b'news/%Y-%m-%d/', max_length=250, verbose_name=b'\xd0\xa4\xd0\xbe\xd1\x82\xd0\xbe\xd0\xb3\xd1\x80\xd0\xb0\xd1\x84\xd0\xb8\xd0\xb8 \xd0\xba \xd0\xbd\xd0\xbe\xd0\xb2\xd0\xbe\xd1\x81\xd1\x82\xd0\xb8'),
        ),
        migrations.AlterField(
            model_name='question',
            name='img',
            field=models.ImageField(upload_to=b'faq/%Y-%m-%d/', verbose_name=b'\xd0\x9f\xd1\x80\xd0\xb8\xd0\xbb\xd0\xb0\xd0\xb3\xd0\xb0\xd0\xb5\xd0\xbco\xd0\xb5 \xd1\x84\xd0\xbe\xd1\x82\xd0\xbe', blank=True),
        ),
    ]
