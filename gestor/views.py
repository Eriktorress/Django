from django.shortcuts import render
from .serializers import ProfSerializer
from rest_framework import viewsets
from .models import Profesion

# Create your views here.
class Profview(viewsets.ModelViewSet):
    serializer_class = ProfSerializer
    Queryset = Profesion.objects.all()
    
