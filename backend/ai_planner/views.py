from rest_framework import viewsets, permissions
from .models import AIPlannedTask
from .serializers import AIPlannedTaskSerializer
from django.utils.dateparse import parse_date

class AIPlannerViewSet(viewsets.ModelViewSet):
    serializer_class = AIPlannedTaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = AIPlannedTask.objects.filter(user=self.request.user)
        # Permet de filtrer par date via l'URL : /api/planner/?date=2026-04-30
        date_param = self.request.query_params.get('date')
        if date_param:
            queryset = queryset.filter(start_time__date=parse_date(date_param))
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)