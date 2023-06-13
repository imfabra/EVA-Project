from django import forms
from .models import Etiqueta, Movimiento, Submovimiento

class EtiquetaForm(forms.ModelForm):
    class Meta:
        model = Etiqueta
        fields = ['nombre', 'descripcion']

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        etiqueta_exists = Etiqueta.objects.filter(nombre__iexact=nombre).exists()
        if etiqueta_exists:
            raise forms.ValidationError("Ya existe una etiqueta con este nombre.")
        return nombre


class MovimientoForm(forms.ModelForm):
    class Meta:
        model = Movimiento
        fields = ['etiqueta', 'descripcion']

class SubmovimientoForm(forms.ModelForm):
    class Meta:
        model = Submovimiento
        fields = ['movimiento', 'join1', 'join2', 'join3', 'join4', 'join5', 'velocidad', 'tiempo', 'orden']


