from rest_framework import serializers
from statistics_user.models import StatisticsUser
from ethnicity.models import Ethnicity
class StatisticsUserSerializer(serializers.ModelSerializer):
    ethnicity = serializers.PrimaryKeyRelatedField(many=False, queryset=Ethnicity.objects.all(), allow_null = True)

    class Meta:
        model = StatisticsUser
        fields = ['id', 'strength','intelligence','dexterity','charisma','wisdom','constitucion','ethnicity','url']