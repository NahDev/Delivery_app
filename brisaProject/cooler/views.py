# views.py em sua aplicação "cooler"
from django.shortcuts import render, get_object_or_404
from .models import Cooler
from django.contrib.auth.decorators import login_required

@login_required
def lista_coolers(request):
    coolers = Cooler.objects.all()
    return render(request, "cooler/lista_coolers.html", {"coolers": coolers})

@login_required
def detalhes_cooler(request, cooler_id):
    cooler = get_object_or_404(Cooler, pk=cooler_id)
    return render(request, "cooler/detalhes_cooler.html", {"cooler": cooler})

@login_required
def home_cliente(request):
    coolers = Cooler.objects.all()
    return render(request, "clientes/home_cliente.html", {"coolers": coolers})
