from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from usuarios.models import Alumno
from usuarios.serializers import AlumnoSerializer

from usuarios.models import Profesor
from usuarios.serializers import ProfesorSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def alumnos_lista(request):
    if request.method == 'GET':
        alumnos = Alumno.objects.all()

        nombre = request.GET.get('nombre', None)
        if nombre is not None:
            alumnos = alumnos.filter(nombre__icontains=nombre)

        alumnos_serializer = AlumnoSerializer(alumnos, many=True)
        return JsonResponse(alumnos_serializer.data, safe=False)

    elif request.method == 'POST':
        alumno_data = JSONParser().parse(request)
        alumno_serializer = AlumnoSerializer(data=alumno_data)
        if alumno_serializer.is_valid():
            alumno_serializer.save()
            return JsonResponse(alumno_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(alumno_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Alumno.objects.all().delete()
        return JsonResponse({'message': '{} Alumnos fueron eliminados exitosamente!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def alumnos_detalle(request, pk):
    try:
        alumno = Alumno.objects.get(pk=pk)
    except Alumno.DoesNotExist:
        return JsonResponse({'message': 'El alumno no existe'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        alumno_serializer = AlumnoSerializer(alumno)
        return JsonResponse(alumno_serializer.data)

    elif request.method == 'PUT':
        alumno_data = JSONParser().parse(request)
        alumno_serializer = AlumnoSerializer(alumno, data=alumno_data)
        if alumno_serializer.is_valid():
            alumno_serializer.save()
            return JsonResponse(alumno_serializer.data)
        return JsonResponse(alumno_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        alumno.delete()
        return JsonResponse({'message': 'Alumno eliminado exitosamente!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST', 'DELETE'])
def profesores_lista(request):
    if request.method == 'GET':
        profesores = Profesor.objects.all()

        nombre = request.GET.get('nombre', None)
        if nombre is not None:
            profesores = profesores.filter(nombre__icontains=nombre)

        profesores_serializer = ProfesorSerializer(profesores, many=True)
        return JsonResponse(profesores_serializer.data, safe=False)

    elif request.method == 'POST':
        profesor_data = JSONParser().parse(request)
        profesor_serializer = ProfesorSerializer(data=profesor_data)
        if profesor_serializer.is_valid():
            profesor_serializer.save()
            return JsonResponse(profesor_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(profesor_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Profesor.objects.all().delete()
        return JsonResponse({'message': '{} Profesores fueron eliminados exitosamente!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def profesores_detalle(request, pk):
    try:
        profesor = Profesor.objects.get(pk=pk)
    except Profesor.DoesNotExist:
        return JsonResponse({'message': 'El profesor no existe'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        profesor_serializer = ProfesorSerializer(profesor)
        return JsonResponse(profesor_serializer.data)

    elif request.method == 'PUT':
        profesor_data = JSONParser().parse(request)
        profesor_serializer = ProfesorSerializer(profesor, data=profesor_data)
        if profesor_serializer.is_valid():
            profesor_serializer.save()
            return JsonResponse(profesor_serializer.data)
        return JsonResponse(profesor_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        profesor.delete()
        return JsonResponse({'message': 'Profesor eliminado exitosamente!'}, status=status.HTTP_204_NO_CONTENT)