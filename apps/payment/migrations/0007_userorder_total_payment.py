# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-06 20:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0006_userorder_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='userorder',
            name='total_payment',
            field=models.IntegerField(default=0),
        ),
    ]
