from django.db import models

# Create your models here.


class Bodega (models.Model):
    nombreBodega = models.CharField(max_length=50)
    direccionBodega = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Bodega"
        verbose_name_plural = "Bodegas"

    def __str__(self):
        return self.nombreBodega
    
class Tienda (models.Model):
    nombreTienda = models.CharField(max_length=50)
    direccionTienda = models.CharField(max_length=100)
    bodega =models.ForeignKey(Bodega, on_delete= models.CASCADE, null=True)

    class Meta:
        verbose_name = "Tienda"
        verbose_name_plural = "Tiendas"

    def __str__(self):
        return self.nombretienda


class Producto (models. Model):
    nombreProducto = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    descripcionProducto = models.CharField(max_length=100)
    bodega = models.ForeignKey(Bodega, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return self.nombreProducto
    

class Devolucion (models. Model):
    nombreDevolucion = models.CharField(max_length=50)
    cantidadDevolucion = models.IntegerField()
    precioDevolucion = models.IntegerField()
    motivoDevolucion = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Devolucion"
        verbose_name_plural = "Devoluciones"

    def __str__(self):
        return self.nombreDevolucion


class productoBodega (models.Model):
    stock = models.IntegerField()
    id_Producto = models.ForeignKey(Producto, on_delete=models.CASCADE, null=True)
    id_Bodega = models.ForeignKey(Bodega, on_delete=models.CASCADE, null=True)


# class registrarse (models.Model):
#     nombre = models.CharField(max_length=50)
#     apellido =models.CharField(max_length=50)
#     usuario = models.CharField(max_length=10)
#     contraseña = models.CharField(max_length=10)
#     contrasena2 = models.CharField(max_length=10)
