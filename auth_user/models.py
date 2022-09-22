from rest_framework import serializers
from django.contrib.auth.models import AbstractUser
from django.db import models
from characters.serializers import CharacterSerializer

from characters.models import Character
# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    character = models.OneToOneField(Character, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.username


class UserSerializer(serializers.HyperlinkedModelSerializer):
    character = serializers.PrimaryKeyRelatedField(many=False, queryset=Character.objects.all(),allow_null = True)

    class Meta:
        model = User

        fields = ['url', 'username','character']

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.save()
        return user