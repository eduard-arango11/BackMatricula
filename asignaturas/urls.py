from django.urls import path
from .views import *

urlpatterns = [
    path('api/asignaturas', asignaturas_lista),
    path('api/asignaturas/<int:pk>', asignaturas_detalle),
]