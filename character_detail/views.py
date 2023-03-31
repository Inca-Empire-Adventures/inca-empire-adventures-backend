from rest_framework import viewsets, permissions
from character_detail.models import CharacterDetail
from character_detail.serializers import CharacterDetailSerializer
from django.db.models import Q
# Create your views here.
class CharacterDetailViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CharacterDetail.objects.all()
    serializer_class = CharacterDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        # Obtener todos los character_detail que pertenecen al usuario
        queryset = CharacterDetail.objects.filter(character__user=user)
        # Filtro opcional para buscar por nombre de character
        character_name = self.request.query_params.get('character_name')
        if character_name:
            queryset = queryset.filter(Q(character__user=user) & Q(character__characterName=character_name))
        return queryset