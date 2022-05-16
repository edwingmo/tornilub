from django.contrib import admin
from .models import Carrito, cartItem

"""class CarritoAdmin(admin.ModelAdmin):
    list_display=('id_carrito',)

class CarritoItemAdmin(admin.ModelAdmin):
    list_display=('product',)
    list_display_links = ('product',)

# Register your models here.
admin.site.register(Carrito, CarritoAdmin)
admin.site.register(cartItem, CarritoItemAdmin)
"""