# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('arenas', '0003_arena_ratings'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.RemoveField(
            model_name='userrating',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='userrating',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='userrating',
            name='user',
        ),
        migrations.RemoveField(
            model_name='arena',
            name='ratings',
        ),
        migrations.AddField(
            model_name='rating',
            name='arena',
            field=models.ForeignKey(default='', to='arenas.Arena'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rating',
            name='comment',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rating',
            name='user',
            field=models.ForeignKey(default='', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='UserRating',
        ),
    ]
