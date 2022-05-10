from django.urls import path
from . import views

urlpatterns = [
    path('', views.tienda, name='tienda'),
    path('filtro/<slug:slug>/', views.tienda, name='filtro_categoria'),
    path('filtro/<precio_min>/', views.tienda, name='filtro_precio'), #<precio_min> es el parametro que estoy necesitando para buscar el precio
    path('buscar/', views.buscar, name='buscar'),
    path('favorito/<int:id_producto>', views.agregandoFavorito, name='favorito'),
    path('', views.agregandoFavorito, name='favoritos'),
    path('quitandoFavorito/<int:id_producto>', views.quitandoFavorito, name='quitandoFavorito'),
    #Detalles del producto
    path('detalles_producto/<slug:slug>', views.detalles, name='detalles_producto'),
]
