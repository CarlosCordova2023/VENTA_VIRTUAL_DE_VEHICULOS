from django.contrib import admin
from .models import Vehiculo

@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'categoria', 'precio', 'fecha_creacion', 'fecha_modificacion')
    search_fields = ('marca', 'modelo', 'serial_carroceria', 'serial_motor', 'categoria')
