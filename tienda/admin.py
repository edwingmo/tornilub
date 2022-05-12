from django.contrib import admin
from .models import Productos, Favoritos, itemFavoritos
# Register your models here.

class AdminProductos(admin.ModelAdmin):

    
    #nombre_producto = models.CharField(max_length=100, unique=True)
    #slug = models.CharField(max_length=100, unique=True)
    #descripcion = models.TextField(max_length=500, blank=True)
    #precio = models.IntegerField()
    #cantidad = models.IntegerField(default=0)
    #stock = models.IntegerField(default=0)
    #activo = models.BooleanField(default=True)
    #imagenes = models.ImageField(upload_to='photos/productos')
    #create_date = models.DateField(auto_now_add=True)
    #last_edit = models.DateField(auto_now=True)
    #category = models.ForeignKey(Categoria, on_delete=models.CASCADE)


    list_display = ('activo', 'category', 'nombre_producto', 'slug', 'descripcion', 'precio', 'cantidad', 'stock', 'create_date', 'last_edit',)
    prepopulated_fields = {'slug':('nombre_producto',)}
    list_display_links = ('nombre_producto',)

admin.site.register(Productos, AdminProductos)
admin.site.register(Favoritos)
admin.site.register(itemfavoritos)
