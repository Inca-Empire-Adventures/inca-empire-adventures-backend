from equipments.models import Equipment
from equipments.serializers import EquipmentSerializer
from rest_framework import viewsets, permissions
from django.db.models import Q

class EquipmentViewSet(viewsets.ModelViewSet):
    serializer_class = EquipmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        # Obtener todos los character_detail que pertenecen al usuario
        queryset = Equipment.objects.filter(character__user=user)
        # Filtro opcional para buscar por nombre de character
        character_name = self.request.query_params.get('character_name')
        if character_name:
            queryset = queryset.filter(Q(character__user=user) & Q(character__characterName=character_name))
        return queryset
    
