from django.shortcuts import render, get_object_or_404, redirect
from auto.models import Carrera, Piloto, RegistroCarrera
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request,'index.html')

def ListaCarrera(request):
    carrera = Carrera.objects.all
    return render(request,'carrera/listaCarrera.html',{'carrera':carrera})

def ListaPiloto(request):
    piloto = Piloto.objects.all
    return render(request,'piloto/listaPiloto.html',{'piloto':piloto})

def ListaRegistro(request):
    registro = RegistroCarrera.objects.all
    return render(request, 'registro/listaRegistro.html',{'registro':registro})
