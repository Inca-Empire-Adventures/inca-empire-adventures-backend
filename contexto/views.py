from rest_framework import viewsets
from rest_framework.response import Response
from contexto.models import Contexto
from contexto.serializers import ContextoSerializer
from rest_framework.decorators import action
from transformers import AutoTokenizer, AutoModelForCausalLM, AutoModel


tokenizer = AutoTokenizer.from_pretrained("KoboldAI/GPT-J-6B-Adventure")
model = AutoModelForCausalLM.from_pretrained("KoboldAI/GPT-J-6B-Adventure")
# Create your views here.
class ContextoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Contexto.objects.all()
    serializer_class = ContextoSerializer


    @action(detail=True, methods=['POST'], name='create context')
    def create(self, request,*args, **kwargs):
        inputs = tokenizer("The god of sun came to the earth to help the inca empire", return_tensors="pt")
        outputs = model(**inputs)


        context_data = request.data
        print("DATA obtenida de tu post: ", outputs)
        new_context = Contexto.objects.create(text_generated=context_data["text_generated"] + "Holi prro" )
        new_context.save()
        serializer = ContextoSerializer(new_context)
        return Response(serializer.data)
