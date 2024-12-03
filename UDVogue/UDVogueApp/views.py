from django.views.generic import TemplateView, ListView, DetailView
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Editorial, Revista, Producto
from .forms import ContactForm

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        lRevistas = Revista.objects.all()
        context['gruposRevistas'] = [lRevistas[i:i+3] for i in range(0, len(lRevistas), 3)]
        return context


class ListaEditorialesView(ListView):
    model = Editorial
    template_name = 'listaEditorial.html'
    context_object_name = 'editoriales'
    ordering = ['nombre']

    def render_to_response(self, context, **response_kwargs):
        if self.request.path.endswith('.txt'):
            editoriales = Editorial.objects.order_by('nombre')
            cadenaDeTexto = ', '.join([editorial.nombre for editorial in editoriales])
            return HttpResponse(cadenaDeTexto)
        return super().render_to_response(context, **response_kwargs)


class DetalleEditorialView(DetailView):
    model = Editorial
    template_name = 'detalleEditorial.html'
    context_object_name = 'editorial'

    def render_to_response(self, context, **response_kwargs):
        if self.request.path.endswith('.txt'):
            editorial = self.object
            lRevistas = editorial.revistas.all()
            cadenaDeTexto = f"Editorial: {editorial.nombre}, CIF: {editorial.cif}\n"
            cadenaDeTexto += "Revistas publicadas:\n"

            if lRevistas.exists():
                for revista in lRevistas:
                    cadenaDeTexto += f"· {revista.titulo}, edición: {revista.numeroEdicion} ({revista.fechaPublicacion})\n"
            else:
                cadenaDeTexto += "Esta editorial no tiene revistas publicadas en estos momentos."
            return HttpResponse(cadenaDeTexto)
        return super().render_to_response(context, **response_kwargs)


class ListaRevistasView(ListView):
    model = Revista
    template_name = 'listaRevista.html'
    context_object_name = 'revistas'
    ordering = ['titulo']

    def render_to_response(self, context, **response_kwargs):
        if self.request.path.endswith('.txt'):
            revistas = Revista.objects.order_by('titulo')
            cadenaDeTexto = ', '.join([revista.titulo for revista in revistas])
            return HttpResponse(cadenaDeTexto)
        return super().render_to_response(context, **response_kwargs)


class DetalleRevistaView(DetailView):
    model = Revista
    template_name = 'detalle_revista.html'
    context_object_name = 'revista'

    def render_to_response(self, context, **response_kwargs):
        if self.request.path.endswith('.txt'):
            revista = self.object
            lProductos = revista.productos.all()
            cadenaDeTexto = (
                f"{revista.titulo}, edición: {revista.numeroEdicion} ({revista.fechaPublicacion}), "
                f"editorial: {revista.editorial.nombre}\n"
                "Oferta de productos:\n"
            )

            if lProductos.exists():
                for producto in lProductos:
                    cadenaDeTexto += (
                        f"· {producto.nombreProducto}, precio: {producto.precio}, "
                        f"talla: {producto.talla}, stock: {producto.stock}\n"
                    )
            else:
                cadenaDeTexto += "Esta revista no tiene productos en estos momentos."

            return HttpResponse(cadenaDeTexto)
        return super().render_to_response(context, **response_kwargs)


class ListaProductosView(ListView):
    model = Producto
    template_name = 'listaProducto.html'
    context_object_name = 'productos'
    ordering = ['nombreProducto']

    def render_to_response(self, context, **response_kwargs):
        if self.request.path.endswith('.txt'):
            productos = Producto.objects.order_by('nombreProducto')
            cadenaDeTexto = "Lista de productos:\n"

            if productos.exists():
                for producto in productos:
                    cadenaDeTexto += (
                        f"· {producto.nombreProducto}, talla: {producto.talla}, color: {producto.color}, "
                        f"precio: {producto.precio}, stock: {producto.stock}, "
                        f"revista: {producto.revista.titulo if producto.revista else 'Sin revista asociada'}\n"
                    )
            else:
                cadenaDeTexto += "No hay productos registrados."
            return HttpResponse(cadenaDeTexto)
        return super().render_to_response(context, **response_kwargs)


class DetalleProductoView(DetailView):
    model = Producto
    template_name = 'detalleProducto.html'
    context_object_name = 'producto'

    def render_to_response(self, context, **response_kwargs):
        if self.request.path.endswith('.txt'):
            producto = self.object
            cadenaDeTexto = (
                f"{producto.nombreProducto}\n"
                f"Talla: {producto.talla},\n"
                f"Color: {producto.color},\n"
                f"Precio: {producto.precio},\n"
                f"Stock: {producto.stock},\n"
                f"Revista: {producto.revista.titulo if producto.revista else 'Sin revista asociada'}"
            )
            return HttpResponse(cadenaDeTexto)
        return super().render_to_response(context, **response_kwargs)

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the data in form.cleaned_data (e.g., send an email)
            print(form.cleaned_data)
            return render(request, 'contact_success.html')  # A success page
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

