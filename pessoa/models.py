from django.db import models
from phone_field import PhoneField
from django_enumfield import enum
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.timezone import timezone

class Base(models.Model):
    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True

class AtributoPessoa(enum.Enum):
    ADMIN = 1
    VENDEDOR = 2
    CLIENTE = 3
    EMPRESA = 4
    ENTREGADOR = 5
    FUNCIONARIO = 6

class Pessoa(Base):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = models.IntegerField()
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    telefone = models.IntegerField()
    grupo = enum.EnumField(AtributoPessoa)


    def __str__(self):
        return self.nome


