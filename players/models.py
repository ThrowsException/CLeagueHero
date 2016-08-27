from django.db import models
from django.core.validators import RegexValidator


class Positions(models.Model):
    CENTER = 1
    RIGHT_WING = 2
    LEFT_WING = 3
    DEFENSE = 4
    GOALIE = 5
    STATUS_CHOICES = (
        (CENTER, 'Center'),
        (RIGHT_WING, 'Right Wing'),
        (LEFT_WING, 'Left Wing'),
        (DEFENSE, 'Defense'),
        (GOALIE, 'Goalie')
    )

    position = models.IntegerField(choices=STATUS_CHOICES)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], blank=True, max_length=16) # validators should be a list
