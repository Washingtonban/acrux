from rest_framework import serializers
from .models import Pessoa


class PessoaSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'email': {'write_only': True},
            'telefone': {'write_only': True}
        }
        model = Pessoa
        fields = (
            'id',
            'cpf',
            'nome',
            'email',
            'telefone',
            'grupo',
            'usuario',
            'criacao',
            'atualizacao',
            'ativo'
        )