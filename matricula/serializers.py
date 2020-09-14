from rest_framework import serializers
from matricula.models import Curso, MatriculaCurso, PeriodoAcademico
from usuarios.serializers import ProfesorSerializer, AlumnoSerializer
from asignaturas.serializers import AsignaturaSerializer


class PeriodoAcademicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeriodoAcademico
        fields = ('id',
                  'nombre',
                  'fecha_inicio',
                  'fecha_fin')


class CursoSerializer(serializers.ModelSerializer):
    periodo_academico = PeriodoAcademicoSerializer(read_only=True)
    asignatura = AsignaturaSerializer(read_only=True)
    profesor = ProfesorSerializer(read_only=True)

    class Meta:
        model = Curso
        fields = ('id',
                  'grupo',
                  'profesor',
                  'asignatura',
                  'periodo_academico',
                  'cupo')


class CursoSerializerPost(serializers.ModelSerializer):

    class Meta:
        model = Curso
        fields = ('id',
                  'grupo',
                  'profesor',
                  'asignatura',
                  'periodo_academico',
                  'cupo')


class MatriculaSerializer(serializers.ModelSerializer):
    curso = CursoSerializer(read_only=True)
    alumno = AlumnoSerializer(read_only=True)

    class Meta:
        model = MatriculaCurso
        fields = ('id',
                  'calificacion',
                  'curso',
                  'alumno')


class MatriculaSerializerPost(serializers.ModelSerializer):

    class Meta:
        model = MatriculaCurso
        fields = ('id',
                  'calificacion',
                  'curso',
                  'alumno')