from django.urls import path
from . import views

urlpatterns = [
    path('', views.solicitarcot, name='solicitarcot'),    
    path('<int:id_product>/', views.solicitarcot, name='solicitarcot'),
    path('enviarcotiz/', views.enviarcotiz, name='enviarcotiz'),
]
