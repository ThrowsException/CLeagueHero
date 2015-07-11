from django.db import models

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
