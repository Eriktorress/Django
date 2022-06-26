from django.http import QueryDict
from django.shortcuts import render
from .serializers import tareaserializer
from rest_framework import viewsets
from .models import tarea

# Create your views here.
class Tareaview(viewsets.modelsviewsets):
    serializer_class = tareaserializer
    Queryset = tarea.objects.all()
    
