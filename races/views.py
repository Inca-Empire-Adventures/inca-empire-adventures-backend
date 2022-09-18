from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from races import serializers
from races.models import Race
from races.serializers import RaceSerializer


class RaceList(APIView):
    def get(self, request, format=None):
        races = Race.objects.all()
        serializer = RaceSerializer(races, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RaceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RaceDetail(APIView):
    def get_object(self, pk):
        try:
            return Race.objects.get(pk=pk)
        except Race.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        race =self.get_object(pk)
        serializer = RaceSerializer(race)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        race = self.get_object(pk)
        serializer = RaceSerializer(race, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        race = self.get_object(pk)
        race.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

