from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
class AccountAdmin(UserAdmin): #Clase para mostrar datos dentro de apartado de administracion de Django
    list_display = ('is_active', 'id', 'email', 'first_name', 'date_joined', 'last_login',) #Se usa una tupla para enviar los datos que queremos
    list_display_links = ('id', 'email',) # list_display_link es para que pueda llevarte a la informacion de ese usuario desde los datos
    readonly_fields = ('date_joined', 'last_login',) #el readonly sirve para que esos datos solo puedan ser leidos mas no editados
    ordering = ('-date_joined',) # ordering sirve para ordenar la lista por un parametro, en este caso, ordenamos por cuando se creo la cuenta con el '-' para indicar ascedente

    #Necesario para guardar cambios hechos en el panel de administracion de django, de lo contrario, no se mostraran los datos
    filter_horizontal = () #Obligatorio
    list_filter = () # Para mostrar un filtro a la derecha del board #Obligatorio
    search_fields = ('id', 'first_name', 'email', 'username') #Para conseguir un objeto en la barra de busqueda
    fieldsets = () #Obligatorio
    #Para mas informacion visitar http://codestudyblog.com/cnb/0320103004.html

admin.site.register(User, AccountAdmin)
