from django.contrib import admin
from .models import ItemCooler  # Importe o modelo ItemCooler


class ItemCoolerAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "cooler_id",
        "bebida",
        "quantidade",
    )  # Adicione 'cooler_id' à lista de campos para exibir


# Registre o modelo ItemCooler com a classe ItemCoolerAdmin personalizada
admin.site.register(ItemCooler, ItemCoolerAdmin)
