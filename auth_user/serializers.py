from auth_user.models import User
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username','password']

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.save()
        return user