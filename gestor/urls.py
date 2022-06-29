from re import A
from django.urls import path
from .views import editar_trab, form_trab,home,Inicio_sesion,Dashboard,list_trab,Listado_usuarios,Formulario_Usuario,eliminar_trab, list_centro, form_centr,editar_cent,eliminar_centr


urlpatterns = [
    #path ('', views.list_trab, name='list_trab'),
    #----------INICIAL-----------
    path ('', home, name='home'),
    path ('Inicio_sesion/', Inicio_sesion, name='Inicio_sesion'),
    path ('Dashboard/', Dashboard, name='Dashboard'),
    #----------USUARIO----------
    path ('Listado_usuarios/', Listado_usuarios, name='Listado_usuarios'),
    path ('Formulario_Usuario/', Formulario_Usuario, name='Formulario_Usuario'),
    #----------TRABAJADOR--------
    path ('Formulario_trabajador/', form_trab, name='form_trab'),
    path ('Listado-trabajador/', list_trab, name='listado-trabajador'),
    path ('Editar_trabajador/<id>/', editar_trab, name='edit_trab'),
    path ('Eliminar_trabajador/<id>/', eliminar_trab, name='eliminar_trabajador'),
    #----------CENTROS------------
    path ('Listado_centros/', list_centro, name='list_centr'),
    path ('Formulario_centro/', form_centr, name='form_centr'),
    path ('Editar_centro/<id>/', editar_cent, name='edit_centr'),
    path ('Eliminar_centro/<id>/', eliminar_centr, name='elim_centr'),
]