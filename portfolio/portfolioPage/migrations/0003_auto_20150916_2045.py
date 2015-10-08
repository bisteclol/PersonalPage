# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioPage', '0002_auto_20150916_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='end_date',
            field=models.DateField(null=True, default=datetime.date.today, blank=True),
        ),
    ]
