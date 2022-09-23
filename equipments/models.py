from django.db import models

from characters.models import Character

# Create your models here.
class Equipment(models.Model):
    name = models.CharField(max_length=25)
    character = models.ForeignKey(Character,on_delete=models.SET_NULL, null=True)
   