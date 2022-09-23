from races.models import Race
from races.serializers import RaceSerializer
from rest_framework import viewsets

class RacesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Race.objects.all().order_by('id')
    serializer_class = RaceSerializer


