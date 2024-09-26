from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from .models import Vehiculo
from .forms import VehiculoForm

from django.contrib.auth.mixins import PermissionRequiredMixin

from django.views.generic.edit import CreateView


def index(request):
    return render(request, 'vehiculo/index.html')

@login_required
@permission_required('vehiculo.add_vehiculo', raise_exception=True)
def add_vehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = VehiculoForm()
    return render(request, 'vehiculo/add_vehiculo.html', {'form': form})

@permission_required('vehiculo.visualizar_catalogo', raise_exception=True)
def catalogo_vehiculos(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'vehiculo/catalogo.html', {'vehiculos': vehiculos})

@login_required
@permission_required('vehiculo.visualizar_catalogo', raise_exception=True)
def listar_vehiculos(request):
    # Obtener todos los vehículos
    vehiculos = Vehiculo.objects.all()
    
    # Clasificar vehículos por precio
    vehiculos_bajo = vehiculos.filter(precio__lte=10000)
    vehiculos_medio = vehiculos.filter(precio__gt=10000, precio__lte=30000)
    vehiculos_alto = vehiculos.filter(precio__gt=30000)
    
    # Pasar los vehículos clasificados al contexto
    context = {
        'vehiculos_bajo': vehiculos_bajo,
        'vehiculos_medio': vehiculos_medio,
        'vehiculos_alto': vehiculos_alto,
    }
    
    return render(request, 'vehiculo/listar.html', context)

class ListarVehiculosView(LoginRequiredMixin, ListView):
    model = Vehiculo
    template_name = 'vehiculo/listar.html'
    context_object_name = 'vehiculos'

    def get_queryset(self):
        return Vehiculo.objects.all()

    # Redirigir a la página de login si no está autenticado
    login_url = 'login'




class AgregarVehiculoView(PermissionRequiredMixin, CreateView):
    model = Vehiculo
    template_name = 'vehiculo/agregar.html'
    fields = ['marca', 'modelo', 'serial_carroceria', 'serial_motor', 'categoria', 'precio']
    success_url = '/vehiculo/listar/'

    # Permiso requerido
    permission_required = 'vehiculo.add_vehiculo'

    # Redirigir si no tiene permiso
    login_url = 'login'
    raise_exception = True