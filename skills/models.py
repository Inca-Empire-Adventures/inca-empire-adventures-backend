from django.db import models

from characters.models import Character

# Create your models here.
class Skills(models.Model):
    name = models.CharField(max_length=60)
    damage = models.IntegerField()
    character = models.ForeignKey(Character, on_delete=models.CASCADE, null=True)