from django.db import models

from characters.models import Character
from item.models import Item

# Create your models here.
class Equipment(models.Model):
    quantity = models.IntegerField()
    character = models.ForeignKey(Character,on_delete=models.SET_NULL, null=True)
    item = models.ForeignKey(Item,on_delete=models.SET_NULL, null=True)

   