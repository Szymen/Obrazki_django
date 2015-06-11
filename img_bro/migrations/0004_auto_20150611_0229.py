# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('img_bro', '0003_obrazek_source'),
    ]

    operations = [
        migrations.AlterField(
            model_name='obrazek',
            name='source',
            field=models.CharField(default=b'', max_length=200),
            preserve_default=True,
        ),
    ]
