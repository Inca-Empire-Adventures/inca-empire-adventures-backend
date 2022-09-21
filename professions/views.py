from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from professions import serializers
import professions
from professions.models import Profession
from professions.serializers import ProfessionSerializer

# Create your views here.
class ProfessionList(APIView):
    def get(self, request, format=None):
        objects = Profession.objects.all()
        serializer = ProfessionSerializer(objects, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProfessionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfessionDetail(APIView):
    def get_object(self, pk):
        try:
            return Profession.objects.get(pk=pk)
        except Profession.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        object =self.get_object(pk)
        serializer = ProfessionSerializer(object)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        object = self.get_object(pk)
        serializer = ProfessionSerializer(object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        object = self.get_object(pk)
        object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

