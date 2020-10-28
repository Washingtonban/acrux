from django.db import models
from phone_field import PhoneField
from django_enumfield import enum

from empresas.models import Empresa


class Base(models.Model):
    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True

class Produto(Base):
    upload_location = '../media/'
    nome = models.CharField(max_length=255)
    preco = models.FloatField(max_length=255)
    imagem = models.ImageField(upload_to=upload_location,
                               null=True,
                               blank=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome