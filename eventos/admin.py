from django.contrib import admin
from .models import Evento

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'Produto',
                    'data_hora',
                    'Pessoa',
                    'criacao',
                    'atualizacao',
                    'ativo')
