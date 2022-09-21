from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from equipments import serializers
from equipments.models import Equipment
from equipments.serializers import EquipmentSerializer

class EquipmentList(APIView):
    def get(self, request, format=None):
        objects = Equipment.objects.all()
        serializer = EquipmentSerializer(objects, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EquipmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EquipmentDetail(APIView):
    def get_object(self, pk):
        try:
            return Equipment.objects.get(pk=pk)
        except Equipment.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        object =self.get_object(pk)
        serializer = EquipmentSerializer(object)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        object = self.get_object(pk)
        serializer = EquipmentSerializer(object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        object = self.get_object(pk)
        object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

