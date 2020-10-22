from rest_framework import serializers
from .models import Empresa


class EmpresaSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'email': {'write_only': True},
            'telefone': {'write_only': True}
        }
        model = Empresa
        fields = (
            'id',
            'cnpj',
            'nome',
            'email',
            'telefone',
            'grupo',
            'criacao',
            'atualizacao',
            'ativo'
        )