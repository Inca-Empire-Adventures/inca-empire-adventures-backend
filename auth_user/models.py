from rest_framework import serializers
from django.contrib.auth.models import User, AbstractUser
from django.db import models

from characters.models import Character
# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    character = models.OneToOneField(Character, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.username


class UserSerializer(serializers.HyperlinkedModelSerializer):
    character = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='id'
    )

    class Meta:
        model = User
        fields = ['url', 'username','character']