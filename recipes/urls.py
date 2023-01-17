# from django.contrib import admin
from django.urls import path
from recipes.views import home, newpag, sobre, contato

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', home),
    path('newpag/', newpag, name='newpag'),
    path('sobre/', sobre),
    path('contato/', contato),
]
