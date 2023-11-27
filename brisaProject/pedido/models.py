from django.db import models
from django.conf import settings
from cooler.models import Cooler
from bebida.models import Bebida


class Pedido(models.Model):
    cliente = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cooler = models.ForeignKey(Cooler, on_delete=models.CASCADE)
    descricao = models.TextField(
        blank=True,
        max_length=1000,
    )
    quantidade = models.PositiveIntegerField(default=1)
    data_pedido = models.DateTimeField(auto_now_add=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    coordenadas = models.CharField(
        max_length=50, null=True, blank=True
    )  # Campo para armazenar as coordenadas

    status_entrega = models.CharField(
        max_length=20,
        choices=[
            ("em_andamento", "Em Andamento"),
            ("entregue", "Entregue"),
            ("atrasado", "Atrasado"),
            # Adicione outros status de entrega conforme necessário
        ],
        default="em_andamento",
    )
    status_pagamento = models.CharField(
        max_length=20,
        choices=[
            ("pago", "Pago"),
            ("em_aberto", "Em Aberto"),
            ("atrasado", "Atrasado"),
            # Adicione outros status de pagamento conforme necessário
        ],
        default="em_aberto",
    )
    preco_cooler = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )

    def save(self, *args, **kwargs):
        if self.latitude is not None and self.longitude is not None:
            self.coordenadas = f"{self.latitude}, {self.longitude}"

        if self.cooler and self.quantidade:
            self.preco_cooler = self.cooler.preco * self.quantidade
        else:
            self.preco_cooler = None

        super(Pedido, self).save(*args, **kwargs)

    def calcular_total(self):
        if self.cooler and self.quantidade:
            return self.cooler.preco * self.quantidade
        return 0.0  # Ou qualquer valor padrão desejado se o cooler ou quantidade não estiverem definidos

    def __str__(self):
        return f"Pedido de {self.cliente.username} para {self.cooler.nome}"
