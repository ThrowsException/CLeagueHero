# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arenas', '0002_auto_20150809_2327'),
    ]

    operations = [
        migrations.AddField(
            model_name='arena',
            name='ratings',
            field=models.ManyToManyField(to='arenas.UserRating'),
        ),
    ]
