from re import A
from django.urls import path
from .views import editar_trab, form_trab,home,Inicio_sesion,Dashboard,form_trab,list_trab,Listado_usuarios,Formulario_Usuario,eliminar_trab


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
    path ('form_trab/', form_trab, name='form_trab'),
    path ('listado-trabajador/', list_trab, name='listado-trabajador'),
    path ('editar_trabajador/<id>/', editar_trab, name='editar_trabajador'),
    path ('eliminar_trabajador/<id>/', eliminar_trab, name='eliminar_trabajador'),


]