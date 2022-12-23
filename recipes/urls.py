from struct import pack
from django.urls import path
from recipes.views import home, sobre, contato, teste

urlpatterns = [
    path('', home),
    path('sobre/', sobre),
    path('contato/', contato),
    path('teste/', teste),
]
