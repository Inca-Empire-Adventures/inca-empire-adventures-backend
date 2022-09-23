from rest_framework import serializers
from characters.models import Character
from professions.models import Profession
from professions.serializers import ProfessionSerializer
from races.models import Race
from races.serializers import RaceSerializer

class CharacterSerializer(serializers.ModelSerializer):
    #profession = serializers.PrimaryKeyRelatedField(many=False, queryset=Profession.objects.all(), allow_null = True)
    #race = serializers.PrimaryKeyRelatedField(many=False, queryset=Race.objects.all(), allow_null = True)
    profession = ProfessionSerializer(many=False,allow_null= True)
    race = RaceSerializer(many=False,allow_null = True)
    class Meta:
        model = Character
        fields = ['id', 'nameGroup', 'namePlayer', 'profession', 'race', 'url']

    def create(self, validated_data):
        character = Character.objects.create(**validated_data)
        character.save()
        return character