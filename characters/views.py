from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from characters.models import Character
from characters.serializers import CharacterSerializer

# Create your views here.
class CharacterList(APIView):
    def get(self, request, format=None):
        objects = Character.objects.all()
        serializer = CharacterSerializer(objects, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CharacterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CharacterDetail(APIView):
    def get_object(self, pk):
        try:
            return Character.objects.get(pk=pk)
        except Character.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        object =self.get_object(pk)
        serializer = CharacterSerializer(object)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        object = self.get_object(pk)
        serializer = CharacterSerializer(object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        object = self.get_object(pk)
        object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

