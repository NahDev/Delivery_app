from django.contrib import admin
from .models import Pedido
from django.utils import timezone


class PedidoAdmin(admin.ModelAdmin):
    list_display = (
        "cliente",
        "cooler",
        "quantidade",
        "calcular_total",
        "tempo_decorrido",
        "status_entrega",
        "status_pagamento",
        "latitude",
        "longitude",
    )

    def calcular_total(self, obj):
        if obj.cooler:  # Verifica se o pedido tem um cooler associado
            return obj.quantidade * obj.cooler.preco
        return (
            0  # Ou qualquer outro valor padrão desejado se não houver cooler associado
        )

    calcular_total.short_description = "Total"

    def tempo_decorrido(self, obj):
        agora = timezone.now()
        tempo_passado = agora - obj.data_pedido
        return str(tempo_passado)

    tempo_decorrido.short_description = "Tempo Decorrido"

    ordering = ("data_pedido",)  # Ordenar os pedidos pelo campo 'data_pedido'


# Registre o modelo Pedido com a classe PedidoAdmin personalizada
admin.site.register(Pedido, PedidoAdmin)
