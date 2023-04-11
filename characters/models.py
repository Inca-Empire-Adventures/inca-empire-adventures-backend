from django.db import models
from statistics_user.models import StatisticsUser
from django.contrib.auth import get_user_model

# Create your models here.
class Character(models.Model):
    characterName = models.CharField(max_length=25)
    statistic = models.OneToOneField(StatisticsUser,on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='characters')


   