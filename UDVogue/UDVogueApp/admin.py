from django.contrib import admin
from .models import Editorial, Revista, Producto

# Register your models here.

admin.site.register(Editorial)
admin.site.register(Revista)
admin.site.register(Producto)