from rest_framework import serializers
from usuarios.models import Alumno, Profesor


class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = ('id',
                  'nombre',
                  'dni',
                  'pin')


class ProfesorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesor
        fields = ('id',
                  'nombre',
                  'cedula')