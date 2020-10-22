from django.db import models
from phone_field import PhoneField
from django_enumfield import enum

import pessoa


class Base(models.Model):
    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True


class AtributoEmpresa(enum.Enum):
    EMPRESA = 1
    CLIENTE = 2


class Empresa(Base):
    cnpj = models.IntegerField()
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    telefone = models.IntegerField()
    grupo = enum.EnumField(AtributoEmpresa)
    # vendedor = models.OneToOneField(pessoa, on_delete=models.CASCADE)
    # usuario = models.OneToOneField(pessoa, on_delete=models.CASCADE)

    # cliente = models.OneToOneField(empresa, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

