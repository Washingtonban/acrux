from django.contrib import admin
from .models import Evento

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'produto',
        'data_hora',
        # 'pessoa',
        'criacao',
        'atualizacao',
        'ativo'
    )
