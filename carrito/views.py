
from django.shortcuts import redirect, render
from tienda.models import Productos
from .models import Carrito, cartItem

def _cart_id(request): #Como es una funcion privada solo trabajara aqui, se empieza el nombre de la funcion con un _
    cart_id = request.session.session_key # Se usa para obtener el id de la sesion del usuario
    if not cart_id:
        cart_id = request.session.create() #Si no existe esa session entonces se crea
    return cart_id

#Agregando producto al carrito
def AgregarProducto(request, id_producto):
    producto = Productos.objects.get(id=id_producto)

    try:
        carrito = Carrito.objects.get(id_carrito=_cart_id(request)) #si el carrito existe
    except Carrito.DoesNotExist:
        carrito = Carrito.objects.create(id_carrito=_cart_id(request))
        carrito.save()

    try:
        cart_item = cartItem.objects.get(product=producto, carrito=carrito)
        cart_item.cantidad += 1 #Para saber cuantos productos de este quiere
        cart_item.save()
    except cartItem.DoesNotExist:
        cart_item = cartItem.objects.create(product=producto, carrito=carrito, cantidad=1)
        cart_item.save()

    return redirect('carrito')

def QuitarProducto(request, id_producto):
    producto = Productos.objects.get(id=id_producto)
    carrito = Carrito.objects.get(id_carrito=_cart_id(request)) #si el carrito existe
    cart_item = cartItem.objects.get(product=producto, carrito=carrito)

    if cart_item.cantidad > 0:
        cart_item.cantidad -= 1 #Para saber cuantos productos de este quiere
        cart_item.save()
    else:
        cart_item.delete()

    return redirect('carrito')

def EliminarProducto(request, id_producto):
    producto = Productos.objects.get(id=id_producto)
    carrito = Carrito.objects.get(id_carrito=_cart_id(request))
    cart_item = cartItem.objects.filter(carrito=carrito, product=producto)

    cart_item.delete()

    return redirect('carrito')

# Create your views here.
def carrito(request, total=0, cart_items=None, cantidad=0):
    title = "Carrito"
    try:
        carrito = Carrito.objects.get(id_carrito=_cart_id(request))
        cart_items = cartItem.objects.filter(carrito=carrito)

        #Total precoio producto
        for i in cart_items:
            total += (i.product.precio * i.cantidad)
            cantidad += i.cantidad
            
    except Carrito.DoesNotExist:
        pass

    context = {
        'title':title,
        'cart_items':cart_items,
        'total':total,
    }
    return render(request, 'tienda/carrito.html', context)
