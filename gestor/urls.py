from django.urls import path, include

from .views import editar_trab,form_trab,home,Inicio_sesion,Dashboard,\
    list_trab,form_usuario,eliminar_trab, list_centro, form_centr,\
    editar_cent,eliminar_centr,list_usuarios,eliminar_usuario,Profview,editar_usuario
from rest_framework import routers



router = routers.DefaultRouter()
router.register('profesion', Profview)


urlpatterns = [

    #-------- API ---------
    path('api/',include(router.urls)),
    #-------- Inicial ---------
    path ('', home, name='home'),
    path ('Inicio_sesion/', Inicio_sesion, name='Inicio_sesion'),
    path ('Dashboard/', Dashboard, name='Dashboard'),
    #-------- Usuarios --------
    path ('Listado_usuarios/', list_usuarios, name='list_usua'),
    path ('Formulario_Usuario/', form_usuario, name='form_Usuario'),
    path ('Editar_usuario/<id>/', editar_usuario, name='edit_usuario'),
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