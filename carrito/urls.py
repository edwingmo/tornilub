from django.urls import path
from . import views

urlpatterns = [
    path('', views.carrito, name='carrito'),
    path('add_cart/<int:id_producto>', views.AgregarProducto, name='add_cart'),
    path('rest_cart/<int:id_producto>', views.QuitarProducto, name='rest_cart'),
    path('delete_product/<int:id_producto>', views.EliminarProducto, name='delete_product'),
]
