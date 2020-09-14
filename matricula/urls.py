from django.urls import path
from .views import *

urlpatterns = [
    path('api/periodos', periodos_lista),
    path('api/periodos/<int:pk>', periodos_detalle),

    path('api/cursos', cursos_lista),
    path('api/cursos/<int:pk>', cursos_detalle),

    path('api/matriculas', matriculas_lista),
    path('api/matriculas/<int:pk>', matriculas_detalle),
]