from rest_framework import serializers
from .models import Produto
from .models import Empresa


class ProdutoSerializer(serializers.ModelSerializer):

    # imagem = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = Produto
        fields = (
            'id',
            'nome',
            'preco',
            'imagem',
            'criacao',
            'atualizacao',
            'empresa',
            'ativo'
        )