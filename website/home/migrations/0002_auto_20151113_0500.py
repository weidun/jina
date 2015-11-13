# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(null=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.TextField(max_length=20),
        ),
    ]
