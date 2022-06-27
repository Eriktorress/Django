from django.shortcuts import render
from .serializers import ProfSerializer
from rest_framework import viewsets
from .models import Profesion, Trabajadores


# Create your views here.
class Profview(viewsets.ModelViewSet):
    serializer_class = ProfSerializer
    Queryset = Profesion.objects.all()

def list_trab(request):
    listado = Trabajadores.objects.all();
    return render(request, 'gestor/list_trab.html', {'listado':listado})