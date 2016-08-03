# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orgs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dep',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('info', models.TextField(verbose_name=b'Kontakty', blank=True)),
                ('dep_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DepDoc',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=512, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
                ('url', models.FileField(upload_to=b'deps', max_length=250, verbose_name=b'\xd0\xa4\xd0\xb0\xd0\xb9\xd0\xbb')),
                ('dep_id', models.IntegerField()),
            ],
        ),
    ]
