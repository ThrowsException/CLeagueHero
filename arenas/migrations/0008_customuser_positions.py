# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '__first__'),
        ('arenas', '0007_arena_coords'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='positions',
            field=models.ManyToManyField(to='players.Positions'),
        ),
    ]
