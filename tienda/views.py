from inspect import currentframe
from pyexpat.errors import messages
from subprocess import IDLE_PRIORITY_CLASS
from django.shortcuts import get_object_or_404, redirect, render

from carrito.models import cartItem
from carrito.views import _cart_id
from .models import Productos, Favoritos, itemFavoritos
from categoria.models import Categoria
from django.urls import reverse
from django.db.models import Q
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator #Todo esto sirve para las paginaciones

productos_mostrar = 16 #Estos es la cantidad de productos que se mostraran por paginacion

#colocar en el template el has_other_pages para saber si tiene mas paginas
#colocar el has_previous para saber si hay pagina anterior
#colocar previous_page_number para ir a la pagina anterior
#colocar .paginator.page_range para iterar las paginas
# productos.number i para saber en que posicion me encuentro
#colocar .has_next para saber si hay otra pagina adelante
#colocar .next_page_number para ir a la pgina siguiente

# Create your views here.
def tienda(request, precio_min = 0, slug=None):
    title = 'Tienda'

    #filtro Por categoria

    categorias = None
    productos = None
    
    if slug != None:
        categorias = get_object_or_404(Categoria, slug=slug) # Lo que hace get_object_or_404 es que busca en el primer parametro el modelo, y compara una de sus
        #propiedades con lo que tu estas buscano, si lo consigue devuelve esa query de lo contrario lanza un error
        productos = Productos.objects.filter(category=categorias, activo=True)
        paginator = Paginator(productos, productos_mostrar) #Paginator necesita 2 parametros obligatorios, sobre que quieres paginar y en grupos de cuantos  
        page = request.GET.get('page') #Capturando la pagina que quiere acceder el cliente
        page_product = paginator.get_page(page) #mostrando los productos de la pagina         
    else:
        productos = Productos.objects.all().filter(activo=True)
        paginator = Paginator(productos, productos_mostrar) #Paginator necesita 2 parametros obligatorios, sobre que quieres paginar y en grupos de cuantos  
        page = request.GET.get('page') #Capturando la pagina que quiere acceder el cliente
        page_product = paginator.get_page(page) #mostrando los productos de la pagina

    #filtro por precio minimo

    #''' if request.method == "GET": #Verificando que la informacion me llega por metodo GET
    #    precio_min = int(request.GET.get('precio_min', 0)) #GET.get para conseguir un valor, no un diccionario, a parte rectifico que me llega por metodo GET

    #    if precio_min >= 1:   
    #        productos = Productos.objects.filter(precio__gte = precio_min) #__gte para filtrar de igual o mayor que
    #        reverse('filtro_precio', args=[precio_min]) #Reverse le agrega a la pagina la url que quieras junto con sus argumentos
        
    #else:
    #    productos = Productos.objects.all().filter(activo=True) '''

    context = {
        'title':title,
        'productos':page_product,
        'cantidad_productos':productos.count(),
    }
    
    return render(request, 'tienda/tienda.html', context)
#Fin de la funcion tienda

def buscar(request):

    if request.method == "GET":
        buscar = request.GET.get('buscar', '')    
        buscar.upper()
        productos = Productos.objects.filter(Q(nombre_producto__icontains=buscar) | Q(numero_parte__icontains=buscar) | Q(marca__icontains=buscar) | Q(descripcion__icontains=buscar))
        paginator = Paginator(productos, productos_mostrar) #Paginator necesita 2 parametros obligatorios, sobre que quieres paginar y en grupos de cuantos  
        page = request.GET.get('page') #Capturando la pagina que quiere acceder el cliente
        page_product = paginator.get_page(page) #mostrando los productos de la pagina
        """reverse('buscar', args=[buscar])"""
    else:
        productos = Productos.objects.all().filter(activo=True)

    context = {
        'productos':page_product,
        'cantidad_productos':productos.count(),
    }
    
    return render(request, 'tienda/tienda.html', context)

#Funcion detalle del producto
def detalles(request, slug):
    producto = Productos.objects.get(slug=slug)

    en_carrito = cartItem.objects.filter(carrito__id_carrito=_cart_id(request), product=producto).exists() #para obtener una propiedad de un modelo se usa dos rayas para abajo
    # (objeto)carrito__(propuedad)id_carrito

    producto.clicks += 1
    producto.save()

    context = {
        'producto':producto,
        'en_carrito':en_carrito,
    }

    return render(request, 'tienda/producto_detalles.html', context)

def _crear_favoritos(request):
    id_favorito = request.session.session_key

    if not id_favorito:
        id_favorito = request.session.create()    
    return id_favorito

def get_current_path(request):
    return {
       'current_path': request.get_full_path()
     }

def agregandoFavorito(request, id_producto):
    url = request.META.get('HTTP_REFERER')

    producto = Productos.objects.get(id=id_producto)

    try:
        favoritos = Favoritos.objects.get(id_favorito=_crear_favoritos(request))
    except Favoritos.DoesNotExist:
        favoritos = Favoritos.objects.create(id_favorito=_crear_favoritos(request))
        favoritos.save()
    
    try:
        producto_favorito = itemFavoritos.objects.get(product=producto, favorit=favoritos)
    except itemFavoritos.DoesNotExist:
        producto_favorito = itemFavoritos.objects.create(product=producto, favorit=favoritos, user=request.user)
        producto_favorito.save()
    
    return redirect(url)

def quitandoFavorito(request, id_producto):
    url = request.META.get('HTTP_REFERER')
    producto = Productos.objects.get(id=id_producto)

    try:
        favoritos = Favoritos.objects.get(id_favorito=_crear_favoritos(request))
    except Favoritos.DoesNotExist:
        pass
    
    try:
        itemFavoritos.objects.get(product=producto, user=request.user).delete()
    except:
        pass

    _favoritos_Existe(request)

    return redirect(url)

def _favoritos_Existe(request):
    
    try:
        favoritos = Favoritos.objects.get(id_favorito=_crear_favoritos(request))
        items_favoritos = itemFavoritos.objects.filter(favorit=favoritos).exists()
        if items_favoritos == False:
            favoritos.delete()
        else:
            pass
    except:
        pass
