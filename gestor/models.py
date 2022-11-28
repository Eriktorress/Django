from asyncio.windows_events import NULL
from decimal import DefaultContext
import email
from pyexpat import model
from tkinter import N
from unicodedata import name
from django.db import models
from django.urls import register_converter



# Create your models here.

class Profesion (models.Model):
    nombre_prof = models.CharField (verbose_name='Nombre Profesión', max_length=100)

    def __str__(self) :
        return f"{self.nombre_prof}"
class Trabajadores(models.Model):
    nombre = models.CharField (verbose_name='Nombre', max_length=100)
    apellido = models.CharField (verbose_name='Apellido', max_length=100)
    rut = models.CharField (verbose_name='Rut', max_length=10)
    email = models.EmailField ()
    profesion = models.ForeignKey(Profesion, on_delete=models.PROTECT, null=True)

    def __str__(self) :
        return f"{self.rut} - {self.nombre} {self.apellido}"
class Usuarios(models.Model):
    nombre_com = models.CharField (verbose_name='Nombre completo', max_length=100)
    apelllidos_usu = models.CharField (verbose_name='Apellido', max_length=100)
    email = models.EmailField ()
    contrasena = models.CharField (verbose_name='Contraseña', max_length=10)

    def __str__(self) :
        return f"{self.nombre_com} - {self.apelllidos_usu} {self.email}"



class Tipo_centro (models.Model):
    nom_tip_centr = models.CharField(max_length=50)

    def __str__(self) :
        return self.nom_tip_centr
    
class Comunas (models.Model):
    nombre_comu = models.CharField(max_length=50)

    def __str__(self) :

        return self.nombre_comu
    
class Regiones (models.Model):
    nombre_regi = models.CharField(max_length=50)

    def __str__(self) :
        return self.nombre_regi
    

class Centros (models.Model):
    tipo_centro = models.ForeignKey(Tipo_centro, on_delete=models.PROTECT)
    direccion = models.CharField(max_length=100)
    comuna = models.ForeignKey(Comunas, on_delete=models.PROTECT)
    region = models.ForeignKey(Regiones, on_delete=models.PROTECT)
    telefono = models.CharField(max_length=100)

    def __str__(self) :
        return f"{self.tipo_centro}-{self.direccion} - {self.comuna}- {self.region}"

# Modelo para API REST

class Tipo_especialidad (models.Model):
    tip_especi = models.CharField (verbose_name='Tipo especialidad', max_length=100)

    def __str__(self) :
        return f"{self.tip_especi}"