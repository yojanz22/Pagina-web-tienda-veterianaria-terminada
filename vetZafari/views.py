from django.shortcuts import render,redirect

from .forms import MascotaForm
from .models import Raza,Mascota

class Persona:
    def __init__(self,rut,nombre,edad,telefono):
        self.rut = rut
        self.nombre = nombre
        self.edad = edad
        self.telefono = telefono
        super().__init__()
     
# Create your views here.

def index(request):
    
    return render(request, 'vetZafari/index.html')

def mascotas(request):
    
    return render(request, 'vetZafari/mascotas.html')

def login(request):
    
    return render(request, 'vetZafari/login.html')

def contacto(request):
    
    return render(request, 'vetZafari/contacto.html')  

def galeria(request):
    
    return render(request, 'vetZafari/galeria.html')  

def registro(request):
    
    return render(request, 'vetZafari/registro.html')  




def agregar_mascota(request):
    datos = {
        'form' : MascotaForm()
    }

    if (request.method == 'POST'):
        formulario = MascotaForm(request.POST)
        if formulario.is_valid():
            formulario.save() #insert
            datos['mensaje'] = "Se registro la mascota"
        else:
            datos['mensaje'] = "Revise datos"
    return render(request,'vetZafari/agregar_mascota.html', datos)

def listado_adopcion(request):
    mascotas = Mascota.objects.all() #select
    return render(request, 'vetZafari/listado_adopcion.html',{"mascotas":mascotas})


def modificar_mascota(request, id):
    mascota = Mascota.objects.get(nombre = id) #select * from Vehiculo where patente = id
    datos = {
        'form' : MascotaForm(instance = mascota)
    }
    
    if (request.method == 'POST'):
        formulario = MascotaForm(data = request.POST, instance = mascota)
        if formulario.is_valid():
            formulario.save() #update
            datos['mensaje'] = "Se modificó la mascota"
        else:
            datos['mensaje'] = "Revise datos, no se modificó"
    return render(request, 'vetZafari/modificar_mascota.html', datos)

def eliminar_mascota(request, id):
    mascota = Mascota.objects.get(nombre = id)
    mascota.delete() #delete from Vehiculo where patente = id
    
    return redirect(to='mascotas')

