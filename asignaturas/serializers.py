from rest_framework import serializers
from asignaturas.models import Asignatura


class AsignaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asignatura
        fields = ('id',
                  'nombre',
                  'descripcion',
                  'codigo')