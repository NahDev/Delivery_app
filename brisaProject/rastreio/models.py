# models.py no aplicativo "rastreio"
from django.db import models
from bebida.models import Bebida


class ItemCooler(models.Model):
    cooler = models.ForeignKey(
        "cooler.Cooler", on_delete=models.CASCADE
    )  # Importe o modelo Cooler após a definição do ItemCooler
    bebida = models.ForeignKey(Bebida, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.cooler.nome} - {self.bebida.nome}"
