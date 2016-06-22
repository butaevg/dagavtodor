# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('name', models.CharField(max_length=180, verbose_name=b'\xd0\x98\xd0\xbc\xd1\x8f')),
                ('username', models.CharField(unique=True, max_length=80, verbose_name=b'\xd0\x9b\xd0\xbe\xd0\xb3\xd0\xb8\xd0\xbd')),
                ('fullname', models.CharField(max_length=150, verbose_name=b'\xd0\x9f\xd0\xbe\xd0\xbb\xd0\xbd\xd0\xbe\xd0\xb5 \xd0\xb8\xd0\xbc\xd1\x8f')),
                ('insta', models.CharField(max_length=150, verbose_name=b'Instagram', blank=True)),
                ('is_admin', models.BooleanField(default=False, verbose_name=b'\xd0\x90\xd0\xb4\xd0\xbc\xd0\xb8\xd0\xbd\xd0\xb8\xd1\x81\xd1\x82\xd1\x80\xd0\xb0\xd1\x82\xd0\xbe\xd1\x80')),
            ],
            options={
                'db_table': 'users',
                'verbose_name': '\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f',
                'verbose_name_plural': '\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0438',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150, verbose_name=b'\xd0\xa0\xd0\xb0\xd0\xb7\xd0\xb4\xd0\xb5\xd0\xbb')),
                ('name_menu', models.CharField(max_length=150, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xb4\xd0\xbb\xd1\x8f \xd0\xbc\xd0\xb5\xd0\xbd\xd1\x8e')),
                ('url', models.CharField(max_length=150, verbose_name=b'\xd0\xa1\xd1\x81\xd1\x8b\xd0\xbb\xd0\xba\xd0\xb0')),
            ],
            options={
                'verbose_name': '\u0440\u0430\u0437\u0434\u0435\u043b',
                'verbose_name_plural': '\u0420\u0430\u0437\u0434\u0435\u043b\u044b',
            },
        ),
        migrations.CreateModel(
            name='UserCat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'\xd0\x93\xd1\x80\xd1\x83\xd0\xbf\xd0\xbf\xd0\xb0')),
                ('cats', models.ManyToManyField(to='users.Category', verbose_name='\u0420\u0430\u0437\u0434\u0435\u043b\u044b')),
            ],
            options={
                'db_table': 'users_group',
                'verbose_name': '\u0433\u0440\u0443\u043f\u043f\u0443',
                'verbose_name_plural': '\u0413\u0440\u0443\u043f\u043f\u044b',
            },
        ),
        migrations.AddField(
            model_name='duser',
            name='cat',
            field=models.ForeignKey(verbose_name=b'\xd0\x93\xd1\x80\xd1\x83\xd0\xbf\xd0\xbf\xd0\xb0', to='users.UserCat', null=True),
        ),
    ]
