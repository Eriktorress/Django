from dataclasses import field
from pyexpat import model
from rest_fremework import serializers
from .models import tarea 


class tareaserializer(serializers.modelserializers):
    class meta:
        model=tarea
        field = ('id', 'titulo','descripcion', 'completado')