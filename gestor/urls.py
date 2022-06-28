from re import A
from django.urls import path
from .views import home,Inicio_sesion,Dashboard,agregar_trabajador,list_trab,Listado_usuarios,Formulario_Usuario


urlpatterns = [
    #path ('', views.list_trab, name='list_trab'),
    #INICIAL
    path ('', home, name='home'),
    path ('Inicio_sesion/', Inicio_sesion, name='Inicio_sesion'),
    path ('Dashboard/', Dashboard, name='Dashboard'),
    #USUARIO
    path ('Listado_usuarios/', Listado_usuarios, name='Listado_usuarios'),
    path ('Formulario_Usuario/', Formulario_Usuario, name='Formulario_Usuario'),
    #TRABAJADOR
    path ('agregar-trabajador/', agregar_trabajador, name='agregar_trabajador'),
    path ('listado-trabajador/', list_trab, name='listado-trabajador')


]