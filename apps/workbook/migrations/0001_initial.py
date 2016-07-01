# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Road',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=512, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
                ('dep', models.ForeignKey(verbose_name=b'\xd0\x94\xd0\xad\xd0\x9f', blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u0434\u043e\u0440\u043e\u0433\u0443',
                'verbose_name_plural': '\u0414\u043e\u0440\u043e\u0433\u0438',
            },
        ),
        migrations.CreateModel(
            name='Workbook',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file', models.FileField(upload_to=b'workbook/{dep}/%Y-%m-%d/', max_length=250, verbose_name=b'\xd0\xa4\xd0\xb0\xd0\xb9\xd0\xbb')),
                ('putdate', models.DateTimeField(auto_now_add=True, verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0')),
                ('dep', models.ForeignKey(related_name='dep_name', verbose_name=b'\xd0\x94\xd0\xad\xd0\x9f', to=settings.AUTH_USER_MODEL)),
                ('road', models.ForeignKey(related_name='road_name', verbose_name=b'\xd0\x94\xd0\xbe\xd1\x80\xd0\xbe\xd0\xb3\xd0\xb0', to='workbook.Road')),
            ],
            options={
                'ordering': ['-putdate'],
            },
        ),
    ]
