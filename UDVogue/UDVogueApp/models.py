from django.db import models

class Editorial(models.Model):
    nombre = models.CharField(max_length=80, default = "")
    cif = models.CharField(max_length=12, default = 'A00000000000')

    def agregarRevista(self, revista):
        self.revistas.add(revista)

    def mostrarRevistas(self):
        return [revista.titulo for revista in self.revistas.all()]

    def __str__(self):
        return self.nombre

class Revista(models.Model):
    editorial = models.ForeignKey(Editorial, on_delete = models.CASCADE, related_name = "revistas", null = True)
    titulo = models.CharField(max_length=50, null = True)
    imagen = models.ImageField(upload_to='revistas/', null = True)
    numeroEdicion = models.IntegerField(default = 1)
    fechaPublicacion = models.DateField(null = True)

    def __str__(self):
        return self.titulo

class Producto(models.Model):
    revista = models.ForeignKey(Revista, on_delete = models.CASCADE, related_name = "productos", null = True)
    nombreProducto = models.CharField(max_length = 60, null = True)
    talla = models.CharField(max_length = 3, default = 'M')
    imagen = models.ImageField(upload_to='productos/', null = True)
    precio = models.DecimalField(max_digits = 5, decimal_places = 2, default = 0.00)
    stock = models.IntegerField(default = 0)

    def actualizarPrecio(self, nuevo_precio):
        self.precio = nuevo_precio
        self.save()

    def ajustarStock(self, cantidad):
        self.stock = max(0, self.stock + cantidad)
        self.save()

    def mostrarInformacion(self):
        return f"Producto: {self.nombreProducto}, Precio: {self.precio}, Stock: {self.stock}"

    def __str__(self):
        return self.nombreProducto