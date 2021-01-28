from django.db import models

# Create your models here.


class Pokemones(models.Model):
    """ This class is for creating the database.
    Note that this model contains the data necessary 
    for the application and is stored in an sql database.
    """
    
    evolution = models.CharField(max_length=100)
    poke_id =  models.IntegerField(unique=True)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name