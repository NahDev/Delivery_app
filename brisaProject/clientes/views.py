from django.urls import reverse
from django.shortcuts import redirect, render


# Renomeie sua view atual para incorporar o nome do aplicativo
def home_app_atual(request):
    # Construa a URL com base no nome da visualização 'home_cliente'
    url_home_cliente = reverse("home_cliente")

    # Redirecione para a URL construída
    return redirect(url_home_cliente)


# Crie uma nova função de view chamada home_cliente que chama a view do aplicativo "clientes"
def home_cliente(request):
    return render(request, "clientes/home_cliente.html")
