from django import forms
from .models import Receta

class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ['titulo', 'ingredientes', 'instrucciones', 'tiempo_preparacion', 'imagen', 'categoria']
