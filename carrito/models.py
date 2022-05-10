from django.db import models
from tienda.models import Productos

# Create your models here.
class Carrito(models.Model):
    id_carrito = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.id_carrito
        
class cartItem(models.Model):
    product = models.ForeignKey(Productos, on_delete=models.CASCADE)
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    activo = models.BooleanField(default=True)

    def sub_total(self):
        return (self.cantidad * self.product.precio)

    def __str__(self):
        return str(self.product)