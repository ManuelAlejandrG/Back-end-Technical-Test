from django.db import models

# Create your models here.


class Pokemones(models.Model):
    """ This class is for creating the database.
    Note that this model contains the data necessary 
    for the application and is stored in an sql database.
    """

    evolution = models.CharField(max_length=100)
    poke_id =  models.IntegerField(unique=True)
    name = models.CharField(max_length=20 )
    min_level = models.IntegerField(null=True)
    needs_overworld_rain = models.BooleanField(null=True)
    turn_upside_down = models.BooleanField(null=True)

    def __str__(self):
        return self.name