# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-28 12:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0004_auto_20171028_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='number',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='订单号'),
        ),
    ]
