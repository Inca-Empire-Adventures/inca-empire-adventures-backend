from rest_framework import serializers
from statistics_user.models import StatisticsUser

class StatisticsUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatisticsUser
        fields = ['id', 'strength','intelligence','dexterity','charisma','wisdom','constitucion','ethnicityType','url']