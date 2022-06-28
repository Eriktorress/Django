from re import A
from django.urls import path
from . import views
from . views import agregar_trabajador, home


urlpatterns = [
    #path ('', views.list_trab, name='list_trab'),
    path ('', home, name='home'),
    path ('agregar-trabajador/', agregar_trabajador, name='agregar_trabajador'),

]