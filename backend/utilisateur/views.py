from rest_framework.viewsets import ModelViewSet
from .models import Utilisateur, SleepTracker, Analyse
from .serializers import (
    UtilisateurSerializer,
    SleepTrackerSerializer,
    AnalyseSerializer
)

class UtilisateurViewSet(ModelViewSet):
    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer


class SleepTrackerViewSet(ModelViewSet):
    queryset = SleepTracker.objects.all()
    serializer_class = SleepTrackerSerializer


class AnalyseViewSet(ModelViewSet):
    queryset = Analyse.objects.all()
    serializer_class = AnalyseSerializer
