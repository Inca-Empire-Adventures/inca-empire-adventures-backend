from rest_framework import serializers
from auth_user.models import User
from characters.models import Character
from statistics_user.models import StatisticsUser

class CharacterSerializer(serializers.ModelSerializer):
    statisctic = serializers.PrimaryKeyRelatedField(many=False, queryset=StatisticsUser.objects.all(), allow_null=True)
    user = serializers.PrimaryKeyRelatedField(many=False, queryset=User.objects.all(), allow_null=True)

    def validate_statisctic(self, value):
        if value is not None and Character.objects.filter(statisctic=value).exclude(pk=self.instance.pk).exists():
            raise serializers.ValidationError("This statistics has already been assigned to another Character.")
        return value
    class Meta:
        model = Character
        fields = ['id', 'characterName', 'statisctic', 'user', 'url']