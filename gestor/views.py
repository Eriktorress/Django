from cgitb import html
from django.shortcuts import render
from .serializers import ProfSerializer
from rest_framework import viewsets
from .models import Profesion, Usuarios

# Create your views here.
class Profview(viewsets.ModelViewSet):
    serializer_class = ProfSerializer
    Queryset = Profesion.objects.all()
    
def Inicio_sesion(request):
    Usuarios = Inicio_sesion.objects.all();
    return render(request,'gestor/Inicio_sesion.html',{'Usuarios': Usuarios})