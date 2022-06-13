from django.db import models

# Create your models here.
class Tarea(models.Model):
    titulo = models.TextField(verbose_name="Titulo", blank=False, max_length=150)


