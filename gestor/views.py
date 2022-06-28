from django.shortcuts import render
from .serializers import ProfSerializer
from rest_framework import viewsets
from .models import Profesion, Trabajadores
from .forms import TrabajadorForm 


# Create your views here.
class Profview(viewsets.ModelViewSet):
    serializer_class = ProfSerializer
    Queryset = Profesion.objects.all()

def home(request):
    return render(request, 'gestor/home.html')


def list_trab(request):
    listado = Trabajadores.objects.all();
    return render(request, 'gestor/list_trab.html', {'listado':listado})

def agregar_trabajador(request):

    data = {
        'form': TrabajadorForm()

    }
    return render(request, 'gestor/agregar.html', data)