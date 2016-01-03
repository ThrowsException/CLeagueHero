# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='positions',
            name='position',
            field=models.IntegerField(choices=[(1, b'Center'), (2, b'Right Wing'), (3, b'Left Wing'), (4, b'Defense'), (5, b'Goalie')]),
        ),
    ]
