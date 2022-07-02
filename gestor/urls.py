from re import A
from django.db import router
from django.urls import path

from gestor.models import Profesion
from .views import editar_trab,form_trab,home,Inicio_sesion,Dashboard,\
    list_trab,form_usuario,eliminar_trab, list_centro, form_centr,\
    editar_cent,eliminar_centr,list_usuarios,eliminar_usuario,Profview
from rest_framework import routers


urlpatterns = [


    #-------- Inicial ---------
    path ('', home, name='home'),
    path ('Inicio_sesion/', Inicio_sesion, name='Inicio_sesion'),
    path ('Dashboard/', Dashboard, name='Dashboard'),
    #-------- Usuarios --------
    path ('Listado_usuarios/', list_usuarios, name='list_usua'),
    path ('Formulario_Usuario/', form_usuario, name='form_Usuario'),
    path ('Eliminar_usuario/<id>/', eliminar_usuario, name='elim_usuario'),
    #-------- Trabajadores------
    path ('Formulario_trabajador/', form_trab, name='form_trab'),
    path ('Listado-trabajador/', list_trab, name='listado-trabajador'),
    path ('Editar_trabajador/<id>/', editar_trab, name='edit_trab'),
    path ('Eliminar_trabajador/<id>/', eliminar_trab, name='eliminar_trabajador'),
    #-------- Centros ----------
    path ('Listado_centros/', list_centro, name='list_centr'),
    path ('Formulario_centro/', form_centr, name='form_centr'),
    path ('Editar_centro/<id>/', editar_cent, name='edit_centr'),
    path ('Eliminar_centro/<id>/', eliminar_centr, name='elim_centr'),
]