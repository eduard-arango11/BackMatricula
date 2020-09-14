from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from asignaturas.models import Asignatura
from asignaturas.serializers import AsignaturaSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def asignaturas_lista(request):
    if request.method == 'GET':
        asignaturas = Asignatura.objects.all()

        nombre = request.GET.get('nombre', None)
        if nombre is not None:
            asignaturas = asignaturas.filter(nombre__icontains=nombre)

        asignaturas_serializer = AsignaturaSerializer(asignaturas, many=True)
        return JsonResponse(asignaturas_serializer.data, safe=False)

    elif request.method == 'POST':
        asignatura_data = JSONParser().parse(request)
        asignatura_serializer = AsignaturaSerializer(data=asignatura_data)
        if asignatura_serializer.is_valid():
            asignatura_serializer.save()
            return JsonResponse(asignatura_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(asignatura_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Asignatura.objects.all().delete()
        return JsonResponse({'message': '{} Asignaturas fueron eliminadas exitosamente!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def asignaturas_detalle(request, pk):
    try:
        asignatura = Asignatura.objects.get(pk=pk)
    except Asignatura.DoesNotExist:
        return JsonResponse({'message': 'La asignatura no existe'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        asignatura_serializer = AsignaturaSerializer(asignatura)
        return JsonResponse(asignatura_serializer.data)

    elif request.method == 'PUT':
        asignatura_data = JSONParser().parse(request)
        asignatura_serializer = AsignaturaSerializer(asignatura, data=asignatura_data)
        if asignatura_serializer.is_valid():
            asignatura_serializer.save()
            return JsonResponse(asignatura_serializer.data)
        return JsonResponse(asignatura_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        asignatura.delete()
        return JsonResponse({'message': 'Asignatura eliminada exitosamente!'}, status=status.HTTP_204_NO_CONTENT)
