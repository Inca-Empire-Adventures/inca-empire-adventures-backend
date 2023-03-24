from rest_framework import serializers
from ethnicity.models import Ethnicity
from statistics_user.models import StatisticsUser

class EthnicitySerializer(serializers.ModelSerializer):   
    class Meta:
        model = Ethnicity
        fields = ['id', 'name','url']