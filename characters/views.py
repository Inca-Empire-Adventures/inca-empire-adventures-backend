from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from characters.models import Character
from characters.serializers import CharacterSerializer
from rest_framework import viewsets

# Create your views here.

class CharacterViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Character.objects.all().order_by('id')
    serializer_class = CharacterSerializer
