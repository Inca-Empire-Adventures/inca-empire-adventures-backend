from rest_framework import serializers
from loop.models import Loop
from loop_detail.models import LoopDetail

# Create your models here.
class LoopDetailSerializer(serializers.ModelSerializer):
    loop = serializers.PrimaryKeyRelatedField(many=False, queryset=Loop.objects.all(),allow_null = True)

    class Meta:
        model = LoopDetail
        fields = ['id', 'content', 'content_type', 'loop', 'url']