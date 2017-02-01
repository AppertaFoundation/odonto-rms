# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import opal.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('opal', '0027_auto_20170114_1302'),
        ('rms', '0015_auto_20170201_1252'),
    ]

    operations = [
        migrations.CreateModel(
            name='Xray',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('updated', models.DateTimeField(null=True, blank=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('img', models.FileField(upload_to=b'')),
                ('notes', models.TextField(null=True, blank=True)),
                ('created_by', models.ForeignKey(related_name='created_rms_xray_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('episode', models.ForeignKey(to='opal.Episode')),
                ('updated_by', models.ForeignKey(related_name='updated_rms_xray_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
        migrations.RemoveField(
            model_name='fileupload',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='fileupload',
            name='episode',
        ),
        migrations.RemoveField(
            model_name='fileupload',
            name='updated_by',
        ),
        migrations.DeleteModel(
            name='FileUpload',
        ),
    ]
