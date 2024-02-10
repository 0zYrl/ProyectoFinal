from django.contrib import admin

from .models import Pedido, LineasPedido

# Register your models here.


class PedidoAdmin(admin.ModelAdmin):

    readonly_fields=("created","updated")

class LineaAdmin(admin.ModelAdmin):

    readonly_fields=("created","updated")



admin.site.register(Pedido)
admin.site.register(LineasPedido)