from django.db import models
from phone_field import PhoneField
from django_enumfield import enum

from produtos.models import Produto

from pessoa.models import Pessoa


class Base(models.Model):
    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Produto(Produto):
    pass

class Pessoa(Pessoa):
    pass


class Evento(Base):
    data_hora = models.DateTimeField()
    Produto = models.ForeignKey("Produto", on_delete=models.CASCADE, related_name='Evento')
    Pessoa = models.ForeignKey("Pessoa", on_delete=models.CASCADE, related_name='Evento')
