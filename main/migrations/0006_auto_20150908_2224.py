# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20150908_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imgcontainer',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
