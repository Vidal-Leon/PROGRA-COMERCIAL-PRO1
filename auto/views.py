from django.shortcuts import render, get_object_or_404, redirect
from auto.models import Carrera, Piloto, RegistroCarrera
from django.contrib import messages
from .forms import CarreraForm, PilotoForm


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

def NuevaCarrera(request):
    if request.method == "POST":
        formulario = CarreraForm(request.POST)
        if formulario.is_valid():

            carrera = Carrera(lugar=formulario.cleaned_data['lugar'],
            fechainicio=formulario.cleaned_data['fechainicio'],
            fechafinal=formulario.cleaned_data['fechafinal'])
            carrera.save()
            messages.add_message(request,messages.SUCCESS,'Datos agregados')
        return redirect('ListaCarrera')
    else:
        form = CarreraForm()
        return render(request,'carrera/editarCarrera.html')

def EliminarCarrera(request, pk):
    carrera = get_object_or_404(Carrera, pk=pk)
    carrera.delete()
    return redirect('ListaCarrera')

def NuevoPiloto(request):
    if request.method == "POST":
        formulario = PilotoForm(request.POST)
        if formulario.is_valid():

            piloto = Piloto(nombre=formulario.cleaned_data['nombre'],
            equipo=formulario.cleaned_data['equipo'],
            vehiculo=formulario.cleaned_data['vehiculo'])
            piloto.save()
            messages.add_message(request,messages.SUCCESS,'Datos agregados')
        return redirect('ListaPiloto')
    else:
        form = PilotoForm()
        return render(request,'piloto/editarPiloto.html')

def NuevoRegistro(request):
    if request.method == "POST":
        formulario = RegistroForm(request.POST)
        if formulario.is_valid():

            registro = RegistroCarrera(piloto=formulario.cleaned_data['piloto'],
            Posicion=formulario.cleaned_data['Posicion'],
            carrera=formulario.cleaned_data['carrera'])
            registro.save()
            messages.add_message(request,messages.SUCCESS,'Datos agregados')
        return redirect('ListaPiloto')
    else:
        form = RegistroForm()
        return render(request,'registro/editarRegistro.html')
