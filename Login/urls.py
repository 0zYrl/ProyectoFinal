from django.urls import path

from .views import VRegistro, cerrar_session, VInicioSesion

urlpatterns = [
   
  
    path('',VRegistro.as_view(), name="registro"),
    path('cerrar',cerrar_session, name="cerrar"),
    path('login/',VInicioSesion.as_view(), name="login"),
]