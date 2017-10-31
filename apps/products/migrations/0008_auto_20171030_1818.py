# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-30 18:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20171030_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Abrigos', 'Abrigos'), ('Accesorios', 'Accesorios'), ('Americanas', 'Americanas'), ('Basicos', 'Basicos'), ('Botas', 'Botas'), ('Camisas', 'Camisas'), ('Jerseis', 'Jerseis'), ('Novedades', 'Novedades'), ('Ofertas', 'Ofertas'), ('Pantalones', 'Pantalones'), ('Sudaderas', 'Sudaderas'), ('Vaqueros', 'Vaqueros'), ('Zapatillas', 'Zapatillas')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='gender',
            field=models.CharField(choices=[('Men', 'Men'), ('Women', 'Women')], max_length=20, null=True),
        ),
    ]