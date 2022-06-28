from dataclasses import field
from pyexpat import model
from django import forms
from .models import Centros, Trabajadores


class TrabajadorForm(forms.ModelForm):

    class Meta:
        model = Trabajadores
        fields = '__all__'


class CentroForm(forms.ModelForm):

    class Meta:
        model = Centros
        fields = '__all__'


