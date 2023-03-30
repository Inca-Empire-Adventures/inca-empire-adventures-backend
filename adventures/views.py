from rest_framework import viewsets
from adventures.enums import RoleType
from adventures.models import Adventures, Conversation
from rest_framework import status
from adventures.serializers import AdventureSerializer
from rest_framework.response import Response
import openai
import os
from characters.models import Character

from inca_empire_adventures_backend.constants import ID_USER_CHARACTER, USER_SESION

# Create your views here.
class AdventureViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows adventures to be viewed or edited.
    """
    queryset = Adventures.objects.all().order_by('id')
    serializer_class = AdventureSerializer

    def create(self, request, *args, **kwargs):
        API_KEY = os.environ.get("API_KEY")
        
        character = Character.objects.get(pk=ID_USER_CHARACTER)

        try:
            adventure = Adventures.objects.get(character=character)
        except Exception as e:
            adventure = None

        if adventure: 
            conversations = Conversation.objects.filter(adventure=adventure)

            messages = [
                {'role': 'system', 'content': 'Hola soy tu dungeon master ¿Como te gustaria iniciar la historia?'}, 
                {'role': 'assistant', 'content': 'Bueno mi nombre es SirPlayer y me encuentro en la epoca del Imperio incaico, Estoy en ayacucho, en la puna del Imperio incaico.'}, 
                {'role': 'assistant', 'content': 'Entrar en la cueva'}, 
                {'role': 'system', 'content': 'Perfecto, SirPlayer. Te encuentras en Ayacucho, una región de la puna del Imperio Incaico, rodeado por altas montañas y extensos campos verdes. Eres un guerrero Inca entrenado en el arte de la guerra y la caza, y has sido enviado en una misión especial por el emperador para investigar los rumores de una tribu hostil que ha estado atacando a las aldeas cercanas.Mientras te adentras en las montañas, escuchas un ruido extraño que viene de detrás de una roca grande. ¿Qué haces?'}]

            for message in conversations:
                messages.append({
                    "role": message.role,
                    "content": message.content
                })

            print("--------------------------:", adventure)
            print("--------------------------")
            print("--------------------------: ", messages)
            print("--------------------------")

            # Iniciar la conversación simulada con el modelo GPT-3.5-turbo
            openai.api_key = API_KEY # Coloca aquí tu propia API key
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages,
                temperature=0.6,
                max_tokens=750,
                n=1,
                stop=None,
                presence_penalty=0.4,
                frequency_penalty=0.4,
            )

            # Obtener la respuesta del modelo y crear el objeto Adventure
            continuation_conversation = response.choices[0].message.content.replace("\n","");

            # Obtener lista de opciones
            options = self.obtener_opciones(continuation_conversation); 

            structure_response = {
                "description": continuation_conversation,
                "options": options
            }

            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                description = request.data["description"]

            assistant_conversation = Conversation(adventure=adventure, role=RoleType.ASSISTANT, content=description )
            assistant_conversation.save()
            
            system_conversation = Conversation(adventure=adventure, role=RoleType.SYSTEM, content=continuation_conversation )
            system_conversation.save()

            #headers = self.get_success_headers(response.choices[0])
            
            return Response(structure_response, status=status.HTTP_201_CREATED)

        elif adventure == None: 
            messages, new_adventure = self.create_conversations(request, character)

            # Iniciar la conversación simulada con el modelo GPT-3.5-turbo
            openai.api_key = API_KEY # Coloca aquí tu propia API key
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages,
                temperature=0.6,
                max_tokens=750,
                n=1,
                stop=None,
                presence_penalty=0.4,
                frequency_penalty=0.4,
            )

            # Obtener la respuesta del modelo y crear el objeto Adventure
            continuation_conversation = response.choices[0].message.content.replace("\n","");

            system_conversation = Conversation(adventure=new_adventure, role=RoleType.SYSTEM, content=continuation_conversation)
            system_conversation.save()
            
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
            max_tokens=500,
            n=1,
            stop=None,
            temperature=0.5,
        )
        options = response.choices[0].text.replace("\n","").split('-') 

        return list(filter(bool, options))


    def create_conversations(self, request, character):
        # Obtener el mensaje inicial de la conversación
        prompt_system = "Hola soy tu dungeon master ¿Como te gustaria iniciar la historia?"

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            description = request.data["description"]

        #TODO obtener el nombre del jugador - Validar si es el inicio de la historia
        prompt_user = f"Bueno mi nombre es {USER_SESION} y me encuentro en la epoca del Imperio incaico, {description}"
        messages = [
            {"role": "system", "content": prompt_system}, 
            {"role":"assistant", "content": prompt_user}
        ]

        new_adventure = Adventures(description=prompt_user, character=character)
        new_adventure.save()

        for message in messages:
            role = message["role"]
            content = message["content"]
            conversation = Conversation(adventure=new_adventure, role=role, content=content)
            conversation.save()

        return messages, new_adventure