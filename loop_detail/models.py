from django.db import models

from loop.models import Loop

# Create your models here.
class LoopDetail(models.Model):
    content = models.IntegerField() 
    content_type = models.CharField(max_length=30)
    loop = models.ForeignKey(Loop, on_delete=models.CASCADE, null=True)