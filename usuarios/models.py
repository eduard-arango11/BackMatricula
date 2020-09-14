from django.db import models

class Alumno(models.Model):
    nombre = models.CharField(max_length=200, blank=False, default='')
    dni = models.CharField(max_length=20, blank=False, default='')
    pin = models.CharField(max_length=20, blank=True, default='')


class Profesor(models.Model):
    nombre = models.CharField(max_length=200, blank=False, default='')
    cedula = models.CharField(max_length=20, blank=False, default='')
