from lzma import MODE_FAST
from pyexpat import _Model
from tabnanny import verbose
from xml.parsers.expat import model
from django.db import models
from django.forms import ModelFormMetaclass, ModelFormOptions, modelformset_factory

# Create your models here.
class Tarea(models.Model):
    titulo = models.TextField(verbose_name="Titulo", blank=False, max_length=150)

