from django import forms
from .models import Categoria, Receta

class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ['titulo', 'ingredientes', 'instrucciones', 'tiempo_preparacion', 'imagen', 'categoria']
    
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), empty_label="Selecciona una categoría")

