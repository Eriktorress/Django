from django.contrib import admin

from gestor.models import Profesion, Trabajadores, Usuarios

# Register your models here.

admin.site.register(Trabajadores)
admin.site.register(Usuarios)
admin.site.register(Profesion)