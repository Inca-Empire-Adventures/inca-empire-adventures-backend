from rest_framework import viewsets
from rest_framework.response import Response
from contexto.models import Contexto
from contexto.serializers import ContextoSerializer
from rest_framework.decorators import action
from rest_framework import renderers
from rest_framework import permissions

# Create your views here.
class ContextoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Contexto.objects.all()
    serializer_class = ContextoSerializer

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)