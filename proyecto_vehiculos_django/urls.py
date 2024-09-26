"""proyecto_vehiculos_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from vehiculo import views as vehiculo_views  # Ajusta a tu app
from django.contrib.auth import views as auth_views
#agregamos la vista
from vehiculo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('vehiculo/add/', views.add_vehiculo, name='add_vehiculo'),
    #path('vehiculo/listar/', views.listar_vehiculos, name='listar'),
  #  path('vehiculo/listar/', listar_vehiculos, name='listar_vehiculos'),
    path('listar/', views.listar_vehiculos, name='listar'),

    # Vistas de autenticación
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    # Vista protegida para ver el catálogo de vehículos
    path('vehiculo/listar/', vehiculo_views.ListarVehiculosView.as_view(), name='listar_vehiculos'),

    # Vista protegida para agregar vehículos (solo para usuarios con permisos)
    path('vehiculo/add/', vehiculo_views.AgregarVehiculoView.as_view(), name='add_vehiculo'),

 # Vista para login
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html', redirect_authenticated_user=True), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
]

