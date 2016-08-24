# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arenas', '0008_customuser_positions'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='freeagents',
            unique_together=set([('player', 'arena')]),
        ),
    ]
