from django.http import JsonResponse
from google import genai

client = genai.Client()

def ask_gemini(request):
    prompt = request.GET.get("q", "Explain how AI works in a few words")

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt,
    )

    return JsonResponse({
        "prompt": prompt,
        "response": response.text
    })