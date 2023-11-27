from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.contrib import admin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    list_display = ("username", "email", "telefone", "is_staff", "is_superuser")
    list_filter = ("is_staff", "is_superuser")
    search_fields = ("username", "email")
    ordering = ("username",)


# Verificar se o modelo CustomUser já está registrado
if not admin.site.is_registered(CustomUser):
    admin.site.register(CustomUser, CustomUserAdmin)
