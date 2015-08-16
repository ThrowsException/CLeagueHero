# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('arenas', '0005_auto_20150816_1812'),
    ]

    operations = [
        migrations.AddField(
            model_name='freeagents',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 16, 18, 13, 17, 736797, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inbox',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 16, 18, 13, 23, 400742, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
