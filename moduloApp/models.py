from django.db import models

# Create your models here.

class Categoria (models.Model):
    nombreCategoria = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
   
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
    def __str__(self):
        return self.nombreCategoria

class Bodega (models.Model):
    nombreBodega = models.CharField(max_length=50)
    direccionBodega = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Bodega"
        verbose_name_plural = "Bodegas"

    def __str__(self):
        return self.nombreBodega
    
class Entrada_Producto (models.Model):
    fecha_entrada = models.DateField()
    descripcion_entrada = models.CharField(max_length=100)
    bodega = models.ForeignKey(Bodega, on_delete=models.CASCADE, null=True)

class Salida_Producto(models.Model):
    fechaSalida = models.DateField()
    descripcionSalida = models.CharField(max_length=100)
    bodega = models.ForeignKey(Bodega, on_delete=models.CASCADE, null=True)

class Devolucion_Producto(models.Model):
    fechaDevolucion = models.DateField()
    descripcionSalida = models.CharField(max_length=100)
    bodega = models.ForeignKey(Bodega, on_delete=models.CASCADE, null=True)

class Tienda(models.Model):
    nombreTienda = models.CharField(max_length=50)
    direccionTienda = models.CharField(max_length=100)
    bodega = models.ForeignKey(Bodega, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "Tienda"
        verbose_name_plural = "Tiendas"

    def __str__(self):
        return self.nombreTienda

class Rol(models.Model):
    nombreRol = models.CharField(max_length=50)
    descripcionRol = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Rol"
        verbose_name_plural = "Roles"

    def __str__(self):
        return self.nombreRol

class Trabajador(models.Model):
    nombreTrabajador = models.CharField(max_length=50)
    contraseñaTrabajador = models.CharField(max_length=50)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE, null=True)
    tienda = models.ForeignKey(Tienda, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "Trabajador"
        verbose_name_plural = "Trabajadores"

    def __str__(self):
        return self.nombreTrabajador
    
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



class productoBodega (models.Model):
    stock = models.IntegerField()
    id_Producto = models.ForeignKey(Producto, on_delete=models.CASCADE, null=True)
    id_Bodega = models.ForeignKey(Bodega, on_delete=models.CASCADE, null=True)
