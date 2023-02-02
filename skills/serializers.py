from rest_framework import serializers
from characters.models import Character

from skills.models import Skills

# Create your models here.
class SkillsSerializer(serializers.ModelSerializer):
    character = serializers.PrimaryKeyRelatedField(many=False, queryset=Character.objects.all(),allow_null = True)

    class Meta:
        model = Skills
        fields = ['id', 'name','damage', 'character', 'url']