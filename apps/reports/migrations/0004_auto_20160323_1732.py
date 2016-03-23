# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reports', '0003_auto_20160314_1636'),
    ]

    operations = [
        migrations.CreateModel(
            name='MachineWorking',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=512, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb8\xd0\xbc\xd0\xb5\xd0\xbd\xd0\xbe\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd1\x82\xd0\xb5\xd1\x85\xd0\xbd\xd0\xb8\xd0\xba\xd0\xb8')),
                ('body', models.TextField(verbose_name=b'\xd0\x9e\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5', blank=True)),
                ('year_issue', models.CharField(max_length=5, verbose_name=b'\xd0\x93\xd0\xbe\xd0\xb4 \xd0\xb2\xd1\x8b\xd0\xbf\xd1\x83\xd1\x81\xd0\xba\xd0\xb0')),
                ('pic_1', models.ImageField(upload_to=b'machine', verbose_name=b'\xd0\xa4\xd0\xbe\xd1\x82\xd0\xbe 1')),
                ('pic_2', models.ImageField(upload_to=b'machine', verbose_name=b'\xd0\xa4\xd0\xbe\xd1\x82\xd0\xbe 2', blank=True)),
                ('pic_3', models.ImageField(upload_to=b'machine', verbose_name=b'\xd0\xa4\xd0\xbe\xd1\x82\xd0\xbe 3', blank=True)),
                ('pic_4', models.ImageField(upload_to=b'machine', verbose_name=b'\xd0\xa4\xd0\xbe\xd1\x82\xd0\xbe 4', blank=True)),
                ('pic_5', models.ImageField(upload_to=b'machine', verbose_name=b'\xd0\xa4\xd0\xbe\xd1\x82\xd0\xbe 5', blank=True)),
                ('dep', models.ForeignKey(related_name='oaod', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['dep'],
            },
        ),
        migrations.AlterModelOptions(
            name='machine',
            options={'ordering': ['dep']},
        ),
        migrations.AddField(
            model_name='machine',
            name='pic_4',
            field=models.ImageField(upload_to=b'machine', verbose_name=b'\xd0\xa4\xd0\xbe\xd1\x82\xd0\xbe 4', blank=True),
        ),
        migrations.AddField(
            model_name='machine',
            name='pic_5',
            field=models.ImageField(upload_to=b'machine', verbose_name=b'\xd0\xa4\xd0\xbe\xd1\x82\xd0\xbe 5', blank=True),
        ),
        migrations.AlterField(
            model_name='machine',
            name='pic_1',
            field=models.ImageField(upload_to=b'machine', verbose_name=b'\xd0\xa4\xd0\xbe\xd1\x82\xd0\xbe 1'),
        ),
        migrations.AlterField(
            model_name='machine',
            name='pic_2',
            field=models.ImageField(upload_to=b'machine', verbose_name=b'\xd0\xa4\xd0\xbe\xd1\x82\xd0\xbe 2', blank=True),
        ),
        migrations.AlterField(
            model_name='machine',
            name='pic_3',
            field=models.ImageField(upload_to=b'machine', verbose_name=b'\xd0\xa4\xd0\xbe\xd1\x82\xd0\xbe 3', blank=True),
        ),
    ]
