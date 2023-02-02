from django.db import models
from item.enums import ItemType

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=50)
    itemType = models.CharField(choices=ItemType.choices, max_length=25)

    def __str__(self):
        return self.name