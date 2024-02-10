from django.urls import path

from .views import procesar_pedido

urlpatterns = [
   
  
    path('',procesar_pedido, name="procesar_pedido"),

]