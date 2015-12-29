# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('arenas', '0006_auto_20150816_1813'),
    ]

    operations = [
        migrations.AddField(
            model_name='arena',
            name='coords',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326, null=True, blank=True),
        ),
    ]
