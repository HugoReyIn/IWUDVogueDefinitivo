from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Editorial, Revista, Producto

def index(request):
    lRevistas = Revista.objects.all() 
    grupoRevistas = [lRevistas[i:i+3] for i in range(0, len(lRevistas), 3)]
    return render(request, 'index.html', {'gruposRevistas': grupoRevistas})

def listaEditoriales(request):
    editoriales = Editorial.objects.order_by('nombre')
    cadenaDeTexto = ', '.join([editorial.nombre for editorial in editoriales])
    return HttpResponse(cadenaDeTexto)

def detalleEditorial(request, id_editorial):
    editorial = get_object_or_404(Editorial, pk=id_editorial)
    lRevistas = editorial.revistas.all()
    cadenaDeTexto = f"Editorial: {editorial.nombre}, CIF: {editorial.cif}\n"
    cadenaDeTexto += "Revistas publicadas:\n"

    if lRevistas.exists():
        for revista in lRevistas:
            cadenaDeTexto += f"· {revista.titulo}, edición: {revista.numeroEdicion} ({revista.fechaPublicacion})\n"
    else:
        cadenaDeTexto += "Esta editorial no tiene revistas publicadas en estos momentos."

    return HttpResponse(cadenaDeTexto)

def listaRevistas(request):
    revistas = Revista.objects.order_by('titulo')
    cadenaDeTexto = ', '.join([revista.titulo for revista in revistas])
    return HttpResponse(cadenaDeTexto)

def detalleRevista(request, id_revista):
    revista = get_object_or_404(Revista, pk=id_revista)
    lProductos = revista.productos.all()
    cadenaDeTexto = f"{revista.titulo}, edición: {revista.numeroEdicion} ({revista.fechaPublicacion}), editorial: {revista.editorial.nombre}\n"
    cadenaDeTexto += "Oferta de productos:\n"

    if lProductos.exists():
        for producto in lProductos:
            cadenaDeTexto += f"· {producto.nombreProducto}, precio: {producto.precio}, talla: {producto.talla}, stock: {producto.stock}\n"
    else:
        cadenaDeTexto += "Esta revista no tiene productos en estos momentos."

    return HttpResponse(cadenaDeTexto)

def listaProductos(request):
    productos = Producto.objects.order_by('nombreProducto')
    cadenaDeTexto = "Lista de productos:\n"

    if productos.exists():
        for producto in productos:
            cadenaDeTexto += (
                f"· {producto.nombreProducto}, "
                f"talla: {producto.talla}, "
                f"color: {producto.color}, "
                f"precio: {producto.precio}, "
                f"stock: {producto.stock}, "
                f"revista: {producto.revista.titulo if producto.revista else 'Sin revista asociada'}\n"
            )
    else:
        cadenaDeTexto += "No hay productos registrados."

    return HttpResponse(cadenaDeTexto)

def detalleProducto(request, id_producto):
    producto = get_object_or_404(Producto, pk=id_producto)
    cadenaDeTexto = (
        f"{producto.nombreProducto}\n"
        f"Talla: {producto.talla},\n"
        f"Color: {producto.color},\n"
        f"Precio: {producto.precio},\n"
        f"Stock: {producto.stock},\n"
        f"Revista: {producto.revista.titulo if producto.revista else 'Sin revista asociada'}"
    )

    return HttpResponse(cadenaDeTexto)


def listaEditorialHtml(request):
    lEditoriales = Editorial.objects.order_by('nombre')
    contexto = {'editoriales': lEditoriales}
    return render(request, 'listaEditorial.html', contexto)

def detalleEditorialHtml(request, id_editorial):
    editorial = get_object_or_404(Editorial, pk=id_editorial)
    contexto = {'editorial': editorial}
    return render(request, 'detalleEditorial.html', contexto)

def listaRevistasHtml(request):
    lRevistas = Revista.objects.order_by('titulo')
    contexto = {'revistas': lRevistas}
    return render(request, 'listaRevista.html', contexto)

def detalleRevistaHtml(request, id_revista):
    revista = get_object_or_404(Revista, pk=id_revista)
    contexto = {'revista': revista}
    #return render(request, 'detalleRevista.html', contexto)
    return render(request, 'detalle_revista.html', {'revista': revista})

def listaProductosHtml(request):
    lProductos = Producto.objects.order_by('nombreProducto')
    contexto = {'productos': lProductos}
    return render(request, 'listaProducto.html', contexto)
    
def detalleProductoHtml(request, id_producto):
    producto = get_object_or_404(Producto, pk=id_producto)
    contexto = {'producto': producto}
    return render(request, 'detalleProducto.html', contexto)
