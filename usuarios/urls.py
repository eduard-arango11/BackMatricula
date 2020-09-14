from django.urls import path
from .views import *

urlpatterns = [
    path('api/alumnos', alumnos_lista),
    path('api/alumnos/<int:pk>', alumnos_detalle),
    path('api/profesores', profesores_lista),
    path('api/profesores/<int:pk>', profesores_detalle),
]