from rest_framework import serializers
from professions.models import Profession
from statistics_user.models import StatisticsUser

class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = ['id', 'name', 'url']