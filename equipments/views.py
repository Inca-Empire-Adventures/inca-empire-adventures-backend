from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from equipments import serializers
from equipments.models import Equipment
from equipments.serializers import EquipmentSerializer
from rest_framework import viewsets

class EquipmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Equipment.objects.all().order_by('id')
    serializer_class = EquipmentSerializer
