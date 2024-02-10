from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import View
from django.contrib import messages
from .forms import CustomUserCreationForm

class VRegistro(View):
    def get(self,request):
        form = CustomUserCreationForm()
        return render(request, "registro/registro.html", {"form": form})

    def post(self,request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('home')
        else:
            return render(request, "registro/registro.html", {"form": form})

def cerrar_session(request):
    logout(request)
    return redirect('home')



class VInicioSesion(View):

    def get(self, request):
        form = AuthenticationForm()
        return render(request, "login/login.html", {"form": form})

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.get_user()
            login(request, usuario)
            return redirect('home')
    
        else:
            return render(request, "login/login.html", {"form": form})