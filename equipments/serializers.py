from rest_framework import serializers
from characters.models import Character
from equipments.models import Equipment

class EquipmentSerializer(serializers.ModelSerializer):
    character = serializers.PrimaryKeyRelatedField(many=False, queryset=Character.objects.all(), allow_null = True)
    class Meta:
        model = Equipment
        fields = ['id', 'name', 'character','url']