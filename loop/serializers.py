from rest_framework import serializers
from adventures.models import Adventures
from loop.models import Loop

# Create your models here.
class LoopSerializer(serializers.ModelSerializer):
    adventure = serializers.PrimaryKeyRelatedField(many=False, queryset=Adventures.objects.all(),allow_null = True)

    class Meta:
        model = Loop
        fields = ['id', 'quantity', 'adventure', 'url']