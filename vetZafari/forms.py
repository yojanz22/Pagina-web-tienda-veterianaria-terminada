from django import forms
from django.forms import ModelForm 
from .models import Mascota

class MascotaForm(ModelForm):
    class Meta:
        model = Mascota
        fields = ['nombre','sexo','color','esterelizado','cliente']


