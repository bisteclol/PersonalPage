# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('company', models.CharField(max_length=200)),
                ('job_title', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
    ]
