from rest_framework import serializers
from characters.models import Character
from equipments.models import Equipment
from item.models import Item

class EquipmentSerializer(serializers.ModelSerializer):
    character = serializers.PrimaryKeyRelatedField(many=False, queryset=Character.objects.all(), allow_null = True)
    item = serializers.PrimaryKeyRelatedField(many=False, queryset=Item.objects.all(), allow_null = True)
    
    class Meta:
        model = Equipment
        fields = ['id', 'quantity', 'character', 'item','url']