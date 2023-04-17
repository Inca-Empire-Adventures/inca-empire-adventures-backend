from django.db import models
from statistics_user.enums import EthnicityType
import json

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
    
    def get_statistics_as_dict(self):
        # Devuelve las estadísticas como un diccionario
        statistics_dict = {
            "strength": self.strength,
            "intelligence": self.intelligence,
            "dexterity": self.dexterity,
            "charisma": self.charisma,
            "wisdom": self.wisdom,
            "constitucion": self.constitucion
        }
        return json.dumps(statistics_dict)
