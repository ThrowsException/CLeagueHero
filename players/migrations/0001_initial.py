# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Positions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('position', models.IntegerField(choices=[(1, b'Center'), (2, b'Right Wing'), (3, b'Left Wing'), (4, b'Defense'), (5, b'Goalie')])),
            ],
        ),
    ]
