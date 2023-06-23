from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
    nombreCategoria = models.CharField(max_length=50)
    descripcionCategoria = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.nombreCategoria


class Bodega(models.Model):
    nombreBodega = models.CharField(max_length=50)
    direccionBodega = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Bodega"
        verbose_name_plural = "Bodegas"

    def __str__(self):
        return self.nombreBodega


class Tienda(models.Model):
    nombreTienda = models.CharField(max_length=50)
    direccionTienda = models.CharField(max_length=100)
    bodega = models.ForeignKey(Bodega, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "Tienda"
        verbose_name_plural = "Tiendas"

    def __str__(self):
        return self.nombreTienda








class Producto(models.Model):
    nombreProducto = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    descripcionProducto = models.CharField(max_length=100)
    bodega = models.ForeignKey(Bodega, on_delete=models.CASCADE, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return self.nombreProducto


class Devolucion(models.Model):
    nombreDevolucion = models.CharField(max_length=50)
    cantidadDevolucion = models.IntegerField()
    precioDevolucion = models.IntegerField()
    motivoDevolucion = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Devolucion"
        verbose_name_plural = "Devoluciones"

    def __str__(self):
        return self.nombreDevolucion


class ProductoBodega(models.Model):
    stock = models.IntegerField()
    id_Producto = models.ForeignKey(Producto, on_delete=models.CASCADE, null=True)
    id_Bodega = models.ForeignKey(Bodega, on_delete=models.CASCADE, null=True)


class Entrada(models.Model):
    fecha_entrada = models.DateField()
    descripcion_entrada = models.CharField(max_length=100)
    bodega = models.ForeignKey(Bodega, on_delete=models.CASCADE, null=True)


class Salida(models.Model):
    fecha_salida = models.DateField()
    descripcion_salida = models.CharField(max_length=100)
    bodega = models.ForeignKey(Bodega, on_delete=models.CASCADE, null=True)


class Rol(models.Model):

    USUARIO = 'US'

    ADMIN = 'AD'

    ROLES_CHOICES = [

        (USUARIO, 'Usuario'),

        (ADMIN, 'Administrador'),

    ]

    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    rol = models.CharField(max_length=2, choices=ROLES_CHOICES, default=USUARIO)