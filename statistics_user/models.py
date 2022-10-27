from django.db import models

# Create your models here.
class StatisticsUser(models.Model):
    strength = models.IntegerField();
    intelligence = models.IntegerField();
    dexterity = models.IntegerField();
    charisma = models.IntegerField();
    wisdom = models.IntegerField();
    constitucion = models.IntegerField();