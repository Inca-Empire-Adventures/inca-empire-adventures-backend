from django.db import models

# Create your models here.
class Equipment(models.Model):
    name = models.CharField(max_length=25)
    characterId = models.IntegerField()
   