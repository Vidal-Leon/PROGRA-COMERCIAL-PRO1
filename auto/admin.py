from django.contrib import admin
from .models import Carrera, Piloto, RegistroCarrera
# Register your models here.

admin.site.register(Carrera)
admin.site.register(Piloto)
admin.site.register(RegistroCarrera)
