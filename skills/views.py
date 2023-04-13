from rest_framework import viewsets, permissions
from skills.models import Skills

from skills.serializers import SkillsSerializer

# Create your views here.

class SkillsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Skills.objects.all().order_by('id')
    serializer_class = SkillsSerializer
    permission_classes = [permissions.IsAuthenticated]
