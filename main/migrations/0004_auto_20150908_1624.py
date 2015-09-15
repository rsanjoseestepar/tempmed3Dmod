# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_imgcontainer_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imgcontainer',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
