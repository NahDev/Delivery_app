# models.py em seu aplicativo "bebida"
from django.db import models


class Bebida(models.Model):
    nome = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    quantidade = models.PositiveIntegerField(
        default=0
    )  # Adicione um campo para rastrear a quantidade em estoque

    def __str__(self):
        return self.nome
