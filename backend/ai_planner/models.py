from django.db import models

from django.conf import settings
class AIPlannedTask(models.Model):
    PRIORITY_CHOICES = [
        (1, 'Basse'),
        (2, 'Moyenne'),
        (3, 'Haute'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    
    # Données temporelles pour l'IA
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    duration_minutes = models.PositiveIntegerField(help_text="Calculé par l'IA")
    
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=2)
    category = models.CharField(max_length=100, )
    
    # Suivi
    is_completed = models.BooleanField(default=False)
    ai_generated = models.BooleanField(default=True) # Pour distinguer les tâches IA
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['start_time']

    def __str__(self):
        return f"{self.title} - {self.start_time.strftime('%H:%M')}"