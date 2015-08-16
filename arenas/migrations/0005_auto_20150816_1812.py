# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('arenas', '0004_auto_20150811_0255'),
    ]

    operations = [
        migrations.CreateModel(
            name='FreeAgents',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('arena', models.ForeignKey(to='arenas.Arena')),
                ('player', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Inbox',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.TextField()),
                ('from_user', models.ForeignKey(related_name='from_user', to=settings.AUTH_USER_MODEL)),
                ('to_user', models.ForeignKey(related_name='to_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='rating',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 16, 18, 12, 44, 218159, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
