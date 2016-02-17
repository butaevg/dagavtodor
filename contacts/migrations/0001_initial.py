# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=300, verbose_name=b'\xd0\x9e\xd1\x82\xd0\xb4\xd0\xb5\xd0\xbb')),
            ],
            options={
                'verbose_name': '\u043e\u0442\u0434\u0435\u043b',
                'verbose_name_plural': '\u041e\u0442\u0434\u0435\u043b\u044b',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('position', models.CharField(max_length=512, verbose_name=b'\xd0\x94\xd0\xbe\xd0\xbb\xd0\xb6\xd0\xbd\xd0\xbe\xd1\x81\xd1\x82\xd1\x8c')),
                ('name', models.CharField(max_length=512, verbose_name=b'\xd0\xa4\xd0\x98\xd0\x9e')),
                ('phone', models.CharField(max_length=256, verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xbb\xd0\xb5\xd1\x84\xd0\xbe\xd0\xbd')),
                ('dep', models.ForeignKey(related_name='dep', verbose_name=b'\xd0\x9e\xd1\x82\xd0\xb4\xd0\xb5\xd0\xbb', to='contacts.Department')),
            ],
            options={
                'verbose_name': '\u0421\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a',
                'verbose_name_plural': '\u0421\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0438',
            },
        ),
    ]
