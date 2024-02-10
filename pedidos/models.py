from django.db import models

from django.contrib.auth import get_user_model

from tienda.models import Producto

from django.db.models import F, Sum, FloatField

# Create your models here.

User=get_user_model()

class Pedido(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.id)
    
    @property
    def total(self):
        return self.lineapedido.set.aggregate(


        total=Sum(F("precio")*F("cantidad"), output_field=FloatField())


    )["total"]

    class meta:
        db_table="pedidos"
        verbose_name="pedido"
        verbose_name_plura="pedidos"
        ordereing=['id']

class LineasPedido(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    producto=models.ForeignKey(Producto, on_delete=models.CASCADE)
    pedido=models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad=models.IntegerField(default=1)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.cantidad} unidades de {self.producto.name}'

    class meta:
        db_table="LineaPedidos"
        verbose_name="Linea pedido"
        verbose_name_plura="Lineas pedidos"
        ordereing=['id']