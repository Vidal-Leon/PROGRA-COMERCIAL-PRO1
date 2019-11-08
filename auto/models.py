from django.db import models
from django.contrib import admin

# Create your models here.

class Carrera(models.Model):
    lugar = models.CharField(max_length = 90)
    fechainicio = models.DateField()
    fechafinal = models.DateField()
    def _str_(self):
        return self.lugar

class Piloto(models.Model):
    nombre = models.CharField(max_length = 70)
    equipo = models.CharField(max_length = 90)
    vehiculo = models.CharField(max_length = 200)
    def _str_(self):
        return self.nombre

class RegistroCarrera(models.Model):
    piloto = models.ForeignKey(Piloto, on_delete=models.CASCADE)
    Posicion = models.CharField(max_length = 70)
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    def _str_(self):
        return self.Posicion

class RegistroCarreraInLine(admin.TabularInline):
    model = RegistroCarrera
    extra = 1

class CarreraAdmin(admin.ModelAdmin):
    inLines = (RegistroCarreraInLine,)

class PilotoAdmin(admin.ModelAdmin):
    inLines = (RegistroCarreraInLine,)
