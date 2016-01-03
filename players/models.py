from django.db import models


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
