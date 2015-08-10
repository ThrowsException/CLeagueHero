from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Arena(models.Model):
    title = models.CharField(max_length=255)
    title_2 = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    address_2 = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    ratings = models.ManyToManyField('UserRating')

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.title

    class Meta:
        db_table = 'arenas'


class CustomUser(AbstractUser):
    pass


class Rating(models.Model):
    ice_surface = models.IntegerField()
    referees = models.IntegerField()
    lockers = models.IntegerField()
    league = models.IntegerField()
    teams = models.IntegerField()


class Comment(models.Model):
    comment = models.TextField()
    user = models.ManyToManyField(CustomUser, through="UserRating")
    rating = models.ManyToManyField(Rating, through="UserRating")

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.comment


class UserRating(models.Model):
    user = models.ForeignKey(CustomUser)
    comment = models.ForeignKey(Comment)
    rating = models.ForeignKey(Rating)
