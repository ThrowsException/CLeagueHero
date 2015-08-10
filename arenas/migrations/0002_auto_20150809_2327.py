# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('arenas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ice_surface', models.IntegerField()),
                ('referees', models.IntegerField()),
                ('lockers', models.IntegerField()),
                ('league', models.IntegerField()),
                ('teams', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserRating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.ForeignKey(to='arenas.Comment')),
                ('rating', models.ForeignKey(to='arenas.Rating')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='rating',
            field=models.ManyToManyField(to='arenas.Rating', through='arenas.UserRating'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, through='arenas.UserRating'),
        ),
    ]
