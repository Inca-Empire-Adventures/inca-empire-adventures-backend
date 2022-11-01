from rest_framework import serializers
from professions.models import Profession
from statistics_user.models import StatisticsUser

class ProfessionSerializer(serializers.ModelSerializer):
    statistics = serializers.PrimaryKeyRelatedField(many=False, queryset=StatisticsUser.objects.all(),allow_null = True)

    class Meta:
        model = Profession
        fields = ['id', 'name','statistics','url']