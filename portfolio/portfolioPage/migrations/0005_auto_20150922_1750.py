# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioPage', '0004_auto_20150916_2050'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='description',
        ),
        migrations.AddField(
            model_name='job',
            name='d1',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='d10',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='d2',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='d3',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='d4',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='d5',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='d6',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='d7',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='d8',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='d9',
            field=models.TextField(null=True),
        ),
    ]
