from django.db import models
from auth_user.models import User
from statistics_user.models import StatisticsUser


# Create your models here.
class Character(models.Model):
    characterName = models.CharField(max_length=25)
    statisctic = models.OneToOneField(StatisticsUser,on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


   