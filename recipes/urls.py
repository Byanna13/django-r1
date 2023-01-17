# from django.contrib import admin
from django.urls import path
from recipes.views import home, newpag, part

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('home/', home, name="home"),
    path('newpag/', newpag, name='newpag'),
    path('part/', part, name='part'),
    # path('sobre/', sobre),
    # path('contato/', contato),
]
