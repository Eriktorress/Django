from django.contrib import admin

from gestor.models import Centros, Comunas, Profesion, Regiones, Tipo_centro, Trabajadores, Usuarios

# Register your models here.



class TrabajadoresAdmin (admin.ModelAdmin):
    list_display = ["rut", "nombre", "apellido" ]


admin.site.register(Trabajadores, TrabajadoresAdmin)
admin.site.register(Usuarios)
admin.site.register(Profesion)
admin.site.register(Tipo_centro)
admin.site.register(Comunas)
admin.site.register(Regiones)
admin.site.register(Centros)
