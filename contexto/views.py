from rest_framework import viewsets
from rest_framework.response import Response
from contexto.models import Contexto
from contexto.serializers import ContextoSerializer
import time
from rest_framework.decorators import action
from happytransformer import GENSettings
from happytransformer import HappyGeneration
from asgiref.sync import sync_to_async
from googletrans import Translator

happy_gen = HappyGeneration("GPT-NEO-1.3B", "EleutherAI/gpt-neo-1.3B")
args = GENSettings(no_repeat_ngram_size=2)

# Create your views here.
class ContextoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Contexto.objects.all()
    serializer_class = ContextoSerializer


    @action(detail=True, methods=['POST'], name='create context')
    def create(self, request,*args, **kwargs):
        context_data = request.data
        result = happy_gen.generate_text(context_data["text_generated"])
        translator = Translator()

        translated_text = translator.translate(result.text, dest='es')
        print(translated_text.text)

        time.sleep(1)   
        new_context = Contexto.objects.create(text_generated = translated_text.text )
        new_context.save()
        serializer = ContextoSerializer(new_context)
        return Response(serializer.data)


class ContextoOriginalViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Contexto.objects.all()
    serializer_class = ContextoSerializer


    @action(detail=True, methods=['POST'], name='create context inglish')
    def create(self, request,*args, **kwargs):
        context_data = request.data
        result = happy_gen.generate_text(context_data["text_generated"])

        time.sleep(5)   
        new_context = Contexto.objects.create(text_generated = result.text )
        new_context.save()
        serializer = ContextoSerializer(new_context)
        return Response(serializer.data)