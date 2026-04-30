from rest_framework import serializers
from .models import Utilisateur, SleepTracker, Analyse


class UtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = '__all__'


class SleepTrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SleepTracker
        fields = '__all__'


class AnalyseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Analyse
        fields = '__all__'