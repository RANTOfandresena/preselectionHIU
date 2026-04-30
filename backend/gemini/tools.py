# ai_planner/tools.py (ou dans ton views.py)

def create_planned_task(title: str, start_time: str, end_time: str, category: str, priority: int, description: str = ""):
    """
    Crée une nouvelle tâche dans le planning de l'utilisateur.
    Les dates doivent être au format ISO (YYYY-MM-DDTHH:MM:SSZ).
    """
    # Cette fonction sera appelée par l'IA via Gemini
    # Elle retourne un dictionnaire que l'IA peut interpréter
    return {
        "status": "success",
        "data": {
            "title": title,
            "start_time": start_time,
            "end_time": end_time,
            "category": category,
            "priority": priority,
            "description": description
        }
    }

# On déclare l'outil pour Gemini
tools = [create_planned_task]