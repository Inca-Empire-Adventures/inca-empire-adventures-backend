from rest_framework import serializers
from characters.models import Character
from statistics_user.models import StatisticsUser
from django.contrib.auth import get_user_model

class CharacterSerializer(serializers.ModelSerializer):
    statisctic = serializers.PrimaryKeyRelatedField(many=False, queryset=StatisticsUser.objects.all(), allow_null=True)
    user = serializers.PrimaryKeyRelatedField(queryset=get_user_model().objects.all(), default=serializers.CurrentUserDefault())
    
    def validate_statisctic(self, value):
        if value is not None and Character.objects.filter(statisctic=value).exclude(pk=self.instance.pk).exists():
            raise serializers.ValidationError("This statistics has already been assigned to another Character.")
        return value
    class Meta:
        model = Character
        fields = ['id', 'characterName', 'statisctic', 'user', 'url']