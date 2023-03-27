from rest_framework import viewsets
from adventures.models import Adventures
from rest_framework import status
from adventures.serializers import AdventureSerializer
from rest_framework.response import Response
import openai
import os

from inca_empire_adventures_backend.constants import USER_SESION

# Create your views here.
class AdventureViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows adventures to be viewed or edited.
    """
    queryset = Adventures.objects.all().order_by('id')
    serializer_class = AdventureSerializer

    def create(self, request, *args, **kwargs):
        API_KEY = os.environ.get("API_KEY")
        # Obtener el mensaje inicial de la conversación
        prompt_system = f"Hola soy tu dungeon master ¿Como te gustaria iniciar la historia?"

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            description = request.data["description"]

        #TODO obtener el nombre del jugador - Validar si es el inicio de la historia
        prompt_user = f"Bueno mi nombre es {USER_SESION} y me encuentro en la empoca del Imperio incaico, {description}"
        messages = [
            {"role": "system", "content": prompt_system}, 
            {"role":"assistant", "content": prompt_user}
        ]

        # Iniciar la conversación simulada con el modelo GPT-3.5-turbo
        openai.api_key = API_KEY # Coloca aquí tu propia API key
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.7,
            max_tokens=1024,
            n=1,
            stop=None,
            presence_penalty=0.6,
            frequency_penalty=0.6,
        )

        # Obtener la respuesta del modelo y crear el objeto Adventure
        continuation_conversation = response.choices[0].message.content.replace("\n","");

        # Obtener lista de opciones
        options = self.obtener_opciones(continuation_conversation); 

        structure_response = {
            "description": continuation_conversation,
            "options": options
        }

        headers = self.get_success_headers(response.choices[0])
        return Response(structure_response, status=status.HTTP_201_CREATED, headers=headers)
    
    def obtener_opciones(self, text):
        prompt_instrucction = text + ". Del parrafo anterior ¿Puedes darme una lista de las opciones mencionadas separado por guiones ? ";
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt_instrucction,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.7,
        )
        options = response.choices[0].text.replace("\n","").split('-') 

        return list(filter(bool, options))
