from rest_framework import serializers
from django.contrib.auth.models import User, AbstractUser
from django.db import models
# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    def __str__(self):
        return self.username


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username']