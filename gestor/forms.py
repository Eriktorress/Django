from dataclasses import field
from pyexpat import model
from django import forms
from .models import Centros, Trabajadores, Usuarios
from django.contrib.auth.forms import UserCreationForm


class TrabajadorForm(forms.ModelForm):

    class Meta:
        model = Trabajadores
        fields = '__all__'


class CentroForm(forms.ModelForm):

    class Meta:
        model = Centros
        fields = '__all__'

class UsuarioForm(forms.ModelForm):

    class Meta:
        model = Usuarios
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
    pass


