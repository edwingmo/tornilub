"""irsmain URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from . import views

#Importes para imagenes
from django.conf import settings # Necesario para indicarle las rutas medias que se colocan en el setting
from django.conf.urls.static import static
#Fin de importe para imagenes

urlpatterns = [
    path('xfs78vxsa63/', admin.site.urls),
    path('', views.Home, name="home"), # Pagina principal por ahora
    path('categoria/', include('categoria.urls')),
    path('tienda/', include('tienda.urls')),
    path('carrito/', include('carrito.urls')),
    path('cotizacion/', include('cotizacion.urls')),
    path('account/', include('accounts.urls')),
]

from decouple import config

if config('DEBUG'):
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
else:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

