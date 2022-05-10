from audioop import reverse
from enum import unique
from django.db import models
from django.urls import reverse

# Create your models here.
class Categoria(models.Model):
    categoria_nombre = models.CharField(max_length=100, unique=True)
    categoria_descripcion = models.CharField(max_length=250, blank=True)
    slug = models.CharField(max_length=200, unique=True)
    imagen_categoria = models.ImageField(upload_to ='photos/categoria', blank=True) #Para importar imagenes es necesario instalar el paquete pillow

    class Meta: #Para colcoarle plurar en el nombre desde la parte administrativa
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def redireccionar(self):
        return reverse('filtro_categoria', args=[self.slug]) #Hay que pasarle como argumento el parametro, el valor que quiero pasar

    def __str__(self): #Para colocar que datos se mostraran en la parte admnistrativa
        return self.categoria_nombre