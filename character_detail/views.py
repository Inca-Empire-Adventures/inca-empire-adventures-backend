from rest_framework import viewsets
from character_detail.models import CharacterDetail
from character_detail.serializers import CharacterDetailSerializer

# Create your views here.
class CharacterDetailViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CharacterDetail.objects.all()
    serializer_class = CharacterDetailSerializer