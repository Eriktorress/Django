from django.contrib import admin

from gestor.models import Trabajadores, Usuarios

# Register your models here.

admin.site.register(Trabajadores)
admin.site.register(Usuarios)