from django.shortcuts import redirect, render, get_object_or_404
from .serializers import ProfSerializer
from rest_framework import viewsets
from .models import Centros, Profesion, Trabajadores
from .forms import TrabajadorForm, CentroForm
from django.contrib import messages

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


#--------TRABAJADORES-------------------------------------------------
#Listado de trabajadores
def list_trab(request):
    listado = Trabajadores.objects.all();
    return render(request, 'gestor/Trabajador/list_trab.html', {'listado':listado})

#Formulario de trabajador
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
    return render(request, 'gestor/Trabajador/form_trab.html', data)

#Editar trabajador
def editar_trab(request, id):
    trabajadores= get_object_or_404(Trabajadores, id=id)

    data = {
        'form': TrabajadorForm(instance=trabajadores)
    }
    
    if request.method == 'POST':
        formulario = TrabajadorForm (data=request.POST, instance=trabajadores)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado correctamente")
            return redirect(to="listado-trabajador")
        data["form"] = formulario
  

    return render (request, 'gestor/Trabajador/edit_trab.html', data)

#Eliminar trabajador
def eliminar_trab(request, id):
    trabajadores = get_object_or_404(Trabajadores, id=id)
    trabajadores.delete()

    return redirect(to="listado-trabajador")


#--------CENTRO DE TRABAJO -----------------------------------------------

#Listar centros de trabajos
def list_centro(request):
    listado = Centros.objects.all();
    return render(request, 'gestor/list_centr.html', {'listado':listado})

#Formulario centro de trabajo
def form_centr(request):

    data = {
        'form': CentroForm()
        
    }

    if request.method == 'POST':
        formulario2 = CentroForm (data=request.POST)
        if formulario2.is_valid():
            formulario2.save()
            data["mensaje"]="Registro de trabajador guardado con exito"
        else:
            data["form"] = formulario2
    return render(request, 'gestor/form_cent.html', data)

#Editar centro de trabajo
def editar_cent(request, id):
    centros= get_object_or_404(Centros, id=id)

    data = {
        'form': CentroForm(instance=centros)
    }
    
    if request.method == 'POST':
        formulario2 = CentroForm (data=request.POST, instance=centros)
        if formulario2.is_valid():
            formulario2.save()
            data["mensaje"]="Registro de trabajador editado con exito"
            return redirect(to="list_centr")
        data["form"] = formulario2

    
    return render (request, 'gestor/editar_centro.html', data)

#Editar eliminar centro

def eliminar_centr(request, id):
    centros = get_object_or_404(Centros, id=id)
    centros.delete()

    return redirect(to="list_centr")