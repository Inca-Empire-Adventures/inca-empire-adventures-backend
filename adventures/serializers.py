from rest_framework import serializers
from adventures.models import Adventures
from characters.models import Character

class AdventureSerializer(serializers.ModelSerializer):
    character = serializers.PrimaryKeyRelatedField(many=False, queryset=Character.objects.all(), allow_null=True)

    class Meta:
        model = Adventures
        fields = ['url', 'description', 'character']