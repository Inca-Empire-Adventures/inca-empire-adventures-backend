from rest_framework import viewsets
from ethnicity.models import Ethnicity
from ethnicity.serializers import EthnicitySerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
class EthnicityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Ethnicity.objects.all().order_by('id')
    serializer_class = EthnicitySerializer