from django.shortcuts import render
from tienda.views import Productos

def Home(request):
    title = 'Inicio'
    productos = Productos.objects.all().filter(activo=True)

    context = {
        'productos':productos,
        'title':title,
    }
    return render(request, 'index.html', context)