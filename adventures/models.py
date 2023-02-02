from django.db import models

from characters.models import Character

# Create your models here.
class Adventures(models.Model):
    description = models.CharField(max_length=250)
    character = models.ForeignKey(Character, on_delete=models.CASCADE, null=True)