from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from UDVogueApp.models import Revista, Producto

class Command(BaseCommand):
    help = "Crea roles de usuario y asigna permisos personalizados."

    def handle(self, *args, **kwargs):
        # Crea grupos (roles)
        admin_group, created = Group.objects.get_or_create(name="Admin")
        editor_group, created = Group.objects.get_or_create(name="Editor")
        viewer_group, created = Group.objects.get_or_create(name="Viewer")

        # Obtén los permisos
        revista_ct = ContentType.objects.get_for_model(Revista)
        producto_ct = ContentType.objects.get_for_model(Producto)

        permisos = {
            "Admin": Permission.objects.filter(content_type__in=[revista_ct, producto_ct]),
            "Editor": Permission.objects.filter(codename__in=["add_revista", "change_revista", "add_producto", "change_producto"]),
            "Viewer": Permission.objects.filter(codename__in=["view_revista", "view_producto"]),
        }

        # Asigna permisos a los grupos
        for group_name, perms in permisos.items():
            group = Group.objects.get(name=group_name)
            group.permissions.set(perms)

        self.stdout.write(self.style.SUCCESS("Roles y permisos creados exitosamente."))
