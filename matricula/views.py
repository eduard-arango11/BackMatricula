from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from matricula.models import Curso, MatriculaCurso, PeriodoAcademico
from matricula.serializers import CursoSerializer, MatriculaSerializer, PeriodoAcademicoSerializer, MatriculaSerializerPost, CursoSerializerPost
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def periodos_lista(request):
    if request.method == 'GET':
        periodos = PeriodoAcademico.objects.all()

        periodos_serializer = PeriodoAcademicoSerializer(periodos, many=True)
        return JsonResponse(periodos_serializer.data, safe=False)

    elif request.method == 'POST':
        periodo_data = JSONParser().parse(request)
        periodo_serializer = PeriodoAcademicoSerializer(data=periodo_data)
        if periodo_serializer.is_valid():
            periodo_serializer.save()
            return JsonResponse(periodo_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(periodo_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = PeriodoAcademico.objects.all().delete()
        return JsonResponse({'message': '{} Periodos Academicos fueron eliminados exitosamente!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def periodos_detalle(request, pk):
    try:
        periodo = PeriodoAcademico.objects.get(pk=pk)
    except PeriodoAcademico.DoesNotExist:
        return JsonResponse({'message': 'El periodo no existe'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        periodo_serializer = PeriodoAcademicoSerializer(periodo)
        return JsonResponse(periodo_serializer.data)

    elif request.method == 'PUT':
        periodo_data = JSONParser().parse(request)
        periodo_serializer = CursoSerializer(periodo, data=periodo_data)
        if periodo_serializer.is_valid():
            periodo_serializer.save()
            return JsonResponse(periodo_serializer.data)
        return JsonResponse(periodo_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        periodo.delete()
        return JsonResponse({'message': 'Periodo eliminado exitosamente!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST', 'DELETE'])
def cursos_lista(request):
    if request.method == 'GET':
        cursos = Curso.objects.all()

        cursos_serializer = CursoSerializer(cursos, many=True)
        return JsonResponse(cursos_serializer.data, safe=False)

    elif request.method == 'POST':
        curso_data = JSONParser().parse(request)
        curso_serializer = CursoSerializerPost(data=curso_data)
        if curso_serializer.is_valid():
            curso_serializer.save()
            return JsonResponse(curso_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(curso_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Curso.objects.all().delete()
        return JsonResponse({'message': '{} Cursos fueron eliminados exitosamente!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def cursos_detalle(request, pk):
    try:
        curso = Curso.objects.get(pk=pk)
    except Curso.DoesNotExist:
        return JsonResponse({'message': 'El curso no existe'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        curso_serializer = CursoSerializer(curso)
        return JsonResponse(curso_serializer.data)

    elif request.method == 'PUT':
        curso_data = JSONParser().parse(request)
        curso_serializer = CursoSerializer(curso, data=curso_data)
        if curso_serializer.is_valid():
            curso_serializer.save()
            return JsonResponse(curso_serializer.data)
        return JsonResponse(curso_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        curso.delete()
        return JsonResponse({'message': 'Curso eliminado exitosamente!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST', 'DELETE'])
def matriculas_lista(request):
    if request.method == 'GET':
        matriculas = MatriculaCurso.objects.all()

        matriculas_serializer = MatriculaSerializer(matriculas, many=True)
        return JsonResponse(matriculas_serializer.data, safe=False)

    elif request.method == 'POST':
        matricula_data = JSONParser().parse(request)
        matricula_serializer = MatriculaSerializerPost(data=matricula_data)
        if matricula_serializer.is_valid():
            matricula_serializer.save()
            return JsonResponse(matricula_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(matricula_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = MatriculaCurso.objects.all().delete()
        return JsonResponse({'message': '{} Matriculas fueron eliminadas exitosamente!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def matriculas_detalle(request, pk):
    try:
        matricula = MatriculaCurso.objects.get(pk=pk)
    except MatriculaCurso.DoesNotExist:
        return JsonResponse({'message': 'La matricula no existe'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        matricula_serializer = MatriculaSerializer(matricula)
        return JsonResponse(matricula_serializer.data)

    elif request.method == 'PUT':
        matricula_data = JSONParser().parse(request)
        matricula_serializer = MatriculaSerializer(matricula, data=matricula_data)
        if matricula_serializer.is_valid():
            matricula_serializer.save()
            return JsonResponse(matricula_serializer.data)
        return JsonResponse(matricula_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        matricula.delete()
        return JsonResponse({'message': 'Matricula eliminada exitosamente!'}, status=status.HTTP_204_NO_CONTENT)
