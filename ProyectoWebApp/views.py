from django.shortcuts import render, HttpResponse




# Create your views here.

def home(request):
      if 'carro' not in request.session:
         request.session['carro'] = {}
      return render(request, "ProyectoWebApp/home.html")