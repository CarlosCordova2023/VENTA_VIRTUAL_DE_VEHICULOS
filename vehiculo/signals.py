from django.db.models.signals import post_save
from django.contrib.auth.models import User, Permission
from django.dispatch import receiver
from django.contrib.contenttypes.models import ContentType
from .models import Vehiculo

@receiver(post_save, sender=User)
def asignar_permiso_visualizar_catalogo(sender, instance, created, **kwargs):
    if created:
        # Obtenemos el tipo de contenido del modelo Vehiculo
        content_type = ContentType.objects.get_for_model(Vehiculo)
        # Buscamos el permiso 'visualizar_catalogo' en base al tipo de contenido
        permiso = Permission.objects.get(codename='visualizar_catalogo', content_type=content_type)
        # Asignamos el permiso al nuevo usuario
        instance.user_permissions.add(permiso)
