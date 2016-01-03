#from django.db import models
from django.contrib.gis.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.gis.geos import GEOSGeometry
from players import models as PlayerModels
# Create your models here.


class Arena(models.Model):
    title = models.CharField(max_length=255)
    title_2 = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    address_2 = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    coords = models.PointField(null=True, blank=True)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.title

    class Meta:
        db_table = 'arenas'

    @property
    def lat(self):
        if self.coords:
            return self.coords.y

    @property
    def lng(self):
        if self.coords:
            return self.coords.x


class CustomUser(AbstractUser):
    positions = models.ManyToManyField(PlayerModels.Positions)


class Rating(models.Model):
    ice_surface = models.IntegerField()
    referees = models.IntegerField()
    lockers = models.IntegerField()
    league = models.IntegerField()
    teams = models.IntegerField()
    comment = models.TextField()
    user = models.ForeignKey(CustomUser)
    arena = models.ForeignKey(Arena)
    date_created = models.DateTimeField(auto_now_add=True)


class FreeAgents(models.Model):
    player = models.ForeignKey(CustomUser)
    arena = models.ForeignKey(Arena)
    date_created = date_created = models.DateTimeField(auto_now_add=True)


class Inbox(models.Model):
    to_user = models.ForeignKey(CustomUser, related_name="to_user")
    from_user = models.ForeignKey(CustomUser, related_name="from_user")
    message = models.TextField()
    date_created = date_created = models.DateTimeField(auto_now_add=True)
