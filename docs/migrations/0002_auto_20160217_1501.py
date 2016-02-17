# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doc',
            name='url',
            field=models.FileField(upload_to=b'docs', max_length=250, verbose_name=b'\xd0\xa4\xd0\xb0\xd0\xb9\xd0\xbb'),
        ),
    ]
