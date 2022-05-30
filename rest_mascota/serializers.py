from rest_framework import serializers
from vetZafari.models import Mascota

class MascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mascota
        fields = ['idMascota','nombre','sexo','color','esterelizado','cliente']