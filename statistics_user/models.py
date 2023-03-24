from django.db import models
from ethnicity.models import Ethnicity
# Create your models here.
class StatisticsUser(models.Model):
    strength = models.IntegerField();
    intelligence = models.IntegerField();
    dexterity = models.IntegerField();
    charisma = models.IntegerField();
    wisdom = models.IntegerField();
    constitucion = models.IntegerField();
    ethnicity = models.ForeignKey(Ethnicity, on_delete=models.SET_NULL, null=True, blank=True)
