from django.shortcuts import render, get_object_or_404
from .models import Receta


def lista_recetas(request):
    recetas = Receta.objects.all().order_by('-fecha_creacion')
    return render(request, 'recetas/lista_recetas.html', {'recetas': recetas})


def detalle_receta(request, receta_id):
    receta = get_object_or_404(Receta, id=receta_id)
    return render(request, 'recetas/detalle_receta.html', {'receta': receta})
