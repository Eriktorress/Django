from django.urls import URLPattern, path
from . import views

URLPattern = [
    path('', views.usuario_list, name= 'usuario_list'),
]