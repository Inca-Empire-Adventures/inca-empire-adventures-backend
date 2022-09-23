from professions.models import Profession
from professions.serializers import ProfessionSerializer
from rest_framework import viewsets

# Create your views here.
class ProfessionsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Profession.objects.all().order_by('id')
    serializer_class = ProfessionSerializer
