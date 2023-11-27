from django import forms
from .models import Cooler


# Se você desejar criar um formulário personalizado para a criação de coolers
class CoolerForm(forms.ModelForm):
    class Meta:
        model = Cooler
        fields = ["nome", "preco", "descricao", "fotos", "bebidas", "itens_cooler"]

    # Se desejar personalizar a validação ou adicionar widgets, você pode fazê-lo aqui
