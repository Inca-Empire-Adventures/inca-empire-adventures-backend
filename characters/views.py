from characters.models import Character
from characters.serializers import CharacterSerializer
from rest_framework import viewsets, permissions

# Create your views here.

class CharacterViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = CharacterSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Character.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)