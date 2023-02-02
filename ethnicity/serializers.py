from rest_framework import serializers
from ethnicity.models import Ethnicity
from statistics_user.models import StatisticsUser

class EthnicitySerializer(serializers.ModelSerializer):
    statistics = serializers.PrimaryKeyRelatedField(many=False, queryset=StatisticsUser.objects.all(),allow_null = True)
    class Meta:
        model = Ethnicity
        fields = ['id', 'name','statistics','url']