from django.db import models


class Asignatura(models.Model):
    nombre = models.CharField(max_length=70, blank=False, default='')
    descripcion = models.CharField(max_length=200, blank=True, default='')
    codigo = models.CharField(max_length=20, blank=True, default='')