from rest_framework import serializers
from .models import AIPlannedTask

class AIPlannedTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = AIPlannedTask
        fields = '__all__'
        read_only_fields = ['user', 'created_at']

    def validate(self, data):
        if data['start_time'] >= data['end_time']:
            raise serializers.ValidationError("L'heure de fin doit être après l'heure de début.")
        return data