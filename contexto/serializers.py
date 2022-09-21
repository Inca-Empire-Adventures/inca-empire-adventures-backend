from rest_framework import serializers

from contexto.models import Contexto

class ContextoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contexto
        fields = ['id', 'text_generated']