from django.shortcuts import redirect, render, get_object_or_404
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
    return render(request,'gestor/Inicio_sesion.html')

def Dashboard(request):  #PAGINA 3
    return render(request,'gestor/Dashboard.html') 


# PAGINAS CON METODOS DINAMICOS

#USUARIOS
def Listado_usuarios (request):
    return render (request,'gestor/Listado_usuarios.html')

def Formulario_Usuario (request):
    return render(request,'gestor/Formulario_Usuario.html')


#TRABAJADORES
def list_trab(request):
    listado = Trabajadores.objects.all();
    return render(request, 'gestor/list_trab.html', {'listado':listado})

def form_trab(request):

    data = {
        'form': TrabajadorForm()

    }

    if request.method == 'POST':
        formulario = TrabajadorForm (data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"]="Registro de trabajador guardado con exito"
        else:
            data["form"] = formulario
    return render(request, 'gestor/form_trab.html', data)


def editar_trab(request, id):
    trabajadores= get_object_or_404(Trabajadores, id=id)

    data = {
        'form': TrabajadorForm(instance=trabajadores)
    }
    
    if request.method == 'POST':
        formulario = TrabajadorForm (data=request.POST, instance=trabajadores)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"]="Registro de trabajador editado con exito"
            return redirect(to="listado-trabajador")
        data["form"] = formulario
  

    return render (request, 'gestor/editartrab.html', data)


def eliminar_trab(request, id):
    trabajadores = get_object_or_404(Trabajadores, id=id)
    trabajadores.delete()

    return redirect(to="listado-trabajador")


