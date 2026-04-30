from django.urls import path
from .views import ai_agent_planner

urlpatterns = [
    path("", ai_agent_planner, name="ask_gemini"),
]