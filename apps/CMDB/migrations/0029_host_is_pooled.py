# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-16 10:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CMDB', '0028_yewutreemptt_islast'),
    ]

    operations = [
        migrations.AddField(
            model_name='host',
            name='is_pooled',
            field=models.BooleanField(default=True, verbose_name='\u662f\u5426\u5728\u8d44\u6e90\u6c60\u4e2d'),
        ),
    ]
