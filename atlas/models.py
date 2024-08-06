from django.db import models

class Usuario(models.Model):
  id_usuario= models.AutoField(primary_key=True)
  rol= models.CharField(max_length=32)
  nombre_usuario=models.CharField(max_length=32)
  clave= models.CharField(max_length=25)
  
  def __str__(self):
    return self.nombre_usuario


class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=100)
    precio = models.FloatField()
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre_producto

class HistorialVentas(models.Model):
    id_venta = models.AutoField(primary_key=True)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    nombre_producto = models.CharField(max_length=100, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    cantidad = models.IntegerField()
    responsable = models.CharField(max_length=50)
    precio = models.FloatField() 

    def save(self, *args, **kwargs):
        self.nombre_producto = self.id_producto.nombre_producto
        super(HistorialVentas, self).save(*args, **kwargs)
    
    def __str__(self):
        return f'Venta {self.id_venta} - Producto {self.id_producto.nombre_producto}'
    class Meta:
      ordering = ['-id_venta'] 

class UsuarioVenta(models.Model):
    id = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_ventas = models.ForeignKey(HistorialVentas, on_delete=models.CASCADE)

    def __str__(self):
        return f'Usuario {self.id_usuario.nombre_usuario} - Venta {self.id_ventas.id_venta}'
