from django.shortcuts import render

from .carro import Carro

from tienda.models import Producto

from django.shortcuts import redirect

from django.contrib import messages
# Create your views here.

def agregar_producto(request, producto_id):
    if request.user.is_authenticated:
        carro=Carro(request)

        producto=Producto.objects.get(id=producto_id)

        carro.agregar(producto=producto)

        return redirect("Tienda")
    else:
        messages.error(request, "Debes iniciar sesión para agregar productos al carrito.")
        return redirect("/login/login")


def eliminar_producto(request, producto_id):

    carro=Carro(request)

    producto=Producto.objects.get(id=producto_id)

    carro.eliminar(producto=producto)

    return redirect("Tienda")


def restar_producto(request, producto_id):

    carro=Carro(request)

    producto=Producto.objects.get(id=producto_id)

    carro.restar_producto(producto=producto)

    return redirect("Tienda")


def limpiar_carro(request):

    carro=Carro(request)

    carro.limpiar_carro()

    return redirect("Tienda")

def mostrar_carrito(request):
    carro = Carro(request)
    productos_en_carro = carro.get_productos()
    total_carro = carro.get_total()
    return render(request, 'carro/widget.html', {'productos_en_carro': productos_en_carro, 'total_carro': total_carro})
