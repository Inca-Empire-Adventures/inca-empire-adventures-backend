from rest_framework import serializers
from characters.models import Character
from statistics_user.models import StatisticsUser
from django.contrib.auth import get_user_model

class CharacterSerializer(serializers.ModelSerializer):
    statistic = serializers.PrimaryKeyRelatedField(many=False, queryset=StatisticsUser.objects.all(), allow_null=True)
    user = serializers.PrimaryKeyRelatedField(queryset=get_user_model().objects.all(), default=serializers.CurrentUserDefault())
    
    def validate_statistic(self, value):
        if value is not None and self.instance is not None and Character.objects.filter(statistic=value).exclude(pk=self.instance.pk).exists():
            raise serializers.ValidationError("This statistics has already been assigned to another Character.")

        if self.instance is None and Character.objects.filter(statistic = value).exists():
            raise serializers.ValidationError("This statistics has already been assigned to another Character.")

        return value
    
    class Meta:
        model = Character
        fields = ['id', 'characterName', 'statistic', 'user', 'url']