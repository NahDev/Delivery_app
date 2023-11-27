from django import forms
from .models import Bebida


class BebidaFrom(forms.ModelForm):
    class Meta:
        model = Bebida
        fields = ["nome", "marca"]
