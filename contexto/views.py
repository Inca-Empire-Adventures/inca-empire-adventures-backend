from rest_framework import viewsets
from rest_framework.response import Response
from contexto.models import Contexto
from contexto.serializers import ContextoSerializer
from rest_framework.decorators import action
from happytransformer import GENSettings
from happytransformer import HappyGeneration
from asgiref.sync import sync_to_async
import time
from googletrans import Translator


happy_gen = HappyGeneration("GPT-NEO", "EleutherAI/gpt-neo-1.3B")
argsIA = GENSettings(no_repeat_ngram_size=2,temperature=0.7,min_length=20,top_k=50, do_sample=True)


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
        result = happy_gen.generate_text(context_data["text_generated"],args=argsIA)
        translator = Translator()

        translated_text = translator.translate(context_data["text_generated"]+result.text, dest='es')
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
        result = happy_gen.generate_text(context_data["text_generated"],args=argsIA)

        time.sleep(1)   
        new_context = Contexto.objects.create(text_generated = context_data["text_generated"]+result.text )
        new_context.save()
        serializer = ContextoSerializer(new_context)
        return Response(serializer.data)
