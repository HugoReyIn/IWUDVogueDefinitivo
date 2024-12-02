from django.urls import path
from .views import (
    IndexView,
    ListaEditorialesView, DetalleEditorialView,
    ListaRevistasView, DetalleRevistaView,
    ListaProductosView, DetalleProductoView
)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    
    path('editoriales/', ListaEditorialesView.as_view(), name='listaEditoriales'),
    path('editoriales/<int:pk>/', DetalleEditorialView.as_view(), name='detalleEditorial'),
    
    path('revistas/', ListaRevistasView.as_view(), name='listaRevistas'),
    path('revistas/<int:pk>/', DetalleRevistaView.as_view(), name='detalleRevista'),

    path('productos/', ListaProductosView.as_view(), name='listaProductos'),
    path('productos/<int:pk>/', DetalleProductoView.as_view(), name='detalleProducto'),
]
