from django.contrib import admin
from .models import Editorial, Revista, Producto

# Admin para Editorial
class EditorialAdmin(admin.ModelAdmin):
    def has_module_permission(self, request):
        # Solo usuarios en el grupo 'AdminEditorial' pueden ver este modelo
        return request.user.groups.filter(name='AdminEditorial').exists() or request.user.is_superuser

    def has_add_permission(self, request):
        # Solo 'AdminEditorial' y superusuarios pueden agregar
        return request.user.groups.filter(name='AdminEditorial').exists() or request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        # Solo 'AdminEditorial' y superusuarios pueden editar
        return request.user.groups.filter(name='AdminEditorial').exists() or request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        # Solo 'AdminEditorial' y superusuarios pueden borrar
        return request.user.groups.filter(name='AdminEditorial').exists() or request.user.is_superuser

# Admin para Revista
class RevistaAdmin(admin.ModelAdmin):
    def has_module_permission(self, request):
        # Solo usuarios en el grupo 'AdminEditorial' o 'AdminRevistas' pueden ver este modelo
        return request.user.groups.filter(name__in=['AdminEditorial', 'AdminRevistas']).exists() or request.user.is_superuser

    def has_add_permission(self, request):
        # Solo 'AdminEditorial' y 'AdminRevistas' pueden agregar revistas
        return request.user.groups.filter(name__in=['AdminEditorial', 'AdminRevistas']).exists() or request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        # Solo 'AdminEditorial' y 'AdminRevistas' pueden editar revistas
        return request.user.groups.filter(name__in=['AdminEditorial', 'AdminRevistas']).exists() or request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        # Solo 'AdminEditorial' y 'AdminRevistas' pueden borrar revistas
        return request.user.groups.filter(name__in=['AdminEditorial', 'AdminRevistas']).exists() or request.user.is_superuser

# Admin para Producto
class ProductoAdmin(admin.ModelAdmin):
    def has_module_permission(self, request):
        # Solo usuarios en el grupo 'AdminProductos' pueden ver este modelo
        return request.user.groups.filter(name='AdminProductos').exists() or request.user.is_superuser

    def has_add_permission(self, request):
        # Solo 'AdminProductos' pueden agregar productos
        return request.user.groups.filter(name='AdminProductos').exists() or request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        # Solo 'AdminProductos' pueden editar productos
        return request.user.groups.filter(name='AdminProductos').exists() or request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        # Solo 'AdminProductos' pueden borrar productos
        return request.user.groups.filter(name='AdminProductos').exists() or request.user.is_superuser


# Registro de modelos en el administrador con las configuraciones personalizadas
admin.site.register(Editorial, EditorialAdmin)
admin.site.register(Revista, RevistaAdmin)
admin.site.register(Producto, ProductoAdmin)
