from django.urls import path
from . import views

urlpatterns = [
    path('registrarse/', views.register, name='registrarse'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', views.dashboard, name='dashboard'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),

    #Recuperando contrase;a
    path('forgotPassword', views.forgotpassword, name='forgotpassword'),
    path('resetearpassword_validate/<uidb64>/<token>/', views.resetearpassword_validate, name='resetearpassword_validate'),
    path('resetearpassword', views.resetearpassword, name='resetearpassword'),
]
