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
            name='Insta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('insta_id', models.CharField(max_length=15, verbose_name=b'User ID')),
                ('dep', models.ForeignKey(related_name='rayon', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['dep'],
            },
        ),
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=512, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb8\xd0\xbc\xd0\xb5\xd0\xbd\xd0\xbe\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd1\x82\xd0\xb5\xd1\x85\xd0\xbd\xd0\xb8\xd0\xba\xd0\xb8')),
                ('body', models.TextField(verbose_name=b'\xd0\x9e\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5', blank=True)),
                ('year_issue', models.CharField(max_length=5, verbose_name=b'\xd0\x93\xd0\xbe\xd0\xb4 \xd0\xb2\xd1\x8b\xd0\xbf\xd1\x83\xd1\x81\xd0\xba\xd0\xb0')),
                ('pic_1', models.ImageField(upload_to=b'upload/machine', max_length=250, verbose_name=b'\xd0\xa4\xd0\xbe\xd1\x82\xd0\xbe\xd0\xb3\xd1\x80\xd0\xb0\xd1\x84\xd0\xb8\xd1\x8f')),
                ('putdate', models.DateTimeField(auto_now_add=True)),
                ('dep', models.ForeignKey(related_name='oao', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-putdate'],
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=512, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
                ('body', models.TextField(verbose_name=b'\xd0\x9e\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
                ('putdate', models.DateField(verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0')),
                ('expiredate', models.DateField(verbose_name=b'\xd0\xa1\xd1\x80\xd0\xbe\xd0\xba')),
                ('hide', models.BooleanField(default=False)),
                ('members', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name=b'\xd0\x98\xd1\x81\xd0\xbf\xd0\xbe\xd0\xbb\xd0\xbd\xd0\xb8\xd1\x82\xd0\xb5\xd0\xbb\xd0\xb8')),
            ],
            options={
                'ordering': ['-putdate'],
                'verbose_name': '\u043f\u043e\u0440\u0443\u0447\u0435\u043d\u0438\u0435',
                'verbose_name_plural': '\u041f\u043e\u0440\u0443\u0447\u0435\u043d\u0438\u044f',
            },
        ),
        migrations.CreateModel(
            name='OrderExec',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('process', models.TextField(verbose_name=b'\xd0\xa7\xd1\x82\xd0\xbe \xd1\x81\xd0\xb4\xd0\xb5\xd0\xbb\xd0\xb0\xd0\xbd\xd0\xbe')),
                ('process_perc', models.IntegerField(verbose_name=b'\xd0\x9f\xd1\x80\xd0\xbe\xd1\x86\xd0\xb5\xd0\xbd\xd1\x82')),
                ('putdate', models.DateField(auto_now_add=True)),
                ('order_id', models.IntegerField()),
                ('member', models.ForeignKey(related_name='member', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Psd',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=512, verbose_name=b'\xd0\x9e\xd0\xb1\xd1\x8a\xd0\xb5\xd0\xba\xd1\x82')),
                ('price', models.FloatField(verbose_name=b'\xd0\xa1\xd1\x82\xd0\xbe\xd0\xb8\xd0\xbc\xd0\xbe\xd1\x81\xd1\x82\xd1\x8c')),
                ('contractor', models.CharField(max_length=4, verbose_name=b'\xd0\x9f\xd1\x80\xd0\xbe\xd0\xb5\xd0\xba\xd1\x82\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd1\x89\xd0\xb8\xd0\xba', choices=[(b'121', b'\xd0\x98\xd0\x9f\xd0\xa2\xd0\xa1 \xd0\xa2\xd1\x80\xd0\xb0\xd0\xbd\xd1\x81\xd0\xbf\xd1\x80\xd0\xbe\xd0\xb5\xd0\xba\xd1\x82'), (b'123', b'\xd0\x9e\xd0\x9e\xd0\x9e \xc2\xab\xd0\xad\xd0\xba\xd0\xbe\xd0\xb4\xd0\xbe\xd1\x80\xc2\xbb'), (b'124', b'\xd0\x97\xd0\x90\xd0\x9e \xc2\xab\xd0\x94\xd0\xb0\xd0\xb3\xd0\xb4\xd0\xbe\xd1\x80\xd0\xbf\xd1\x80\xd0\xbe\xd0\xb5\xd0\xba\xd1\x82\xc2\xbb'), (b'125', b'\xd0\x9e\xd0\x9e\xd0\x9e \xc2\xab\xd0\x94\xd0\xbe\xd1\x80\xd1\x81\xd1\x82\xd1\x80\xd0\xbe\xd0\xb9\xd0\xbf\xd1\x80\xd0\xbe\xd0\xb5\xd0\xba\xd1\x82\xc2\xbb')])),
                ('exe', models.FloatField(verbose_name=b'\xd0\x92\xd1\x8b\xd0\xbf\xd0\xbe\xd0\xbb\xd0\xbd\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5', blank=True)),
                ('exe_perc', models.IntegerField(default=0, verbose_name=b'\xd0\x92\xd1\x8b\xd0\xbf\xd0\xbe\xd0\xbb\xd0\xbd\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5, %', blank=True)),
                ('getsum', models.FloatField(verbose_name=b'\xd0\x9f\xd0\xbe\xd0\xbb\xd1\x83\xd1\x87\xd0\xb5\xd0\xbd\xd0\xbe', blank=True)),
                ('exe_getsum', models.IntegerField(default=0, verbose_name=b'\xd0\x9f\xd0\xbe\xd0\xbb\xd1\x83\xd1\x87\xd0\xb5\xd0\xbd\xd0\xbe, %', blank=True)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': '\u041f\u0421\u0414',
                'verbose_name_plural': '\u041f\u0421\u0414',
            },
        ),
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('putdate', models.DateTimeField(auto_now_add=True)),
                ('sost', models.CharField(max_length=50)),
                ('temp', models.CharField(max_length=10)),
                ('pr_r', models.CharField(max_length=100)),
                ('pr_m', models.CharField(max_length=100)),
                ('works', models.TextField(blank=True)),
                ('rayon', models.ForeignKey(related_name='org', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-putdate'],
            },
        ),
        migrations.CreateModel(
            name='WeatherCurrent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('putdate', models.DateTimeField(auto_now=True)),
                ('sost', models.CharField(max_length=50)),
                ('temp', models.CharField(max_length=10)),
                ('pr_r', models.CharField(max_length=100)),
                ('pr_m', models.CharField(max_length=100)),
                ('works', models.TextField(blank=True)),
                ('rayon', models.ForeignKey(related_name='dep', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cont', models.IntegerField()),
                ('road', models.IntegerField()),
                ('works', models.TextField()),
                ('tech', models.TextField(blank=True)),
                ('pers', models.CharField(max_length=100, blank=True)),
                ('putdate', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-putdate'],
            },
        ),
        migrations.CreateModel(
            name='WorkImg',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pic', models.ImageField(max_length=250, upload_to=b'upload/work')),
                ('work', models.ForeignKey(related_name='pics', to='reports.Work')),
            ],
        ),
    ]
