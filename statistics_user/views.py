from statistics_user.models import StatisticsUser
from statistics_user.serializers import StatisticsUserSerializer
from rest_framework import viewsets

class StatisticsUserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = StatisticsUser.objects.all().order_by('id')
    serializer_class = StatisticsUserSerializer