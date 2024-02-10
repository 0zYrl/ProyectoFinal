from django.shortcuts import render
from .models import Producto
from carro.carro import Carro


def tienda(request):
    productos = Producto.objects.all()
    carro = Carro(request)

    return render(request, "tienda/tienda.html", {"productos": productos, "carro": carro})