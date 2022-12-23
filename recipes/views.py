from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html')

def sobre(request):
    return HttpResponse('<h1>SOBRE - Django</h1>')

def contato(request):
    return HttpResponse('<h1>CONTATO - Django</h1>')