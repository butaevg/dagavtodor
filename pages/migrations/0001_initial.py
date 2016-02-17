# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=512, verbose_name=b'\xd0\x97\xd0\xb0\xd0\xb3\xd0\xbe\xd0\xbb\xd0\xbe\xd0\xb2\xd0\xbe\xd0\xba')),
                ('slug', models.SlugField(max_length=512, verbose_name=b'URL')),
                ('body', models.TextField(verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xba\xd1\x81\xd1\x82')),
            ],
            options={
                'verbose_name': '\u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0443',
                'verbose_name_plural': '\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u044b',
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'\xd0\xa0\xd0\xb0\xd0\xb7\xd0\xb4\xd0\xb5\xd0\xbb')),
            ],
            options={
                'verbose_name': '\u0440\u0430\u0437\u0434\u0435\u043b',
                'verbose_name_plural': '\u0420\u0430\u0437\u0434\u0435\u043b',
            },
        ),
        migrations.AddField(
            model_name='page',
            name='section',
            field=models.ForeignKey(related_name='sec', to='pages.Section'),
        ),
    ]
