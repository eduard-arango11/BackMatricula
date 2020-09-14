from django.db import models
from usuarios.models import Profesor, Alumno
from asignaturas.models import Asignatura


class PeriodoAcademico(models.Model):
    nombre = models.CharField(max_length=100, blank=False, default='')
    fecha_inicio = models.DateField(blank=True, default='')
    fecha_fin = models.DateField(blank=True, default='')


class Curso(models.Model):
    grupo = models.CharField(max_length=70, blank=False, default='')
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    periodo_academico = models.ForeignKey(PeriodoAcademico, on_delete=models.CASCADE)
    cupo = models.PositiveIntegerField(default=1)


class MatriculaCurso(models.Model):
    calificacion = models.CharField(max_length=70, blank=True, default='')
    curso = models.ForeignKey('Curso', on_delete=models.CASCADE, related_name='curso')
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE, related_name='alumno')
