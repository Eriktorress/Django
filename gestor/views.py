from django.shortcuts import render
from .serializers import ProfSerializer
from rest_framework import viewsets
from .models import Profesion, Trabajadores
from .forms import TrabajadorForm 


# Create your views here.
class Profview(viewsets.ModelViewSet):
    serializer_class = ProfSerializer
    Queryset = Profesion.objects.all()

# PAGINAS CON LO INICIAL 

def home(request):  #PAGINA 1
    return render(request, 'gestor/home.html')

def Inicio_sesion(request):  #PAGINA 2
    return render(request,'Inicio_sesion.html')

def Dashboard(request):  #PAGINA 3
    return render(request,'Dashboard.html') 


# PAGINAS CON METODOS DINAMICOS

#USUARIOS
def Listado_usuarios (request):
    return render (request,'Listado_usuarios.html')

def Formulario_Usuario (request):
    return render(request,'Formulario_Usuario.html')


#TRABAJADORES
def list_trab(request):
    listado = Trabajadores.objects.all();
    return render(request, 'gestor/list_trab.html', {'listado':listado})

def agregar_trabajador(request):

    data = {
        'form': TrabajadorForm()

    }
    return render(request, 'gestor/agregar.html', data)