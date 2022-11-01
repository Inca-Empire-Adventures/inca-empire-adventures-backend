from rest_framework import serializers
from races.models import Race
from statistics_user.models import StatisticsUser

class RaceSerializer(serializers.ModelSerializer):
    statistics = serializers.PrimaryKeyRelatedField(many=False, queryset=StatisticsUser.objects.all(),allow_null = True)
    class Meta:
        model = Race
        fields = ['id', 'name','statistics','url']