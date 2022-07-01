from django.urls import path
from .views import contacto,mascotas,registro,galeria,login,index,agregar_mascota,listado_adopcion,modificar_mascota,eliminar_mascota
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns =[
    path('',index,name="index"),
    path('login/',LoginView.as_view(template_name='vet/login.html'),name="login"),
    path('logout/',LoginView.as_view(template_name='vet/logout.html'),name="logout "),
    path('mascotas',mascotas,name="mascotas"),
    path('contacto',contacto,name="contacto"),
    path('registro/',registro,name="registro"),
    path('galeria',galeria,name="galeria"),
    path('agregar_mascota',agregar_mascota,name="agregar_mascota"),
    path('listado_adopcion',listado_adopcion,name="listado_adopcion"),
    path('modificar_mascota/<id>',modificar_mascota,name="modificar_mascota"),
    path('eliminar_mascota/<id>',eliminar_mascota,name="eliminar_mascota"),
    
]