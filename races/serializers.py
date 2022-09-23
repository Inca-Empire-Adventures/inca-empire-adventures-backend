from rest_framework import serializers
from races.models import Race

class RaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Race
        fields = ['id', 'name','url']