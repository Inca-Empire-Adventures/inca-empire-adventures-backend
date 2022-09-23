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
