# forms.py no aplicativo "pedido"
from django import forms
from .models import Pedido


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = [
            "cooler",
            "quantidade",
            "descricao",
        ]


# Adicione a nova classe para capturar as coordenadas de localização
class LocalizacaoForm(forms.Form):
    latitude = forms.FloatField(widget=forms.HiddenInput())
    longitude = forms.FloatField(widget=forms.HiddenInput())
