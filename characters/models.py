from django.db import models


# Create your models here.
class Character(models.Model):
    nameGroup = models.CharField(max_length=25)
    namePlayer = models.CharField(max_length=25)
    raceId = models.IntegerField()
    professionId = models.IntegerField()


   