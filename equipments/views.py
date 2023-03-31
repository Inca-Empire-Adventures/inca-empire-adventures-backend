from equipments.models import Equipment
from equipments.serializers import EquipmentSerializer
from rest_framework import viewsets, permissions

class EquipmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Equipment.objects.all().order_by('id')
    serializer_class = EquipmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    
