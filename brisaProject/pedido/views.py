# views.py no aplicativo "pedido"
from django.shortcuts import render, redirect, get_object_or_404
from .models import Pedido
from .forms import PedidoForm, LocalizacaoForm

from django.contrib.auth.decorators import login_required


@login_required
def criar_pedido(request):
    if request.method == "POST":
        form = PedidoForm(request.POST)
        localizacao_form = LocalizacaoForm(request.POST)

        if form.is_valid() and localizacao_form.is_valid():
            pedido = form.save(commit=False)
            pedido.cliente = request.user
            pedido.save()

            # Salvar as coordenadas de localização
            latitude = localizacao_form.cleaned_data["latitude"]
            longitude = localizacao_form.cleaned_data["longitude"]
            pedido.latitude = latitude
            pedido.longitude = longitude
            pedido.save()

            return redirect(
                "confirmacao_pedido", pedido_id=pedido.id
            )  # Redirecionar para a página de confirmação

    else:
        form = PedidoForm()
        localizacao_form = LocalizacaoForm()

    return render(
        request,
        "pedido/criar_pedido.html",
        {"form": form, "localizacao_form": localizacao_form},
    )


@login_required
def confirmacao_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    total = pedido.calcular_total()

    return render(request, "pedido/confirmacao_pedido.html", {'pedido': pedido, 'total': total})
