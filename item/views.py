from rest_framework import viewsets, permissions
from item.models import Item
from item.serializers import ItemSerializer

# Create your views here.
class ItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Item.objects.all().order_by('id')
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated]
