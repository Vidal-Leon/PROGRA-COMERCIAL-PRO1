from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import include, url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    url(r'^carrera/', views.ListaCarrera, name='ListaCarrera'),
    url(r'^piloto/', views.ListaPiloto, name='ListaPiloto'),
    url(r'^registro/', views.ListaRegistro, name='ListaRegistro'),
]
