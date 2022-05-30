from statistics import mode
from tkinter import CASCADE
from django.db import models

# Create your models here.


class Cliente(models.Model):
    
    nombrecompleto = models.CharField(max_length=50,primary_key=True, verbose_name='nombre')
    numero = models.CharField(max_length=20, verbose_name='numero')
    domicilio = models.CharField(max_length=50,null=True, verbose_name='Domicilio')
    fecha = models.DateTimeField(auto_now=True, verbose_name='fecha')
    
    def __str__(self):
        return self.nombrecompleto
    
    
class Mascota(models.Model):
    idMascota = models.IntegerField(auto_created = True,primary_key=True,verbose_name='Id')
    nombre = models.CharField(max_length=50,verbose_name='nombre')
    sexo = models.CharField(max_length=10,verbose_name='sexo')
    color = models.CharField(max_length=50,verbose_name='color')
    esterelizado = models.BooleanField(default=True, max_length=2,verbose_name='Esterelizado')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre
    
class Raza(models.Model):
    tipoRaza = models.CharField(max_length=50, primary_key=True, verbose_name= 'Tipo Raza')
    descripcion = models.CharField(max_length=50, verbose_name='Descripcion')
    


