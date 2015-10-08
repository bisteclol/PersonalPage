# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioPage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='begin_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='job',
            name='end_date',
            field=models.DateField(null=True, blank=True),
        ),
    ]
