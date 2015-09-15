# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import main.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BodyPart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('body_part', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ImgContainer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tentative_img_type', models.CharField(default=b'0', max_length=10)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('deleted', models.DateTimeField(auto_now=True)),
                ('file', models.FileField(default=b'no_file', upload_to=main.models.upload_to)),
                ('tentative_body_part', models.ManyToManyField(default=b'0', to='main.BodyPart')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MedImg',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file', models.FileField(default=b'no_file', upload_to=main.models.upload_to)),
                ('img_type', models.CharField(max_length=10)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('deleted', models.DateTimeField(auto_now=True)),
                ('body_part', models.ManyToManyField(to='main.BodyPart')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('model_file', models.FileField(default=b'None/no_file', upload_to=main.models.upload_to)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('deleted', models.DateTimeField(auto_now=True)),
                ('medimg', models.ForeignKey(default=b'0', to='main.MedImg')),
            ],
        ),
        migrations.CreateModel(
            name='Organ',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('organ', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AddField(
            model_name='model',
            name='organ',
            field=models.ForeignKey(default=b'0', to='main.Organ'),
        ),
        migrations.AddField(
            model_name='model',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bodypart',
            name='organ',
            field=models.ManyToManyField(to='main.Organ'),
        ),
    ]
