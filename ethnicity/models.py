from django.db import models
from statistics_user.models import StatisticsUser

# Create your models here.
class Ethnicity(models.Model):
    name = models.CharField(max_length=50)
    statistics = models.OneToOneField(StatisticsUser, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.name