from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from google import genai
from google.genai import types
import os
from dotenv import load_dotenv
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
load_dotenv()

@swagger_auto_schema(
    method='post',
    operation_description="Génère du contenu avec Gemini AI",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'contents': openapi.Schema(type=openapi.TYPE_STRING, description='Prompt principal')
        },
        required=[]
    ),
    responses={
        200: openapi.Response(
            description="Réponse IA générée",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'text': openapi.Schema(type=openapi.TYPE_STRING),
                    'contents': openapi.Schema(type=openapi.TYPE_STRING),
                }
            )
        )
    }
)
@api_view(['POST'])
@permission_classes([AllowAny])
def generate_content(request):
    prompt = request.data.get('contents') or request.data.get('prompt')

    client = genai.Client(api_key=os.environ.get("GOOGLE_API_KEY"))
    response = client.models.generate_content(
        model='gemini-3-flash-preview',
        contents=prompt,
        config=types.GenerateContentConfig(
            system_instruction="Tu es un expert en informatique. Réponds brièvement."
        )
    )

    return Response({
        'text': getattr(response, 'text', None) or response,
        'contents': prompt,
    })
