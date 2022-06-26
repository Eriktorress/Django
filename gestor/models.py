import email
from django.db import models

# Create your models here.
class Trabajadores(models.Model):
    nombre = models.CharField (verbose_name='Nombre', max_length=100)
    apellido = models.CharField (verbose_name='Apellido', max_length=100)
    rut = models.CharField (verbose_name='Rut', max_length=10)
    email = models.CharField (verbose_name='Email', max_length=100)


    def __str__(self) :
        return f"{self.rut} - {self.nombre} {self.apellido}"
    
class Usuarios(models.Model):
    nombre = models.CharField (verbose_name='Nombre', max_length=100)
    apellido = models.CharField (verbose_name='Apellido', max_length=100)
    rut = models.CharField (verbose_name='Rut', max_length=10)
    email = models.CharField (verbose_name='Email', max_length=100)
    
    def __str__(self) :
        return f"{self.rut} - {self.nombre} {self.apellido}"