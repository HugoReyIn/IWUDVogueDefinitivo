from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    path('editoriales/', views.listaEditoriales, name = 'listaEditoriales'),
    path('editoriales/<int:id_editorial>', views.detalleEditorial, name = 'detalleEditorial'),
    
    path('revistas/', views.listaRevistas, name = 'listaRevistas'),
    path('revistas/<int:id_revista>', views.detalleRevista, name = 'detalleRevista'),

    path('productos/', views.listaProductos, name = 'listaProductos'),
    path('productos/<int:id_producto>', views.detalleProducto, name = 'detalleProducto'),

    path('editorialesHtml/', views.listaEditorialHtml, name = 'listaEditorialHtml'),
    path('editorialesHtml/<int:id_editorial>', views.detalleEditorialHtml, name = 'detalleEditorialHtml'),

    path('revistasHtml/', views.listaRevistasHtml, name = 'listaRevistasHtml'),
    path('revistasHtml/<int:id_revista>', views.detalleRevistaHtml, name = 'detalleRevistaHtml'),

    path('productosHtml/', views.listaProductosHtml, name = 'listaProductosHtml'),
    path('productosHtml/<int:id_producto>', views.detalleProductoHtml, name = 'detalleProductoHtml'),
]