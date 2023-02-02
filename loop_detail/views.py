from rest_framework import viewsets
from loop_detail.models import LoopDetail
from loop_detail.serializers import LoopDetailSerializer

# Create your views here.
class LoopDetailViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = LoopDetail.objects.all().order_by('id')
    serializer_class = LoopDetailSerializer
