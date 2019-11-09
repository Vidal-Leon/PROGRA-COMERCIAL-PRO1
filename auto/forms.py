from django.contrib.admin import widgets
from django import forms
from .models import Carrera, Piloto

class CarreraForm(forms.ModelForm):
    class Meta:
        model = Carrera
        fields = ('lugar','fechainicio','fechafinal',)

class PilotoForm(forms.ModelForm):
    class Meta:
        model = Piloto
        fields = ('nombre', 'equipo', 'vehiculo',)
