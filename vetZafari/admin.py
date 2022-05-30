from django.contrib import admin

from .models import Cliente, Mascota, Raza
# Register your models here.
admin.site.register(Cliente)
admin.site.register(Mascota)
admin.site.register(Raza)
