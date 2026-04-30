from django.db import models
from django.contrib.auth.models import AbstractUser

# USER PRINCIPAL
class Utilisateur(AbstractUser):
    GENRE_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female')
    ]
    
    poids = models.FloatField(null=True, blank=True)
    taille = models.FloatField(null=True, blank=True)
    genre = models.CharField(max_length=1, choices=GENRE_CHOICES, null=True, blank=True)

    def __str__(self):
        return self.username


# SUIVI DU SOMMEIL (1 user → plusieurs jours)
class SleepTracker(models.Model):
    user = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    heures_sommeil = models.FloatField()

    def __str__(self):
        return f"{self.user.username} - {self.date}"


# ANALYSE MEDICALE (JSON flexible)
class Analyse(models.Model):
    user = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    type_analyse = models.CharField(max_length=100)
    fichier_json = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.type_analyse}"

# Create your models here.
