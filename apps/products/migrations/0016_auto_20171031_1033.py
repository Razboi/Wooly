# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-31 10:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_product_section'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='clothes',
        ),
        migrations.RemoveField(
            model_name='product',
            name='footwear',
        ),
        migrations.AlterField(
            model_name='product',
            name='section',
            field=models.CharField(choices=[('Prendas', 'Prendas'), ('Calzado', 'Calzado'), ('Complementos', 'Complementos')], default='Prendas', max_length=20),
        ),
    ]
