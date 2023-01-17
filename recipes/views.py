# from urllib import request
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


# Comando para execultar: py .\manage.py runserver
# Abrir no navegador: localhost:8000

# Create your views here.

# def home(request):
#      return render(request, 'home.html')

def home(request):
    return render(request,'recipes/pages/home.html', context={'name': 'Fabiana Souza'})

def newpag(request):
    return render(request,'recipes/pages/newpag.html', context={'name': 'Fabiana Souza'})

# def home(request):
#     return render(request,'recipes/pages/home.html')


def sobre(request):
    return HttpResponse('<h1>SOBRE - Django</h1>')

def contato(request):
    return HttpResponse('<h1>CONTATO - Django</h1>')