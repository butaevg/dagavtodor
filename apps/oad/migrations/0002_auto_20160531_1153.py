# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oad', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('count_all', models.CharField(max_length=20)),
                ('count_current', models.CharField(max_length=20)),
                ('val_all', models.CharField(max_length=20)),
                ('val_current', models.CharField(max_length=20)),
                ('position', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': '\u0440\u0430\u0431\u043e\u0442\u0443',
                'verbose_name_plural': '\u0420\u0430\u0431\u043e\u0442\u044b',
            },
        ),
        migrations.AlterField(
            model_name='worktype',
            name='num_unit',
            field=models.IntegerField(null=True, verbose_name=b'\xd0\x9d\xd0\xbe\xd0\xbc\xd0\xb5\xd1\x80 \xd0\xb5\xd0\xb4\xd0\xb8\xd0\xbd\xd0\xb8\xd1\x87. \xd1\x80\xd0\xb0\xd1\x81\xd1\x86\xd0\xb5\xd0\xbd\xd0\xba\xd0\xb8', blank=True),
        ),
        migrations.AddField(
            model_name='journal',
            name='work_type',
            field=models.ForeignKey(related_name='work', to='oad.WorkType'),
        ),
    ]
