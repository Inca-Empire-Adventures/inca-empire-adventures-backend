from django.db import models

from professions.models import Profession
from races.models import Race


# Create your models here.
class Character(models.Model):
    nameGroup = models.CharField(max_length=25)
    namePlayer = models.CharField(max_length=25)
    profession = models.ForeignKey(Profession, on_delete=models.SET_NULL, null=True)
    race = models.OneToOneField(Race, on_delete=models.CASCADE, null=True)

   