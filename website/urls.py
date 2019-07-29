from django.urls import path, include
from website.views import index, lista, login, cadastrar_ideia

urlpatterns = [
    path('', index),
    path('lista', lista),
    path('login', login),
    path('ideias', cadastrar_ideia)
]
