from rest_framework import serializers
from character_detail.models import CharacterDetail
from characters.models import Character
from professions.models import Profession


class CharacterDetailSerializer(serializers.HyperlinkedModelSerializer):
    character = serializers.PrimaryKeyRelatedField(many=False, queryset=Character.objects.all(), allow_null = True)
    profession = serializers.PrimaryKeyRelatedField(many=False, queryset=Profession.objects.all(), allow_null = True)


    class Meta:
        model = CharacterDetail
        fields = ['url', 'character','profession']

    def create(self, validated_data):
        character_detail = CharacterDetail.objects.create(**validated_data)
        character_detail.save()
        return character_detail