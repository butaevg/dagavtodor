# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0005_auto_20160324_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='psd',
            name='contractor',
            field=models.ForeignKey(related_name='proj', verbose_name=b'\xd0\x9f\xd1\x80\xd0\xbe\xd0\xb5\xd0\xba\xd1\x82\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd1\x89\xd0\xb8\xd0\xba', to=settings.AUTH_USER_MODEL),
        ),
    ]
