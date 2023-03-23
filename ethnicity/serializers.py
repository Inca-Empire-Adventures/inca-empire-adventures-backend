from rest_framework import serializers
from ethnicity.models import Ethnicity
from statistics_user.models import StatisticsUser

class EthnicitySerializer(serializers.ModelSerializer):
    statistics = serializers.PrimaryKeyRelatedField(many=False, queryset=StatisticsUser.objects.all(), allow_null = True)

    def validate_statistics(self, value):
        if value is not None and Ethnicity.objects.filter(statistics=value).exclude(pk=self.instance.pk).exists():
            raise serializers.ValidationError("This statistics has already been assigned to another Ethnicity.")
        return value
    
    class Meta:
        model = Ethnicity
        fields = ['id', 'name','statistics','url']