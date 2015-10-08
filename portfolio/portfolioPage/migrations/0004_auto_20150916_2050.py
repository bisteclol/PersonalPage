# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioPage', '0003_auto_20150916_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
