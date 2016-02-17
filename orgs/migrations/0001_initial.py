# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('icon', models.CharField(max_length=50)),
                ('catname', models.CharField(max_length=100)),
                ('org_id', models.IntegerField()),
                ('cat', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Org',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
                ('body', models.TextField(verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xba\xd1\x81\xd1\x82', blank=True)),
                ('address', models.CharField(max_length=200, verbose_name=b'\xd0\x90\xd0\xb4\xd1\x80\xd0\xb5\xd1\x81')),
                ('phone', models.CharField(max_length=100, verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xbb\xd0\xb5\xd1\x84\xd0\xbe\xd0\xbd\xd1\x8b', blank=True)),
                ('email', models.EmailField(max_length=100, verbose_name=b'E-mail', blank=True)),
                ('site', models.CharField(max_length=100, verbose_name=b'\xd0\xa1\xd0\xb0\xd0\xb9\xd1\x82', blank=True)),
                ('director', models.CharField(max_length=150, verbose_name=b'\xd0\xa0\xd1\x83\xd0\xba\xd0\xbe\xd0\xb2\xd0\xbe\xd0\xb4\xd0\xb8\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c')),
                ('cat', models.CharField(max_length=3, verbose_name=b'\xd0\xa2\xd0\xb8\xd0\xbf', choices=[(b'dep', b'\xd0\x94\xd0\xbe\xd1\x80\xd0\xbe\xd0\xb6\xd0\xbd\xd0\xbe-\xd1\x8d\xd0\xba\xd1\x81\xd0\xbf\xd0\xbb\xd1\x83\xd0\xb0\xd1\x82\xd0\xb0\xd1\x86\xd0\xb8\xd0\xbe\xd0\xbd\xd0\xbd\xd1\x8b\xd0\xb5 \xd0\xbf\xd1\x80\xd0\xb5\xd0\xb4\xd0\xbf\xd1\x80\xd0\xb8\xd1\x8f\xd1\x82\xd0\xb8\xd1\x8f'), (b'vne', b'\xd0\x92\xd0\xbd\xd0\xb5\xd1\x88\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xbf\xd0\xbe\xd0\xb4\xd1\x80\xd1\x8f\xd0\xb4\xd1\x87\xd0\xb8\xd0\xba\xd0\xb8'), (b'uch', b'\xd0\xa3\xd1\x87\xd1\x80\xd0\xb5\xd0\xb6\xd0\xb4\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f'), (b'ao', b'\xd0\x90\xd0\xba\xd1\x86\xd0\xb8\xd0\xbe\xd0\xbd\xd0\xb5\xd1\x80\xd0\xbd\xd1\x8b\xd0\xb5 \xd0\xbe\xd0\xb1\xd1\x89\xd0\xb5\xd1\x81\xd1\x82\xd0\xb2\xd0\xb0')])),
            ],
            options={
                'verbose_name': '\u043e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u044e',
                'verbose_name_plural': '\u041e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u0438',
            },
        ),
    ]
