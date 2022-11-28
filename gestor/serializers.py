from rest_framework import serializers
from .models import Profesion 
from .models import Tipo_centro
from .models import Tipo_especialidad


class ProfSerializer(serializers.ModelSerializer):
    class Meta:
        model= Profesion
        fields = '__all__'

class TipocenSerializer(serializers.ModelSerializer):     
    class Meta:
        model= Tipo_centro
        fields = '__all__'

class TipoespecualidadSerializer(serializers.ModelSerializer):     
    class Meta:
        model= Tipo_especialidad
        fields = '__all__'