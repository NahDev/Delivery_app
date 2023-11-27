from django.contrib import admin
from .models import Bebida
# Register your models here.
@admin.register(Bebida)
class BebidaAdmin(admin.ModelAdmin):
    list_display = (
        "nome",
        "quantidade",
    )  # Exibe o campo quantidade no painel de administração
    list_filter = ("nome",)
    search_fields = ("nome",)