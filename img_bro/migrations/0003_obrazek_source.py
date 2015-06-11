# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('img_bro', '0002_auto_20150611_0136'),
    ]

    operations = [
        migrations.AddField(
            model_name='obrazek',
            name='source',
            field=models.URLField(default=b''),
            preserve_default=True,
        ),
    ]
