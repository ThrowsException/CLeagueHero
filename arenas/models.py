from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Arena(models.Model):
    title = models.CharField(max_length=255)
    title_2 = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    address_2 = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

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
    comment = models.TextField()
    user = models.ForeignKey(CustomUser)
    arena = models.ForeignKey(Arena)

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Rating._meta.fields]
