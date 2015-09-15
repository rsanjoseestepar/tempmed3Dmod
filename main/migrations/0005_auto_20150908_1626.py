# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20150908_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imgcontainer',
            name='name',
            field=models.CharField(default=b'NoName', max_length=100),
        ),
    ]
