from rest_framework import serializers
from .models import Profesion 


class ProfSerializer(serializers.ModelSerializer):
    class Meta:
        model= Profesion
        fields = '__all__'