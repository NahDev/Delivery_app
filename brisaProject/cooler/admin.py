from django.contrib import admin
from .models import Cooler


# Registre os modelos Cooler, Bebida e ItemCooler para que possam ser gerenciados no painel de administração
@admin.register(Cooler)
class CoolerAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'preco')  # Adicione 'id' à lista de campos para exibir
    list_filter = ("nome",)
    search_fields = ("nome",)



