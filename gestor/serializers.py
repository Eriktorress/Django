from rest_framework import serializers
from .models import Profesion 


class ProfSerializer(serializers.ModelSerializer):
    class meta:
        model= Profesion
        field = ('id', 'titulo','descripcion', 'completado')