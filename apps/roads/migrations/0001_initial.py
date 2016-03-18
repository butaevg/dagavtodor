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
            name='Cam3g',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=300, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
                ('folder', models.CharField(max_length=100, verbose_name=b'\xd0\x9a\xd0\xb0\xd1\x82\xd0\xb0\xd0\xbb\xd0\xbe\xd0\xb3')),
                ('ip', models.CharField(max_length=50, verbose_name=b'IP-\xd0\xb0\xd0\xb4\xd1\x80\xd0\xb5\xd1\x81', blank=True)),
                ('hide', models.BooleanField(default=False, verbose_name=b'\xd0\xa1\xd0\xba\xd1\x80\xd1\x8b\xd1\x82\xd1\x8c')),
            ],
            options={
                'verbose_name': '3g-\u043a\u0430\u043c\u0435\u0440\u0443',
                'verbose_name_plural': '3g-\u043a\u0430\u043c\u0435\u0440\u044b',
            },
        ),
        migrations.CreateModel(
            name='CamIp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=300, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
                ('html', models.TextField(verbose_name=b'HTML-\xd0\xba\xd0\xbe\xd0\xb4')),
                ('img', models.ImageField(upload_to=b'upload/webcam', verbose_name=b'\xd0\x9a\xd0\xb0\xd1\x80\xd1\x82\xd0\xb8\xd0\xbd\xd0\xba\xd0\xb0')),
                ('ip', models.CharField(max_length=50, verbose_name=b'IP-\xd0\xb0\xd0\xb4\xd1\x80\xd0\xb5\xd1\x81', blank=True)),
                ('hide', models.BooleanField(default=False, verbose_name=b'\xd0\xa1\xd0\xba\xd1\x80\xd1\x8b\xd1\x82\xd1\x8c')),
            ],
            options={
                'verbose_name': 'ip-\u043a\u0430\u043c\u0435\u0440\u0443',
                'verbose_name_plural': 'ip-\u043a\u0430\u043c\u0435\u0440\u044b',
            },
        ),
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rayon', models.CharField(max_length=100, verbose_name=b'\xd0\xa0\xd0\xb0\xd0\xb9\xd0\xbe\xd0\xbd')),
                ('plos', models.CharField(max_length=20, verbose_name=b'\xd0\x9f\xd0\xbb\xd0\xbe\xd1\x89\xd0\xb0\xd0\xb4\xd1\x8c')),
                ('nal_dor_obs', models.CharField(max_length=20, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xbb\xd0\xb8\xd1\x87\xd0\xb8\xd0\xb5 \xd0\xb4\xd0\xbe\xd1\x80\xd0\xbe\xd0\xb3 \xd0\xbd\xd0\xb0 \xd1\x82\xd1\x8b\xd1\x81. \xd0\xba\xd0\xbc.')),
                ('selo', models.CharField(max_length=20, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xbb\xd0\xb8\xd1\x87\xd0\xb8\xd0\xb5 \xd1\x81\xd0\xb5\xd0\xbb')),
                ('selo_bezd', models.CharField(max_length=20, verbose_name=b'\xd0\xb2 \xd1\x82.\xd1\x87. \xd1\x81 \xd0\xb1\xd0\xb5\xd0\xb7\xd0\xb4\xd0\xbe\xd1\x80. \xd0\xbf\xd0\xbe\xd0\xba\xd1\x80\xd1\x8b\xd1\x82\xd0\xb8\xd0\xb5\xd0\xbc')),
                ('prot_obs', models.CharField(max_length=20, verbose_name=b'\xd0\x9f\xd1\x80\xd0\xbe\xd1\x82\xd1\x8f\xd0\xb6\xd0\xb5\xd0\xbd\xd0\xbd\xd0\xbe\xd1\x81\xd1\x82\xd1\x8c \xd0\xb4\xd0\xbe\xd1\x80\xd0\xbe\xd0\xb3')),
                ('res_dor', models.CharField(max_length=20, verbose_name=b'\xd0\xa0\xd0\xb5\xd1\x81\xd0\xbf\xd1\x83\xd0\xb1\xd0\xbb\xd0\xb8\xd0\xba\xd0\xb0\xd0\xbd\xd1\x81\xd0\xba\xd0\xb8\xd0\xb5')),
                ('mest_dor', models.CharField(max_length=20, verbose_name=b'\xd0\x9c\xd0\xb5\xd1\x81\xd1\x82\xd0\xbd\xd1\x8b\xd0\xb5')),
                ('res_dor_asf', models.CharField(max_length=20, verbose_name=b'\xd0\xa0\xd0\xb5\xd1\x81\xd0\xbf\xd1\x83\xd0\xb1\xd0\xbb\xd0\xb8\xd0\xba\xd0\xb0\xd0\xbd\xd1\x81\xd0\xba\xd0\xb8\xd0\xb5 - \xd0\xb0\xd1\x81\xd1\x84\xd0\xb0\xd0\xbb\xd1\x8c\xd1\x82')),
                ('mest_dor_asf', models.CharField(max_length=20, verbose_name=b'\xd0\x9c\xd0\xb5\xd1\x81\xd1\x82\xd0\xbd\xd1\x8b\xd0\xb5 - \xd0\xb0\xd1\x81\xd1\x84\xd0\xb0\xd0\xbb\xd1\x8c\xd1\x82')),
                ('map_rayon', models.ImageField(upload_to=b'upload/maps', verbose_name=b'\xd0\x9a\xd0\xb0\xd1\x80\xd1\x82\xd0\xb0', blank=True)),
            ],
            options={
                'verbose_name': '\u0440\u0430\u0439\u043e\u043d',
                'verbose_name_plural': '\u041a\u0430\u0440\u0442\u044b \u0440\u0430\u0439\u043e\u043d\u043e\u0432',
            },
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='ReportImg',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.ImageField(upload_to=b'upload/roads', max_length=250, verbose_name=b'\xd0\xa4\xd0\xbe\xd1\x82\xd0\xbe')),
                ('report', models.ForeignKey(related_name='pics', verbose_name=b'\xd0\x9e\xd1\x82\xd1\x87\xd0\xb5\xd1\x82', to='roads.Report')),
            ],
        ),
        migrations.CreateModel(
            name='Road',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=512, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
                ('body', models.TextField(verbose_name=b'\xd0\x9e\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5', blank=True)),
                ('pic', models.ImageField(upload_to=b'upload/roads', max_length=250, verbose_name=b'\xd0\x9a\xd0\xb0\xd1\x80\xd1\x82\xd0\xb0-\xd1\x81\xd1\x85\xd0\xb5\xd0\xbc\xd0\xb0', blank=True)),
                ('cat', models.CharField(max_length=3, verbose_name=b'\xd0\x92\xd0\xb8\xd0\xb4', choices=[(b'str', b'\xd0\xa1\xd1\x82\xd1\x80\xd0\xbe\xd0\xb8\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c\xd1\x81\xd1\x82\xd0\xb2\xd0\xbe'), (b'rec', b'\xd0\xa0\xd0\xb5\xd0\xba\xd0\xbe\xd0\xbd\xd1\x81\xd1\x82\xd1\x80\xd1\x83\xd0\xba\xd1\x86\xd0\xb8\xd1\x8f'), (b'rem', b'\xd0\xa0\xd0\xb5\xd0\xbc\xd0\xbe\xd0\xbd\xd1\x82')])),
                ('onsite', models.BooleanField(default=False, verbose_name=b'\xd0\x9f\xd0\xbe\xd0\xba\xd0\xb0\xd0\xb7\xd1\x8b\xd0\xb2\xd0\xb0\xd1\x82\xd1\x8c \xd0\xbd\xd0\xb0 \xd1\x81\xd0\xb0\xd0\xb9\xd1\x82\xd0\xb5')),
                ('report', models.BooleanField(default=False, verbose_name=b'\xd0\x95\xd1\x81\xd1\x82\xd1\x8c \xd0\xbe\xd1\x82\xd1\x87\xd0\xb5\xd1\x82\xd1\x8b')),
                ('complete', models.BooleanField(default=False, verbose_name=b'\xd0\x97\xd0\xb0\xd0\xb2\xd0\xb5\xd1\x80\xd1\x88\xd0\xb5\xd0\xbd')),
                ('contractor', models.ForeignKey(verbose_name=b'\xd0\x9f\xd0\xbe\xd0\xb4\xd1\x80\xd1\x8f\xd0\xb4\xd1\x87\xd0\xb8\xd0\xba', blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u043e\u0431\u044a\u0435\u043a\u0442',
                'verbose_name_plural': '\u041e\u0431\u044a\u0435\u043a\u0442\u044b',
            },
        ),
        migrations.AddField(
            model_name='report',
            name='road',
            field=models.ForeignKey(related_name='reps', verbose_name=b'\xd0\x9e\xd0\xb1\xd1\x8a\xd0\xb5\xd0\xba\xd1\x82', to='roads.Road'),
        ),
    ]
