from django.db import models
from statistics_user.enums import EthnicityType

# Create your models here.
class StatisticsUser(models.Model):
    strength = models.IntegerField();
    intelligence = models.IntegerField();
    dexterity = models.IntegerField();
    charisma = models.IntegerField();
    wisdom = models.IntegerField();
    constitucion = models.IntegerField();
    ethnicityType = models.CharField(choices=EthnicityType.choices, max_length=50)

    def __str__(self):
        return self.ethnicityType
