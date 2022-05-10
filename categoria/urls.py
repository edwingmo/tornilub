from django.urls import path
from . import views

urlpatterns = [
    path('', views.Categoria, name='categoria'),
]
