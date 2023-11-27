from django.urls import path
from . import views

urlpatterns = [
    # Outras URLs do seu aplicativo
    path("home_cliente/", views.home_cliente, name="home_cliente"),
]
