# urls.py no aplicativo "pedido"
from django.urls import path
from . import views

urlpatterns = [
    path(
        "criar/", views.criar_pedido, name="criar_pedido"
    ),  # URL para criar um novo pedido
    path(
        "confirmacao/<int:pedido_id>/",
        views.confirmacao_pedido,
        name="confirmacao_pedido",
    ),  # Exemplo de definição de URL nomeada
    # Outras URLs relacionadas aos pedidos, se necessário
]
