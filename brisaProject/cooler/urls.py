# urls.py em sua aplicação "cooler"
from django.urls import path
from . import views

urlpatterns = [
    path("", views.lista_coolers, name="lista_coolers"),
    path("<int:cooler_id>/", views.detalhes_cooler, name="detalhes_cooler"),
]
