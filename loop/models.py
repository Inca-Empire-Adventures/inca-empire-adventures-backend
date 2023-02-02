from django.db import models
from adventures.models import Adventures

# Create your models here.
class Loop(models.Model):
    quantity = models.IntegerField()
    adventure = models.ForeignKey(Adventures, on_delete=models.CASCADE, null=True)