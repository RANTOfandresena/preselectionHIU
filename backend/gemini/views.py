from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

from gemini import tools
from utilisateur.models import Utilisateur
load_dotenv()


@api_view(['POST'])
@permission_classes([AllowAny]) # Change en IsAuthenticated pour la production
def ai_agent_planner(request):
    user_prompt = request.data.get('contents')
    client = genai.Client(api_key=os.environ.get("GOOGLE_API_KEY"))

    # Instruction système stricte pour guider l'agent
    sys_instr = """
    Tu es un assistant de santé intelligent. Ton rôle est de créer des tâches de santé 
    dans le planning de l'utilisateur en utilisant l'outil 'create_planned_task'. 
    Analyse le temps libre et suggère des activités (sport, hydratation, repos).
    """

    # Appel Gemini avec les outils activés
    response = client.models.generate_content(
        model='gemini-3-flash-preview',
        contents=user_prompt,
        config=types.GenerateContentConfig(
            system_instruction=sys_instr,
            tools=tools.tools,  # <--- Ajoute .tools pour accéder à la LISTE dans le module
        )
    )

    # Extraction de l'appel de fonction
    function_call = None
    if response.candidates[0].content.parts:
        for part in response.candidates[0].content.parts:
            if part.function_call:
                function_call = part.function_call

    if function_call:
        # L'IA a décidé de créer une tâche !
        # On récupère les arguments générés par l'IA
        args = function_call.args
        
        # Ici, on enregistre REELLEMENT dans la base de données Django
        from .models import AIPlannedTask
        task = AIPlannedTask.objects.create(
            user = Utilisateur(id=1),# user=request.user,
            title=args['title'],
            start_time=args['start_time'],
            end_time=args['end_time'],
            category=args['category'],
            priority=args.get('priority', 2),
            description=args.get('description', ''),
            ai_generated=True
        )

        return Response({
            'message': "L'IA a planifié une nouvelle activité.",
            'task_id': task.id,
            'details': args
        })

    return Response({
        'text': response.text,
        'message': "L'IA n'a pas jugé nécessaire de planifier une tâche."
    })