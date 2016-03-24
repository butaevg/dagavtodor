# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0004_auto_20160323_1732'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='machineworking',
            name='dep',
        ),
        migrations.AddField(
            model_name='machine',
            name='working',
            field=models.BooleanField(default=True),
        ),
        migrations.DeleteModel(
            name='MachineWorking',
        ),
    ]
