from django.db import models

# Create your models here.

class Profession(models.Model):
    name = models.CharField(max_length=60)
    