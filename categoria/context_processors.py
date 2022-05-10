from .models import Categoria

def categorias(request):
    todas_categorias = Categoria.objects.all()
    return dict(todas_categorias=todas_categorias) #Esto es para que me retorne el diccionario