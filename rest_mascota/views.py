from operator import methodcaller
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from vet.models import Mascota
from rest_mascota.serializers import MascotaSerializer

@csrf_exempt
@api_view(['GET','POST'])
def lista_mascota(request):
    if request.method == 'GET':
        lista_mascota = Mascota.objects.all()
        serializer = MascotaSerializer(lista_mascota, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MascotaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
@api_view(['GET','PUT','DELETE'])
def detalle_mascota(request, mas):
    try:
        mascota= Mascota.objects.get(idMascota = mas)
    except Mascota.DoesNotExist:
        return Response(Status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = MascotaSerializer(mascota)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        dataM = JSONParser().parse(request)
        serializer = MascotaSerializer(data=dataM)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        mascota.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
                
        
    
