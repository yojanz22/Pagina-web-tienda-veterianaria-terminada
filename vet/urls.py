from django.urls import path
from .views import contacto,mascotas,registro,galeria,login,index,agregar_mascota,listado_adopcion,modificar_mascota,eliminar_mascota

urlpatterns =[
    path('',index,name="index"),
    path('login',login,name="login"),
    path('mascotas',mascotas,name="mascotas"),
    path('contacto',contacto,name="contacto"),
    path('registro',registro,name="registro"),
    path('galeria',galeria,name="galeria"),
    path('agregar_mascota',agregar_mascota,name="agregar_mascota"),
    path('listado_adopcion',listado_adopcion,name="listado,adopcion"),
    path('modificar_mascota/<id>',modificar_mascota,name="modificar_mascota"),
    path('eliminar_mascota/<id>',eliminar_mascota,name="eliminar_mascota"),
]