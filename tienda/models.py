from django.db import models
from categoria.models import Categoria
from django.urls import reverse
from accounts.models import User

# Create your models here.
class Productos(models.Model):
    nombre_producto = models.CharField(max_length=100, unique=True)
    slug = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(max_length=500, blank=True)
    precio = models.IntegerField()
    cantidad = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)
    activo = models.BooleanField(default=True)
    imagenes = models.ImageField(upload_to='photos/productos')
    create_date = models.DateField(auto_now_add=True)
    last_edit = models.DateField(auto_now=True)
    numero_parte = models.CharField(max_length=50, blank=True)
    clicks = models.IntegerField(default=0)
    favorito_status = models.BooleanField(default=False)
    category = models.ForeignKey(Categoria, on_delete=models.CASCADE) # el foreingkey  es para relacionarlo a mi modelo de categoria(pudiendo llamar cualquier propiedad de la misma)
    #el Cascade sirve para cuando se elimine una categoria tambien se elimine el producto
    marca = models.CharField(max_length=100, blank=True)


    def redireccionar(self):
        return reverse('detalles_producto', args=[self.slug]) #Hay que pasarle como argumento el parametro, el valor que quiero pasar

    def __str__(self):
        return self.nombre_producto

class Favoritos(models.Model):
    id_favorito = models.CharField(max_length=250, blank=True)
    create_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id_favorito

class itemfavoritos(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Productos, on_delete=models.CASCADE)
    favorit = models.ForeignKey(Favoritos, on_delete=models.CASCADE, null=True)

    def __unicode__(self):
        return self.product

