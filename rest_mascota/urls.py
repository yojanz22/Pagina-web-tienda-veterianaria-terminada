from django.urls import path
from rest_mascota.views import lista_mascota,detalle_mascota

urlpatterns = [
    path('lista_mascota',lista_mascota,name="lista_mascota"),
    path('detalle_mascota/<mas>',detalle_mascota,name='detalle_mascota')
]
