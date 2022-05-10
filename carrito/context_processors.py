from .models import Carrito, cartItem
from .views import _cart_id

def cantidadItemsCarrito(request):

    cantidad = 0

    try:
        carrito = Carrito.objects.filter(id_carrito=_cart_id(request))
        cart_items = cartItem.objects.all().filter(carrito=carrito[:1])

        for i in cart_items:
            cantidad += i.cantidad
            
    except Carrito.DoesNotExist:
        cantidad = 0

    return dict(cantidad=cantidad)
    