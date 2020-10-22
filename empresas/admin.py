from django.contrib import admin
from .models import Empresa

@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'cnpj',
                    'nome',
                    'email',
                    'telefone',
                    'grupo',
                    'criacao',
                    'atualizacao',
                    'ativo')
