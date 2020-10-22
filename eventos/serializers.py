from rest_framework import serializers
from .models import Evento


class EventoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Evento
        fields = (
            'id',
            'produto',
            'data_hora',
            'funcionarios',
            'criacao',
            'atualizacao',
            'ativo'
        )