from rest_framework import viewsets, permissions
from loop.models import Loop
from loop.serializers import LoopSerializer

# Create your views here.
class LoopViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Loop.objects.all().order_by('id')
    serializer_class = LoopSerializer
    permission_classes = [permissions.IsAuthenticated]

