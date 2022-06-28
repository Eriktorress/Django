from dataclasses import field
from pyexpat import model
from django import forms
from .models import Trabajadores


class TrabajadorForm(forms.ModelForm):

    class Meta:
        model = Trabajadores
        fields = '__all__'


