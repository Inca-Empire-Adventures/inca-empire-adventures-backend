from django.db import models

from statistics_user.models import StatisticsUser

# Create your models here.

class Profession(models.Model):
    name = models.CharField(max_length=60)
    statistics = models.OneToOneField(StatisticsUser, on_delete=models.CASCADE, null=True)
    