from django.db import models
from bebida.models import (
    Bebida,
)  # Importe o modelo ItemCooler do aplicativo "rastreio"


class Cooler(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField()
    fotos = models.ImageField(upload_to="coolers")
    itens_cooler = models.ManyToManyField(
        Bebida, related_name="itens"
    )  # Defina o related_name como 'itens'

    def __str__(self):
        return self.nome
