from django.contrib import admin
from .models import Funcionario, Item, Lancamento

admin.site.register(Funcionario)
admin.site.register(Item)

@admin.register(Lancamento)
class LancamentoAdmin(admin.ModelAdmin):
    list_display = ('funcionario', 'data_hora', 'total')
    list_filter = ('data_hora', 'funcionario') # Filtro lateral de datas