from django.shortcuts import render
from rest_framework import viewsets
from adventures.models import Adventures
from adventures.serializers import AdventureSerializer
from skills.models import Skills

from skills.serializers import SkillsSerializer

# Create your views here.

class AdventureViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Adventures.objects.all().order_by('id')
    serializer_class = AdventureSerializer
