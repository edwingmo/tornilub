from .models import Productos, Favoritos, itemFavoritos
from .views import _crear_favoritos
from decouple import config

def contextoPublico(request):
    cantidad_producto = Productos.objects.all().count
    clicks = Productos.objects.all().order_by('-clicks')[:4]
    productos = Productos.objects.all()

    
    favoritos = Favoritos.objects.filter(id_favorito=_crear_favoritos(request))
    favoritos_items = itemFavoritos.objects.filter(favorit=favoritos[:1])

    if request.user.is_authenticated:
        favoritos_items = itemFavoritos.objects.filter(user=request.user)      
        
    else:
        favoritos_items = itemFavoritos.objects.filter(favorit=favoritos[:1])

    favoritos_cantidad = False
    favoritos_list = []

    if len(favoritos_items) > 0:
        favoritos_cantidad = True
    else:
        favoritos_cantidad = False

    for favorito in favoritos_items:
        favoritos_list.append(favorito.product.id)
    
    
    context = {
        'cantidad_productos':cantidad_producto,
        'clicks':clicks,
        'products':productos,
        'favoritos':favoritos_items,
        'favoritos_existe':favoritos_cantidad,
        'lista_favoritos':favoritos_list,
        'urladmin':config("ADMIN"),
    }
    
    return context
