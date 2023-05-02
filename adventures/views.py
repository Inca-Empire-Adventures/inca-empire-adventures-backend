from adventures.models import Adventures, Conversation
from adventures.promts import PROMT_MISION_PRINCIPAL_PLAYER, PROMT_OBTENCION_OPCIONES, PROMT_OBTENCION_RESUMEN, PROMT_PLAYER_CONTEXT, PROMT_RECORDAR_SISTEMA_D20, PROMT_SYSTEM_CONTEXT
from adventures.serializers import AdventureSerializer
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from characters.models import Character
from adventures.enums import RoleType
from rest_framework import status
from django.db.models import Q
import tiktoken
import json


import openai
import os

class AdventureViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Adventures.objects.all().order_by('id')
    serializer_class = AdventureSerializer

    def get_queryset(self):
        user = self.request.user
        # Obtener todos los character_detail que pertenecen al usuario
        queryset = Adventures.objects.filter(character__user=user)

        # Filtro opcional para buscar por nombre de character
        character_name = self.request.query_params.get('character_name')
        
        if character_name:
            queryset = queryset.filter(Q(character__user=user) & Q(character__characterName=character_name))
        return queryset

    def create(self, request, *args, **kwargs): 
        character = Character.objects.get(pk=request.data["character"])

        try:
            adventure = Adventures.objects.get(character=character)
        except Exception as e:
            adventure = None

        # Si tengo una aventura iniciada
        if adventure: 
            #Se obtiene la conversacion completa
            messages = self.obtener_conversacion_resumida(adventure)
            description = ""

            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                description = request.data["description"]

            #Validar envio de recordatorio de sistema d20
            recordar_sistema_d20 = self.validar_recordatorio_sistema_d20(adventure=adventure)
            if recordar_sistema_d20:
                description = description + PROMT_RECORDAR_SISTEMA_D20

            messages.append({
                "role": RoleType.USER,
                "content":  description
            })

            print("messages")
            print(json.dumps(messages))
            print("messages")


            total_tokens = self.obtener_cantidad_tokens(json.dumps(messages),"cl100k_base")
            print("total_tokens")
            print(total_tokens)
            print("total_tokens")

            if total_tokens >= 1500:
                resumen_completo = self.obtener_resumen(adventure)
                adventure.description = resumen_completo
                adventure.save()

                #Se crea una conversacion cn el nuevo resumen
                resumen_conversation = Conversation(adventure=adventure, role=RoleType.RESUME, content=resumen_completo )
                resumen_conversation.save()

            # Iniciar la conversación simulada con el modelo GPT-3.5-turbo
            response = self.obtener_response_chat_completion(messages=messages)

            # Obtener la respuesta del modelo y crear el objeto Adventure
            continuation_conversation = response.choices[0].message.content.replace("\n","");

            # Obtener lista de opciones
            options = self.obtener_opciones(continuation_conversation); 

            structure_response = {
                "description": continuation_conversation,
                "options": options
            }

            user_conversation = Conversation(adventure=adventure, role=RoleType.USER, content=description )
            user_conversation.save()
            
            assistant_conversation = Conversation(adventure=adventure, role=RoleType.ASSISTANT, content=continuation_conversation )
            assistant_conversation.save()

            #headers = self.get_success_headers(response.choices[0])
            
            return Response(structure_response, status=status.HTTP_201_CREATED)

        #Si estoy iniciando una aventura
        elif adventure == None: 
            messages, new_adventure = self.create_conversations(request, character)

            # Iniciar la conversación simulada con el modelo GPT-3.5-turbo
            response = self.obtener_response_chat_completion(messages=messages)

            # Obtener la respuesta del modelo y crear el objeto Adventure
            continuation_conversation = response.choices[0].message.content#.replace("\n","");

            assistant_conversation = Conversation(adventure=new_adventure, role=RoleType.ASSISTANT, content=continuation_conversation)
            assistant_conversation.save()
            
            # Obtener lista de opciones
            options = self.obtener_opciones(continuation_conversation); 

            structure_response = {
                "description": continuation_conversation,
                "options": options
            }

            headers = self.get_success_headers(response.choices[0])
            
            return Response(structure_response, status=status.HTTP_201_CREATED, headers=headers)
    
    def obtener_opciones(self, text):
        prompt_instrucction = text + PROMT_OBTENCION_OPCIONES;
        response = self.obtener_response_completion(prompt_instrucction)
        options = response.choices[0].text.replace("\n","").split('*') 

        return list(filter(bool, options))

    def create_conversations(self, request, character):
        # Obtener el mensaje inicial de la conversación
        description = ""
        
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            description = request.data["description"]

        #Obtener parrafo de estadisticas y etnia del personaje
        promt_user_statistics = self.obtener_promt_inicial(character);


        prompt_user = f"{PROMT_PLAYER_CONTEXT} {description} {PROMT_MISION_PRINCIPAL_PLAYER} Mis estadisticas son: {promt_user_statistics}"
        messages = [
            {"role": "system", "content": PROMT_SYSTEM_CONTEXT}, 
            {"role":"user", "content": prompt_user}
        ]

        new_adventure = Adventures(description=prompt_user, character=character)
        new_adventure.save()

        for message in messages:
            role = message["role"]
            content = message["content"]
            conversation = Conversation(adventure=new_adventure, role=role, content=content)
            conversation.save()

        return messages, new_adventure

    def obtener_promt_inicial(self, character):
        template_aventura_inicial = {
            "EstadisticasPersonaje": character.statistic.get_statistics_as_dict(),
            "ContextoGlobalActual": "Imperio incaico",
            "EtniaPersonaje": character.statistic.get_ethnicityType_display(),
            "NombrePersonaje": character.characterName
        }

        return f"template_aventura_inicial: { json.dumps(template_aventura_inicial) }"

    def obtener_cantidad_tokens(self, string: str, encoding_name: str) -> int:
        """Returns the number of tokens in a text string."""
        encoding = tiktoken.get_encoding(encoding_name)
        num_tokens = len(encoding.encode(string))
        return num_tokens
    
    def obtener_resumen(self, adventure):
        conversacion_completa = self.obtener_conversacion_resumida(adventure)

        prompt_instrucction = json.dumps(conversacion_completa) + PROMT_OBTENCION_RESUMEN
        
        response = self.obtener_response_completion(prompt_instrucction=prompt_instrucction)

        resumen = response.choices[0].text.replace("\n","").split('-') 

        return resumen
    
    def obtener_conversacion(self, adventure):
        conversations = Conversation.objects.filter(adventure=adventure)
        messages = []

        for message in conversations:
            messages.append({
                "role": message.role,
                "content": message.content
            })

        return messages
    
    def obtener_response_completion(self, prompt_instrucction, engine_model = "text-davinci-003" ):
        API_KEY = os.environ.get("API_KEY")
        openai.api_key = API_KEY # Coloca aquí tu propia API key

        return openai.Completion.create(
                engine=engine_model,
                prompt=prompt_instrucction,
                max_tokens=750,
                n=1,
                stop=None,
                temperature=0.1,
            )

    def obtener_response_chat_completion(self, messages, engine_model = "gpt-3.5-turbo"):
        API_KEY = os.environ.get("API_KEY")
        openai.api_key = API_KEY # API key
        
        return openai.ChatCompletion.create(
                model=engine_model,
                messages=messages,
                temperature=0.6,
                max_tokens=1000,
                n=1,
                stop=None,
                presence_penalty=0,
                frequency_penalty=0,
            )
        
    def obtener_conversacion_resumida(self, adventure):
        last_resume_conversation = Conversation.objects.filter(adventure=adventure, role=RoleType.RESUME).last()
        if last_resume_conversation is None:
            return self.obtener_conversacion(adventure)

        conversations =  Conversation.objects.filter(adventure=adventure, id__gt=last_resume_conversation.id)
        first_conversation =  Conversation.objects.get(id=1)


        messages = [
            {
                "role": RoleType.SYSTEM,
                "content": first_conversation.content
            },
            {
                "role": RoleType.USER,
                "content": f"El resumen de la historia es la siguiente: {last_resume_conversation.content}"
            },
            {
                "role": RoleType.ASSISTANT,
                "content": "Entendido, continuare la historia con el resumen"
            },
        ]

        for message in conversations:
            messages.append({
                "role": message.role,
                "content": message.content
            })

        return messages
    
    def validar_recordatorio_sistema_d20(self, adventure):
        ultimas_tres_respuestas = Conversation.objects.filter(adventure=adventure, role=RoleType.USER).order_by('-id')[:3]
        for respuesta in ultimas_tres_respuestas:
            if any(char.isdigit() for char in respuesta.content):
                return False
        return True